# SPDX-License-Identifier: Apache-2.0
# Copyright © Viktor Savitskiy, 2025
# DHAIE Project – Reflexive AI Infrastructure
# Repository: https://github.com/designhumanai/dhaie-rai-core

"""
Neo4j Client for DHAIE Semantic Observer

Manages connections to Neo4j graph database and provides methods for
semantic knowledge graph operations.

This is the persistence layer for the reflexive architecture intelligence.
"""

from neo4j import GraphDatabase, Driver, Session
from neo4j.exceptions import ServiceUnavailable, AuthError
from typing import Optional, Dict, Any, List
import logging

logger = logging.getLogger(__name__)


class Neo4jClient:
    """
    Neo4j database client for semantic knowledge graph operations.
    
    This client manages the connection to Neo4j and provides methods for:
    - Creating service nodes from manifests
    - Building semantic relationships
    - Querying the knowledge graph
    - Health checking the database connection
    """
    
    def __init__(self, uri: str, user: str, password: str):
        """
        Initialize Neo4j client.
        
        Args:
            uri: Neo4j connection URI (bolt://host:port)
            user: Neo4j username
            password: Neo4j password
            
        Raises:
            ServiceUnavailable: If Neo4j is not reachable
            AuthError: If credentials are invalid
        """
        self.uri = uri
        self.user = user
        self._driver: Optional[Driver] = None
        
        logger.info(f"Initializing Neo4j client: {uri}")
        
        try:
            self._driver = GraphDatabase.driver(
                uri,
                auth=(user, password),
                max_connection_lifetime=3600,
                max_connection_pool_size=50,
                connection_timeout=30,
                encrypted=False  # Use True with neo4j+s:// in production
            )
            
            # Verify connectivity
            self._driver.verify_connectivity()
            logger.info("✅ Neo4j connection established")
            
        except ServiceUnavailable as e:
            logger.error(f"❌ Neo4j service unavailable: {e}")
            raise
        except AuthError as e:
            logger.error(f"❌ Neo4j authentication failed: {e}")
            raise
        except Exception as e:
            logger.error(f"❌ Neo4j connection error: {e}")
            raise
    
    def close(self):
        """
        Close the Neo4j driver connection.
        
        Should be called on application shutdown.
        """
        if self._driver:
            self._driver.close()
            logger.info("Neo4j connection closed")
    
    def verify_connectivity(self) -> bool:
        """
        Verify Neo4j connection is active.
        
        Returns:
            True if connection is healthy, False otherwise
        """
        try:
            if not self._driver:
                return False
            
            self._driver.verify_connectivity()
            return True
            
        except Exception as e:
            logger.error(f"Neo4j connectivity check failed: {e}")
            return False
    
    def get_database_info(self) -> Dict[str, Any]:
        """
        Get Neo4j database information and statistics.
        
        Returns:
            Dictionary with database version, node count, relationship count
        """
        try:
            with self._driver.session() as session:
                # Get Neo4j version
                version_result = session.run("CALL dbms.components() YIELD versions")
                version = version_result.single()["versions"][0] if version_result.peek() else "unknown"
                
                # Get node count
                node_count_result = session.run("MATCH (n) RETURN count(n) as count")
                node_count = node_count_result.single()["count"]
                
                # Get relationship count
                rel_count_result = session.run("MATCH ()-[r]->() RETURN count(r) as count")
                rel_count = rel_count_result.single()["count"]
                
                # Get service manifest count
                manifest_count_result = session.run(
                    "MATCH (s:Service) RETURN count(s) as count"
                )
                manifest_count = manifest_count_result.single()["count"]
                
                return {
                    "version": version,
                    "total_nodes": node_count,
                    "total_relationships": rel_count,
                    "service_manifests": manifest_count,
                    "connected": True
                }
                
        except Exception as e:
            logger.error(f"Failed to get database info: {e}")
            return {
                "version": "unknown",
                "total_nodes": 0,
                "total_relationships": 0,
                "service_manifests": 0,
                "connected": False,
                "error": str(e)
            }
    
    def initialize_schema(self) -> bool:
        """
        Initialize Neo4j schema with constraints and indexes.
        
        Creates:
        - Unique constraint on Service.id
        - Index on Service.name
        - Index on Service.domainContext
        
        Returns:
            True if schema initialization successful
        """
        try:
            with self._driver.session() as session:
                logger.info("Initializing Neo4j schema...")
                
                # Create unique constraint on Service.id
                session.run(
                    """
                    CREATE CONSTRAINT service_id_unique IF NOT EXISTS
                    FOR (s:Service) REQUIRE s.id IS UNIQUE
                    """
                )
                logger.info("✅ Created constraint: service_id_unique")
                
                # Create index on Service.name
                session.run(
                    """
                    CREATE INDEX service_name_idx IF NOT EXISTS
                    FOR (s:Service) ON (s.name)
                    """
                )
                logger.info("✅ Created index: service_name_idx")
                
                # Create index on Service.domainContext
                session.run(
                    """
                    CREATE INDEX service_domain_idx IF NOT EXISTS
                    FOR (s:Service) ON (s.domainContext)
                    """
                )
                logger.info("✅ Created index: service_domain_idx")
                
                # Create index on Service.manifestVersion
                session.run(
                    """
                    CREATE INDEX service_manifest_version_idx IF NOT EXISTS
                    FOR (s:Service) ON (s.manifestVersion)
                    """
                )
                logger.info("✅ Created index: service_manifest_version_idx")
                
                logger.info("✅ Neo4j schema initialization complete")
                return True
                
        except Exception as e:
            logger.error(f"Schema initialization failed: {e}")
            return False
    
    def create_service_node(self, manifest: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create or update a service node from a manifest.
        
        Args:
            manifest: Service manifest dictionary (validated)
            
        Returns:
            Created/updated service node properties
            
        Raises:
            Exception: If service creation fails
        """
        try:
            with self._driver.session() as session:
                result = session.run(
                    """
                    MERGE (s:Service {id: $id})
                    SET s.name = $name,
                        s.version = $version,
                        s.manifestVersion = $manifestVersion,
                        s.description = $description,
                        s.businessPurpose = $businessPurpose,
                        s.domainContext = $domainContext,
                        s.providerName = $providerName,
                        s.consentMechanism = $consentMechanism,
                        s.updatedAt = datetime()
                    ON CREATE SET s.createdAt = datetime()
                    RETURN s
                    """,
                    id=manifest["@id"],
                    name=manifest["name"],
                    version=manifest["version"],
                    manifestVersion=manifest["dhaie:manifestVersion"],
                    description=manifest["description"],
                    businessPurpose=manifest["dhaie:businessPurpose"],
                    domainContext=manifest["dhaie:domainContext"],
                    providerName=manifest["provider"]["name"],
                    consentMechanism=manifest.get("dhaie:consentMechanism")
                )
                
                service_node = result.single()["s"]
                logger.info(f"✅ Created/updated service node: {manifest['name']}")
                
                return dict(service_node)
                
        except Exception as e:
            logger.error(f"Failed to create service node: {e}")
            raise
    
    def find_service_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Find a service by name.
        
        Args:
            name: Service name
            
        Returns:
            Service node properties or None if not found
        """
        try:
            with self._driver.session() as session:
                result = session.run(
                    """
                    MATCH (s:Service {name: $name})
                    RETURN s
                    """,
                    name=name
                )
                
                record = result.single()
                if record:
                    return dict(record["s"])
                return None
                
        except Exception as e:
            logger.error(f"Failed to find service by name: {e}")
            return None
    
    def get_all_services(self) -> List[Dict[str, Any]]:
        """
        Get all services in the knowledge graph.
        
        Returns:
            List of service node properties
        """
        try:
            with self._driver.session() as session:
                result = session.run(
                    """
                    MATCH (s:Service)
                    RETURN s
                    ORDER BY s.name
                    """
                )
                
                services = [dict(record["s"]) for record in result]
                logger.info(f"Retrieved {len(services)} services")
                return services
                
        except Exception as e:
            logger.error(f"Failed to get all services: {e}")
            return []
    
    def delete_all_data(self) -> bool:
        """
        Delete all nodes and relationships in the database.
        
        WARNING: This is destructive and should only be used in development!
        
        Returns:
            True if deletion successful
        """
        try:
            with self._driver.session() as session:
                result = session.run("MATCH (n) DETACH DELETE n")
                logger.warning("⚠️  Deleted all data from Neo4j")
                return True
                
        except Exception as e:
            logger.error(f"Failed to delete all data: {e}")
            return False


# Global Neo4j client instance
_neo4j_client: Optional[Neo4jClient] = None


def get_neo4j_client() -> Optional[Neo4jClient]:
    """
    Get the global Neo4j client instance.
    
    Returns:
        Neo4jClient instance or None if not initialized
    """
    return _neo4j_client


def initialize_neo4j_client(uri: str, user: str, password: str) -> Neo4jClient:
    """
    Initialize the global Neo4j client instance.
    
    Args:
        uri: Neo4j connection URI
        user: Neo4j username
        password: Neo4j password
        
    Returns:
        Initialized Neo4jClient instance
        
    Raises:
        Exception: If initialization fails
    """
    global _neo4j_client
    
    if _neo4j_client is not None:
        logger.warning("Neo4j client already initialized, closing existing connection")
        _neo4j_client.close()
    
    _neo4j_client = Neo4jClient(uri, user, password)
    
    # Initialize schema
    _neo4j_client.initialize_schema()
    
    return _neo4j_client


def close_neo4j_client():
    """
    Close the global Neo4j client instance.
    """
    global _neo4j_client
    
    if _neo4j_client is not None:
        _neo4j_client.close()
        _neo4j_client = None
