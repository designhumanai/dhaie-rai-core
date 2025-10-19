# SPDX-License-Identifier: Apache-2.0
# Copyright © Viktor Savitskiy, 2025
# DHAIE Project – Reflexive AI Infrastructure
# Repository: https://github.com/designhumanai/dhaie-rai-core

"""
Tests for Neo4j Client

Tests Neo4j connection, schema initialization, and basic operations.
"""

import pytest
from app.neo4j_client import Neo4jClient
import os


@pytest.fixture
def neo4j_uri():
    """Get Neo4j URI from environment or use default"""
    return os.getenv("NEO4J_URI", "bolt://localhost:7687")


@pytest.fixture
def neo4j_credentials():
    """Get Neo4j credentials from environment or use defaults"""
    return {
        "user": os.getenv("NEO4J_USER", "neo4j"),
        "password": os.getenv("NEO4J_PASSWORD", "dhaie-rai-dev")
    }


@pytest.fixture
def neo4j_client(neo4j_uri, neo4j_credentials):
    """Create Neo4j client fixture"""
    client = Neo4jClient(
        neo4j_uri,
        neo4j_credentials["user"],
        neo4j_credentials["password"]
    )
    
    # Clean database before tests
    client.delete_all_data()
    
    # Initialize schema
    client.initialize_schema()
    
    yield client
    
    # Cleanup after tests
    client.delete_all_data()
    client.close()


def test_neo4j_connection(neo4j_client):
    """Test: Neo4j connection is established"""
    assert neo4j_client.verify_connectivity() is True


def test_schema_initialization(neo4j_client):
    """Test: Schema constraints and indexes are created"""
    result = neo4j_client.initialize_schema()
    assert result is True


def test_get_database_info(neo4j_client):
    """Test: Can retrieve database information"""
    db_info = neo4j_client.get_database_info()
    
    assert "version" in db_info
    assert "total_nodes" in db_info
    assert "total_relationships" in db_info
    assert "service_manifests" in db_info
    assert db_info["connected"] is True


def test_create_service_node(neo4j_client):
    """Test: Can create a service node from manifest"""
    
    # Minimal valid manifest
    manifest = {
        "@id": "https://example.com/services/test-service/v1/manifest",
        "name": "Test Service",
        "version": "1.0.0",
        "dhaie:manifestVersion": "1.1",
        "description": "A test service for unit testing",
        "dhaie:businessPurpose": "Validate Neo4j client functionality",
        "dhaie:domainContext": "Testing.Unit.Neo4j",
        "provider": {
            "name": "Test Organization"
        },
        "dhaie:consentMechanism": "no_pii_processed"
    }
    
    # Create service node
    service_node = neo4j_client.create_service_node(manifest)
    
    # Verify node properties
    assert service_node["name"] == "Test Service"
    assert service_node["version"] == "1.0.0"
    assert service_node["manifestVersion"] == "1.1"
    assert service_node["domainContext"] == "Testing.Unit.Neo4j"
    assert service_node["consentMechanism"] == "no_pii_processed"


def test_find_service_by_name(neo4j_client):
    """Test: Can find service by name"""
    
    # Create test service
    manifest = {
        "@id": "https://example.com/services/findable-service/v1/manifest",
        "name": "Findable Service",
        "version": "1.0.0",
        "dhaie:manifestVersion": "1.1",
        "description": "A service that can be found",
        "dhaie:businessPurpose": "Test service lookup functionality",
        "dhaie:domainContext": "Testing.Unit.Lookup",
        "provider": {
            "name": "Test Organization"
        }
    }
    
    neo4j_client.create_service_node(manifest)
    
    # Find service
    found_service = neo4j_client.find_service_by_name("Findable Service")
    
    assert found_service is not None
    assert found_service["name"] == "Findable Service"
    assert found_service["domainContext"] == "Testing.Unit.Lookup"


def test_find_nonexistent_service(neo4j_client):
    """Test: Returns None for nonexistent service"""
    
    result = neo4j_client.find_service_by_name("Nonexistent Service")
    assert result is None


def test_get_all_services(neo4j_client):
    """Test: Can retrieve all services"""
    
    # Create multiple services
    manifests = [
        {
            "@id": f"https://example.com/services/service-{i}/v1/manifest",
            "name": f"Service {i}",
            "version": "1.0.0",
            "dhaie:manifestVersion": "1.1",
            "description": f"Test service number {i}",
            "dhaie:businessPurpose": f"Test service {i} purpose",
            "dhaie:domainContext": f"Testing.Unit.Service{i}",
            "provider": {
                "name": "Test Organization"
            }
        }
        for i in range(1, 4)
    ]
    
    for manifest in manifests:
        neo4j_client.create_service_node(manifest)
    
    # Get all services
    all_services = neo4j_client.get_all_services()
    
    assert len(all_services) == 3
    assert all(s["name"].startswith("Service") for s in all_services)


def test_update_existing_service(neo4j_client):
    """Test: Updating service node with same ID"""
    
    # Create initial service
    manifest_v1 = {
        "@id": "https://example.com/services/updatable/v1/manifest",
        "name": "Updatable Service",
        "version": "1.0.0",
        "dhaie:manifestVersion": "1.1",
        "description": "Original description",
        "dhaie:businessPurpose": "Original purpose",
        "dhaie:domainContext": "Testing.Unit.Update",
        "provider": {
            "name": "Test Organization"
        }
    }
    
    neo4j_client.create_service_node(manifest_v1)
    
    # Update service
    manifest_v2 = manifest_v1.copy()
    manifest_v2["version"] = "2.0.0"
    manifest_v2["description"] = "Updated description"
    
    neo4j_client.create_service_node(manifest_v2)
    
    # Verify update (should have only 1 node)
    all_services = neo4j_client.get_all_services()
    assert len(all_services) == 1
    
    # Verify updated properties
    updated_service = neo4j_client.find_service_by_name("Updatable Service")
    assert updated_service["version"] == "2.0.0"
    assert updated_service["description"] == "Updated description"


def test_service_count_in_database_info(neo4j_client):
    """Test: Database info reflects correct service count"""
    
    # Initially empty
    db_info = neo4j_client.get_database_info()
    assert db_info["service_manifests"] == 0
    
    # Add services
    for i in range(5):
        manifest = {
            "@id": f"https://example.com/services/counted-{i}/v1/manifest",
            "name": f"Counted Service {i}",
            "version": "1.0.0",
            "dhaie:manifestVersion": "1.1",
            "description": f"Service for count test {i}",
            "dhaie:businessPurpose": f"Count validation {i}",
            "dhaie:domainContext": f"Testing.Count.Service{i}",
            "provider": {
                "name": "Test Organization"
            }
        }
        neo4j_client.create_service_node(manifest)
    
    # Verify count
    db_info = neo4j_client.get_database_info()
    assert db_info["service_manifests"] == 5


@pytest.mark.skip(reason="Requires Neo4j to be unavailable for testing")
def test_connection_failure_handling():
    """Test: Handles connection failures gracefully"""
    
    with pytest.raises(Exception):
        Neo4jClient("bolt://invalid-host:7687", "neo4j", "wrong-password")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
