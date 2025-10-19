// SPDX-License-Identifier: Apache-2.0
// Copyright © Viktor Savitskiy, 2025
// Part of DHAIE RAI Core

// ============================================================================
// DHAIE Semantic Observer - Neo4j Graph Schema
// ============================================================================
//
// This schema defines the knowledge graph structure for reflexive AI systems.
// It models services, their relationships, and ethical constraints.
//
// Node Labels:
//   - Service: Core service entity from manifests
//   - EthicalConstraint: Regulatory/ethical compliance declarations
//   - Operation: Service operations/capabilities
//   - SocialImpact: Social impact metrics
//
// Relationship Types:
//   - DEPENDS_ON: Semantic dependencies between services
//   - COMPLIES_WITH: Service compliance with ethical constraints
//   - HAS_OPERATION: Service capabilities
//   - HAS_IMPACT: Social impact declarations
//   - PROVIDED_BY: Service provider organization
// ============================================================================

// ----------------------------------------------------------------------------
// CONSTRAINTS (Uniqueness)
// ----------------------------------------------------------------------------

// Service nodes must have unique IDs (@id from manifest)
CREATE CONSTRAINT service_id_unique IF NOT EXISTS
FOR (s:Service) REQUIRE s.id IS UNIQUE;

// Ethical constraints identified by regulation name
CREATE CONSTRAINT ethical_constraint_id_unique IF NOT EXISTS
FOR (e:EthicalConstraint) REQUIRE e.id IS UNIQUE;

// Operations identified by service+operation name
CREATE CONSTRAINT operation_id_unique IF NOT EXISTS
FOR (o:Operation) REQUIRE o.id IS UNIQUE;

// ----------------------------------------------------------------------------
// INDEXES (Query Performance)
// ----------------------------------------------------------------------------

// Index on service name for fast lookup
CREATE INDEX service_name_idx IF NOT EXISTS
FOR (s:Service) ON (s.name);

// Index on domain context for domain queries
CREATE INDEX service_domain_idx IF NOT EXISTS
FOR (s:Service) ON (s.domainContext);

// Index on manifest version for compatibility checks
CREATE INDEX service_manifest_version_idx IF NOT EXISTS
FOR (s:Service) ON (s.manifestVersion);

// Index on consent mechanism for compliance queries
CREATE INDEX service_consent_idx IF NOT EXISTS
FOR (s:Service) ON (s.consentMechanism);

// Index on ethical constraint regulation name
CREATE INDEX ethical_regulation_idx IF NOT EXISTS
FOR (e:EthicalConstraint) ON (e.regulation);

// Index on operation category
CREATE INDEX operation_category_idx IF NOT EXISTS
FOR (o:Operation) ON (o.category);

// ----------------------------------------------------------------------------
// NODE PROPERTY SCHEMA (Documentation)
// ----------------------------------------------------------------------------

// Service Node Properties:
// - id: string (URI from @id field)
// - name: string (human-readable service name)
// - version: string (semver service version)
// - manifestVersion: string (manifest schema version, e.g., "1.1")
// - description: string (technical summary)
// - businessPurpose: string (why the service exists)
// - domainContext: string (dot-separated domain path)
// - providerName: string (organization name)
// - consentMechanism: string (consent handling approach)
// - createdAt: datetime (node creation timestamp)
// - updatedAt: datetime (last update timestamp)

// EthicalConstraint Node Properties:
// - id: string (generated from service_id + regulation)
// - regulation: string (constraint name, e.g., "GDPR")
// - uri: string (link to official regulation)
// - articles: list<string> (specific articles/sections)
// - implementation: string (how compliance is achieved)
// - verificationType: string (automated_scan, manual_audit, etc.)
// - verificationTool: string (name of verification tool)
// - lastVerified: date (last verification date)

// Operation Node Properties:
// - id: string (generated from service_id + operation_name)
// - name: string (operation identifier, camelCase)
// - description: string (operation explanation)
// - category: string (financial, dataQuery, etc.)
// - mutates: boolean (whether operation changes state)
// - piiFields: list<string> (PII field names)
// - auditRequired: boolean (whether audit logging required)

// SocialImpact Node Properties:
// - id: string (generated from service_id)
// - description: string (narrative impact description)
// - metrics: list<map> (structured impact metrics)

// ----------------------------------------------------------------------------
// RELATIONSHIP PROPERTY SCHEMA (Documentation)
// ----------------------------------------------------------------------------

