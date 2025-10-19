# SPDX-License-Identifier: Apache-2.0
# Copyright © Viktor Savitskiy, 2025
# DHAIE Project – Reflexive AI Infrastructure
# Repository: https://github.com/designhumanai/dhaie-rai-core

"""
DHAIE Semantic Observer - Main Application

The Semantic Observer is the intelligence aggregator that collects service manifests,
builds a live knowledge graph, and exposes semantic queries via REST API.

This is the brain of the reflexive system that makes architecture understandable.
"""

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime
import logging
import os

# Import Neo4j client
from app.neo4j_client import (
    initialize_neo4j_client,
    close_neo4j_client,
    get_neo4j_client
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Environment variables
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "dhaie-rai-dev")

# Initialize FastAPI application
app = FastAPI(
    title="DHAIE Semantic Observer",
    description="Real-time architecture intelligence aggregator for Reflexive AI systems",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0"
    },
    contact={
        "name": "DHAIE Project",
        "url": "https://github.com/designhumanai/dhaie-rai-core",
        "email": "info@designhumanai.com"
    }
)

# CORS middleware for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models for API
class HealthResponse(BaseModel):
    """Health check response model"""
    status: str = Field(..., description="Service health status")
    timestamp: str = Field(..., description="ISO 8601 timestamp")
    version: str = Field(..., description="Service version")
    neo4j_connected: bool = Field(..., description="Neo4j connection status")
    manifest_count: Optional[int] = Field(None, description="Number of ingested manifests")

class ErrorResponse(BaseModel):
    """Standard error response"""
    error: str = Field(..., description="Error type")
    message: str = Field(..., description="Human-readable error message")
    details: Optional[Dict[str, Any]] = Field(None, description="Additional error context")

# Startup event
@app.on_event("startup")
async def startup_event():
    """
    Application startup tasks.
    
    Initializes connections and validates configuration.
    """
    logger.info("🚀 DHAIE Semantic Observer starting...")
    logger.info(f"📊 Neo4j URI: {NEO4J_URI}")
    logger.info(f"👤 Neo4j User: {NEO4J_USER}")
    logger.info("✅ FastAPI application initialized")
    
    # Initialize Neo4j connection
    try:
        neo4j_client = initialize_neo4j_client(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)
        logger.info("✅ Neo4j client initialized and schema created")
        
        # Log database info
        db_info = neo4j_client.get_database_info()
        logger.info(f"📊 Neo4j version: {db_info['version']}")
        logger.info(f"📊 Total nodes: {db_info['total_nodes']}")
        logger.info(f"📊 Service manifests: {db_info['service_manifests']}")
        
    except Exception as e:
        logger.error(f"❌ Failed to initialize Neo4j: {e}")
        logger.warning("⚠️  Service will run in degraded mode without graph storage")

# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    """
    Application shutdown tasks.
    
    Gracefully closes connections and cleanup resources.
    """
    logger.info("🛑 DHAIE Semantic Observer shutting down...")
    
    # Close Neo4j connection
    close_neo4j_client()
    
    logger.info("✅ Shutdown complete")

# Root endpoint
@app.get(
    "/",
    summary="Root endpoint",
    description="Returns basic service information",
    response_model=Dict[str, str]
)
async def root():
    """
    Root endpoint providing service identity.
    
    Returns:
        Basic service information including name, version, and documentation links
    """
    return {
        "@context": "https://schema.org/",
        "@type": "SoftwareApplication",
        "name": "DHAIE Semantic Observer",
        "version": "1.0.0",
        "description": "Real-time architecture intelligence aggregator",
        "documentation": "/docs",
        "health": "/health",
        "manifest": "https://github.com/designhumanai/dhaie-rai-core"
    }

# Health check endpoint
@app.get(
    "/health",
    summary="Health check",
    description="Returns service health status and connectivity",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK
)
async def health_check():
    """
    Health check endpoint for monitoring and orchestration.
    
    Validates:
    - Service is running
    - Neo4j connection is active
    - Basic system metrics
    
    Returns:
        HealthResponse with current service status
    
    Raises:
        HTTPException: If critical dependencies are unavailable
    """
    try:
        # Check Neo4j connection
        neo4j_client = get_neo4j_client()
        
        if neo4j_client is None:
            # Neo4j not initialized
            health_status = HealthResponse(
                status="degraded",
                timestamp=datetime.utcnow().isoformat() + "Z",
                version="1.0.0",
                neo4j_connected=False,
                manifest_count=None
            )
        else:
            # Get Neo4j database info
            neo4j_connected = neo4j_client.verify_connectivity()
            db_info = neo4j_client.get_database_info()
            
            health_status = HealthResponse(
                status="healthy" if neo4j_connected else "degraded",
                timestamp=datetime.utcnow().isoformat() + "Z",
                version="1.0.0",
                neo4j_connected=neo4j_connected,
                manifest_count=db_info.get("service_manifests")
            )
        
        logger.info(f"Health check: {health_status.status}")
        return health_status
        
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={
                "error": "HealthCheckFailed",
                "message": "Service health check failed",
                "details": {"exception": str(e)}
            }
        )

# Placeholder for manifest ingestion (Step 3)
@app.post(
    "/manifests",
    summary="Ingest service manifest",
    description="Accept and validate a DHAIE service manifest (v1.1)",
    status_code=status.HTTP_501_NOT_IMPLEMENTED
)
async def ingest_manifest():
    """
    Manifest ingestion endpoint (to be implemented in Step 3).
    
    This endpoint will:
    1. Validate manifest against schema v1.1
    2. Extract semantic metadata
    3. Store in Neo4j knowledge graph
    4. Return ingestion confirmation
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail={
            "error": "NotImplemented",
            "message": "Manifest ingestion will be implemented in Step 3",
            "next_step": "Step 2: Neo4j integration"
        }
    )

# Placeholder for graph queries (Step 4)
@app.get(
    "/graph/service/{name}",
    summary="Query service by name",
    description="Retrieve service details from knowledge graph",
    status_code=status.HTTP_501_NOT_IMPLEMENTED
)
async def get_service(name: str):
    """
    Service query endpoint (to be implemented in Step 4).
    
    Args:
        name: Service name from manifest
        
    Returns:
        Complete service manifest with relationships
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail={
            "error": "NotImplemented",
            "message": f"Service query for '{name}' will be implemented in Step 4",
            "next_step": "Step 3: Manifest ingestion"
        }
    )

# Custom exception handler
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """
    Custom HTTP exception handler for consistent error responses.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.detail if isinstance(exc.detail, dict) else {
            "error": "HTTPException",
            "message": str(exc.detail)
        }
    )

# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """
    Catch-all exception handler for unexpected errors.
    """
    logger.error(f"Unhandled exception: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "InternalServerError",
            "message": "An unexpected error occurred",
            "details": {"exception_type": type(exc).__name__}
        }
    )

if __name__ == "__main__":
    import uvicorn
    
    # For development only
    logger.info("🔧 Running in development mode")
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
        log_level="info"
    )