// DEPENDS_ON Relationship Properties:
// - relationship: string (from DHAIE taxonomy, e.g., "data.provider.primary")
// - businessReason: string (why dependency exists)
// - consentImplications: string (data sharing implications)
// - conditionWhen: string (optional: activation condition)
// - conditionEnforcement: string (optional: mandatory/recommended/optional)
// - createdAt: datetime (relationship creation timestamp)

// COMPLIES_WITH Relationship Properties:
// - createdAt: datetime (compliance declaration timestamp)

// HAS_OPERATION Relationship Properties:
// - createdAt: datetime (operation declaration timestamp)

// HAS_IMPACT Relationship Properties:
// - createdAt: datetime (impact declaration timestamp)

// ----------------------------------------------------------------------------
// EXAMPLE QUERIES
// ----------------------------------------------------------------------------

// Find all services in a specific domain
// MATCH (s:Service)
// WHERE s.domainContext STARTS WITH 'FinTech.Payments'
// RETURN s.name, s.businessPurpose, s.domainContext
// ORDER BY s.name;

// Find services with GDPR compliance
// MATCH (s:Service)-[:COMPLIES_WITH]->(e:EthicalConstraint)
// WHERE e.regulation = 'GDPR'
// RETURN s.name, e.implementation, e.lastVerified;

// Find dependency graph for a service
// MATCH path = (s:Service {name: 'PaymentService'})-[:DEPENDS_ON*1..3]->(dep:Service)
// RETURN path;

// Find services requiring explicit consent
// MATCH (s:Service)
// WHERE s.consentMechanism = 'explicit_consent_required'
// RETURN s.name, s.businessPurpose;

// Find all operations that mutate state and handle PII
// MATCH (s:Service)-[:HAS_OPERATION]->(o:Operation)
// WHERE o.mutates = true AND size(o.piiFields) > 0
// RETURN s.name, o.name, o.piiFields;

// Find services with conditional dependencies
// MATCH (s:Service)-[r:DEPENDS_ON]->(dep:Service)
// WHERE r.conditionWhen IS NOT NULL
// RETURN s.name, dep.name, r.conditionWhen, r.conditionEnforcement;

// Calculate ethical compliance coverage
// MATCH (s:Service)
// OPTIONAL MATCH (s)-[:COMPLIES_WITH]->(e:EthicalConstraint)
// RETURN s.name, count(e) as compliance_count
// ORDER BY compliance_count DESC;

// Find services with social impact metrics
// MATCH (s:Service)-[:HAS_IMPACT]->(si:SocialImpact)
// RETURN s.name, si.description, si.metrics;

// ----------------------------------------------------------------------------
// SCHEMA VALIDATION QUERIES
// ----------------------------------------------------------------------------

// Check for services without ethical constraints (should be none)
// MATCH (s:Service)
// WHERE NOT (s)-[:COMPLIES_WITH]->(:EthicalConstraint)
// RETURN s.name, s.domainContext;

// Check for broken dependency links (targetUri doesn't exist)
// MATCH (s:Service)-[r:DEPENDS_ON]->(target:Service)
// WHERE NOT exists(target.id)
// RETURN s.name, r.businessReason;

// Verify consent mechanism for services with PII operations
// MATCH (s:Service)-[:HAS_OPERATION]->(o:Operation)
// WHERE size(o.piiFields) > 0 AND s.consentMechanism IS NULL
// RETURN s.name, o.name, o.piiFields;

// ----------------------------------------------------------------------------
// DATA CLEANUP (Development Only)
// ----------------------------------------------------------------------------

// Delete all data (WARNING: DESTRUCTIVE!)
// MATCH (n) DETACH DELETE n;

// Delete specific service and all relationships
// MATCH (s:Service {name: 'ServiceName'})
// DETACH DELETE s;

// ----------------------------------------------------------------------------
// NOTES
// ----------------------------------------------------------------------------
//
// 1. All constraints use IF NOT EXISTS to allow idempotent execution
// 2. Indexes are created for common query patterns
// 3. This schema is designed for Neo4j 5.x Community Edition
// 4. For production, consider adding:
//    - Node key constraints for multi-property uniqueness
//    - Full-text indexes for description fields
//    - Point indexes if adding geospatial data
//    - Vector indexes if adding ML embeddings
//
// 5. Schema evolution policy:
//    - MINOR changes: Add new optional properties/relationships
//    - MAJOR changes: Remove properties or change semantics
//    - Always maintain backward compatibility within MAJOR version
//
// ============================================================================
