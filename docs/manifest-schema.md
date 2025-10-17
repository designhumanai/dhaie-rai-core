<!--
SPDX-License-Identifier: CC-BY-NC-SA-4.0
Copyright © Viktor Savitskiy, 1995–2025
-->

# DHAIE RAI Service Manifest Schema v1.0

> **Semantic Self-Description for Reflexive AI Systems**
>
> *"Systems should describe and explain themselves in human-meaningful terms."*

---

## 📖 Overview

The **DHAIE RAI Service Manifest** is the foundational contract of a Reflexive AI infrastructure. It is a machine-readable, semantically rich document that allows a service to declare not only *what* it does, but **why** it exists, **what** it means in a business context, **how** it complies with ethical and regulatory constraints, and **what relationships** it has with other services.

This document specifies the structure, semantics, and intended use of the Service Manifest Schema v1.0.

### Design Philosophy

- **Meaning Before Mechanism:** The business purpose and intent are primary; technical details are secondary.
- **Clarity Before Complexity:** The schema is designed to be understood by developers and stakeholders without a deep background in semantics.
- **Ethics Before Efficiency:** Ethical constraints and compliance are first-class citizens, not optional additions.

---

## 🎯 Core Concepts

### What is a Reflexive Service?

A Reflexive Service is a software component that can **explain its own role, dependencies, and boundaries** within a larger system. It goes beyond a technical API description to include:

- **Business Purpose:** The value it provides in the problem domain.
- **Domain Context:** Its place in the business architecture.
- **Semantic Dependencies:** The other services it relies on, and the *reason* for those dependencies.
- **Ethical Layer:** The regulations, consent mechanisms, and social impact considerations it must adhere to.
- **Operational Semantics:** What actions it performs, whether they mutate state, and what PII is involved.

### The Role of the Manifest

The Manifest acts as a **"service passport"** within the DHAIE RAI ecosystem. It is used by:

1. **Semantic Observers:** To build and maintain a live knowledge graph of the system.
2. **Drift Detectors:** To validate that a service's runtime behavior matches its declared intent.
3. **Developers & Architects:** To understand service boundaries and interactions at a semantic level.
4. **Auditors & Regulators:** To verify compliance and ethical alignment.
5. **AI Agents:** To reason about system topology and make autonomous decisions.

---

## 🗂️ Schema Fundamentals

### Format & Compliance

- **Format:** JSON-LD 1.1
- **JSON Schema:** Draft 2020-12 for validation
- **Core Vocabulary:** Hybrid `schema.org` + `dhaie:` ontology
- **RDF Compatible:** Can be converted to RDF/OWL for Neo4j knowledge graphs

### The `@context` and `@type`

The manifest is rooted in a hybrid ontology to ensure both external compatibility and DHAIE's unique semantic needs.

```json
{
  "@context": {
    "@vocab": "https://schema.org/",
    "dhaie": "https://designhumanai.com/ontology/v1#"
  },
  "@type": "dhaie:ReflexiveServiceManifest"
}
```

- **`@vocab: "https://schema.org/"`**: Defaults common properties (like `name`, `description`) to the widely understood schema.org vocabulary.
- **`dhaie:` namespace**: Hosts DHAIE-specific concepts that are not covered by schema.org, ensuring semantic precision for reflexive AI concepts.

---

## 🗂️ Field Reference

*Detailed specification of each field in the DHAIE RAI Service Manifest. This section is normative and serves as the primary source for developers and validators.*

**Terminology Note:** Throughout this document, **PII** refers to **Personally Identifiable Information** as defined by relevant data protection regulations.

---

### 🆔 Top-Level Identity & Purpose

#### `@id`
- **Type:** `URI` (String, formatted as a Uniform Resource Identifier)
- **Required:** ✅ Yes
- **Description:** A globally unique and persistent identifier for this specific service manifest instance. This URI SHOULD be dereferenceable and MUST NOT change over the service's lifecycle. It is used to uniquely identify the service node in the RDF knowledge graph.
- **Format:** MUST start with `https://` and follow a stable, organizational URI pattern.
- **Best Practice:** Use versioned paths (e.g., `/v2/manifest`) to enable schema evolution.
- **Example:**
  ```json
  "@id": "https://api.example.com/services/payment-engine/v2/manifest"
  ```

---

#### `name`
- **Type:** `String` (schema.org/Text)
- **Required:** ✅ Yes
- **Description:** The human-readable name of the service. This should be a simple, recognizable name used in communications and dashboards.
- **Constraints:** 
  - Min 3, max 100 characters
  - MUST match regex: `^[a-zA-Z0-9][ a-zA-Z0-9-]{0,98}[a-zA-Z0-9]$`
  - (letters, numbers, spaces, hyphens only; no leading/trailing whitespace)
- **Example:**
  ```json
  "name": "Cross-Border Payment Engine"
  ```

---

#### `version`
- **Type:** `String` (schema.org/Text)
- **Required:** ✅ Yes
- **Description:** The version of the service software implementation itself. Follows semantic versioning (MAJOR.MINOR.PATCH).
- **Format:** Semantic Versioning 2.0.0 (e.g., `2.5.1`, `1.0.0-beta.3`)
- **Pattern:** `^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$`
- **Example:**
  ```json
  "version": "2.5.1"
  ```

---

#### `dhaie:manifestVersion`
- **Type:** `String`
- **Required:** ✅ Yes
- **Description:** The version of the DHAIE Service Manifest schema this document complies with. This allows for schema evolution and runtime validation against the correct specification.
- **Format:** Fixed string for this specification: `"1.0"`
- **Example:**
  ```json
  "dhaie:manifestVersion": "1.0"
  ```

---

#### `description`
- **Type:** `String` (schema.org/Text)
- **Required:** ✅ Yes
- **Description:** A clear, concise, and technical summary of *what* the service does functionally. This complements the `dhaie:businessPurpose` which describes the *why*.
- **Constraints:** Min 10, max 500 characters. 1-3 sentences recommended.
- **Example:**
  ```json
  "description": "Processes and settles international fiat currency transactions between financial institutions using SWIFT and SEPA protocols."
  ```

---

#### `dhaie:businessPurpose`
- **Type:** `String` (schema.org/Text)
- **Required:** ✅ Yes
- **Description:** A foundational field for reflexivity. A statement explaining the *raison d'être* of the service—the business value it provides and the problem it solves in the domain.
- **Philosophy:** Answers "Why would a business pay for this to exist?" and "What human need does this serve?"
- **Constraints:** Min 20, max 700 characters. Should be a concise value proposition.
- **Example:**
  ```json
  "dhaie:businessPurpose": "To enable fast, secure, and cost-effective cross-border monetary transfers for migrant workers, thereby promoting financial inclusion and reducing economic friction in underserved markets."
  ```

---

#### `dhaie:domainContext`
- **Type:** `String`
- **Required:** ✅ Yes
- **Description:** A dot-separated path that locates the service within the business architecture and domain ontology. It provides semantic context for discovery and relationship mapping.
- **Format:** 
  - MUST match regex: `^[a-zA-Z][a-zA-Z0-9]*(?:\.[a-zA-Z][a-zA-Z0-9]*){2,}$`
  - Minimum 3 levels (e.g., `Domain.Subdomain.Capability`)
  - Letters and numbers only; no whitespace
- **Best Practice:** Define a controlled vocabulary within your organization. Common top-level domains: `FinTech`, `Healthcare`, `Ecommerce`, `Manufacturing`, `Education`.
- **Examples:**
  ```json
  "dhaie:domainContext": "FinTech.Payments.International"
  "dhaie:domainContext": "Healthcare.PatientEngagement.Portal"
  "dhaie:domainContext": "Ecommerce.Fulfillment.Shipping"
  ```

---

### ⚙️ Operational & Technical Context

#### `provider`
- **Type:** `Object` (schema.org/Organization)
- **Required:** ✅ Yes
- **Description:** The entity (team, company, department) responsible for developing, maintaining, and operating this service.
- **Fields:**
  - `name` (String, Required): The name of the providing organization. Min 2, max 200 characters.
  - `url` (URI, Optional): A link to the provider's homepage or information page.
- **Example:**
  ```json
  "provider": {
    "name": "Example FinTech Corp - Payments Division",
    "url": "https://www.example.com/payments"
  }
  ```

---

#### `dhaie:operations`
- **Type:** `Array` of `Object`
- **Required:** ❌ No
- **Description:** A list of the primary actions, capabilities, or operations the service exposes. This describes *what* the service can do at a functional level, enriched with semantic metadata about state changes, PII handling, and audit requirements.
- **Object Fields:**
  - `name` (String, Required): A unique, machine-readable identifier for the operation.
    - MUST match regex: `^[a-z][a-zA-Z0-9]{2,49}$` (camelCase, 3-50 chars)
  - `description` (String, Required): A human-readable explanation of the operation. Min 10, max 300 characters.
  - `category` (String, Optional): A high-level grouping.
    - Allowed values: `financial`, `dataQuery`, `dataMutation`, `admin`, `compute`, `orchestration`, `notification`, `authentication`
  - `mutates` (Boolean, Optional): Whether this operation changes system state (creates, updates, deletes data).
  - `piiFields` (Array of String, Optional): List of PII field names involved in this operation. Each must match `^[a-zA-Z][a-zA-Z0-9_]*$`. Must be unique.
  - `auditRequired` (Boolean, Optional): Whether this operation requires audit logging for compliance purposes.
- **Example:**
  ```json
  "dhaie:operations": [
    {
      "name": "fundsTransfer",
      "description": "Initiates a transfer of funds between two specified accounts with fraud detection.",
      "category": "financial",
      "mutates": true,
      "piiFields": ["accountNumber", "recipientName", "senderName"],
      "auditRequired": true
    },
    {
      "name": "getTransactionHistory",
      "description": "Retrieves paginated transaction history for a given account.",
      "category": "dataQuery",
      "mutates": false,
      "piiFields": ["accountNumber"],
      "auditRequired": false
    }
  ]
  ```

---

### 🛡️ The Ethical Layer

#### `dhaie:ethicalConstraints`
- **Type:** `Array` of `Object`
- **Required:** ✅ Yes (minimum 1 entry)
- **Description:** A structured declaration of the ethical, legal, and regulatory frameworks that govern the service's operation. This is a core tenet of the DHAIE Reflexive AI principle, making constraints explicit and machine-readable.
- **Object Fields:**
  - `regulation` (String, Required): The common name of the regulation or standard. Min 2, max 50 characters.
  - `uri` (URI, Optional but strongly recommended): A direct link to the official text or authoritative definition of the constraint.
  - `articles` (Array of String, Optional): Specific articles, sections, or rules within the regulation that are relevant. Each must match pattern `^[A-Z][a-zA-Z]+ \d+.*$` (e.g., "Article 6", "Section 1234"). Omit if not applicable. Must be unique.
  - `implementation` (String, Required): A brief, human-readable description of how the service implements this constraint. Min 10, max 500 characters.
  - `verificationMethod` (Object, Optional): Machine-actionable compliance verification.
    - `type` (String, Required): Enum: `automated_scan`, `manual_audit`, `third_party_certification`, `continuous_monitoring`
    - `tool` (String, Optional): Name of verification tool (e.g., "OpenPolicyAgent", "Vanta"). Max 100 characters.
    - `policyUri` (URI, Optional): Link to the policy/rule definition.
    - `lastVerified` (String, Optional): ISO 8601 date of last verification (format: `YYYY-MM-DD`).
- **Example:**
  ```json
  "dhaie:ethicalConstraints": [
    {
      "regulation": "GDPR",
      "uri": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679",
      "articles": ["Article 6(1)(a)", "Article 7", "Article 17"],
      "implementation": "Explicit user consent is obtained and logged before processing any PII. Right to erasure is implemented via data deletion API.",
      "verificationMethod": {
        "type": "automated_scan",
        "tool": "OneTrust Privacy Automation",
        "policyUri": "https://policies.example.com/gdpr-compliance.rego",
        "lastVerified": "2025-10-01"
      }
    },
    {
      "regulation": "AML (Anti-Money Laundering)",
      "uri": "https://www.fatf-gafi.org/",
      "implementation": "All transactions >$10k trigger mandatory risk assessment and are reported to FinCEN within 24 hours."
    }
  ]
  ```

---

#### `dhaie:consentMechanism`
- **Type:** `String`
- **Required:** ⚠️ Conditional
  - Required if ANY of the following is true:
    - Service processes PII (declared in `dhaie:operations[].piiFields`)
    - Any `dhaie:semanticDependencies` entry has `consentImplications` field
  - Otherwise, should be set to `"no_pii_processed"`
- **Description:** Defines the primary mechanism by which user consent is obtained for data processing activities.
- **Allowed Values (Controlled Vocabulary):**
  - `explicit_consent_required`: Consent must be explicitly granted by the user via a clear affirmative action (checkbox, signature, etc.).
  - `implied_consent`: Consent is inferred from user actions and context (e.g., proceeding with a transaction).
  - `no_pii_processed`: The service does not handle any PII, thus consent is not applicable.
  - `consent_managed_externally`: Consent is handled by a dedicated upstream service (e.g., a Consent Management Platform).
- **Validation Rule:** If `consentMechanism` is `"no_pii_processed"`, then `dhaie:operations[].piiFields` MUST NOT be present in any operation.
- **Example:**
  ```json
  "dhaie:consentMechanism": "explicit_consent_required"
  ```

---

#### `dhaie:socialImpact`
- **Type:** `Object`
- **Required:** ❌ No (but strongly encouraged for services with societal implications)
- **Description:** Qualitative or quantitative metrics that describe the service's intended positive contribution to society or its alignment with DHAIE's cognitive equity principles.
- **Object Fields:**
  - `metrics` (Array of Object, Optional): Structured, measurable social impact indicators.
    - `name` (String, Required): Standardized metric name from DHAIE taxonomy.
      - Allowed values: `financial_inclusion_index`, `cross_border_cost_reduction`, `carbon_footprint_reduction`, `accessibility_improvement`, `cognitive_equity_score`, `digital_divide_reduction`, `healthcare_access_improvement`, `education_accessibility`
    - `value` (Number, Required): The measured value.
    - `baseline` (Number, Optional): Baseline value for comparison (what it was before this service).
    - `unit` (String, Optional): Unit of measurement (e.g., "percentage", "index", "USD saved"). Max 50 characters.
    - `measurementMethod` (String, Optional): How this metric is measured/calculated. Max 200 characters.
  - `description` (String, Required): A narrative description of the social impact. Min 20, max 700 characters.
- **Important:** The `metrics` array MUST contain objects with `name` and `value` fields, NOT simple strings. The old format `"metrics": ["financial_inclusion_index"]` is deprecated and will fail validation.
- **Example:**
  ```json
  "dhaie:socialImpact": {
    "metrics": [
      {
        "name": "financial_inclusion_index",
        "value": 0.73,
        "baseline": 0.45,
        "unit": "index (0-1 scale)",
        "measurementMethod": "World Bank Financial Inclusion Index methodology"
      },
      {
        "name": "cross_border_cost_reduction",
        "value": 54.2,
        "baseline": 100.0,
        "unit": "percentage",
        "measurementMethod": "Average remittance cost vs traditional wire transfer"
      }
    ],
    "description": "Reduces the average cost of remittances for migrant workers by over 50%, enabling more capital to reach families in developing economies and contributing to poverty reduction."
  }
  ```

---

### 🔗 Semantic Dependencies

#### `dhaie:semanticDependencies`
- **Type:** `Array` of `Object`
- **Required:** ❌ No
- **Description:** Declares other services that this service relies upon to fulfill its purpose, enriching the basic "dependency" with the *semantic reason* for that dependency. This is crucial for the Semantic Observer to build an accurate knowledge graph and for Drift Detector to validate behavioral consistency.
- **Object Fields:**
  - `target` (String, Required): The `name` of the dependent-upon service. Min 3, max 100 characters.
  - `targetUri` (URI, Optional but strongly recommended): The `@id` of the dependent-upon service's manifest for explicit semantic linking. MUST start with `https://`. Omit if not available.
  - `relationship` (String, Required): The nature of the dependency from the DHAIE Relationship Taxonomy (see below).
  - `businessReason` (String, Required): A clear explanation of *why* this dependency exists. Min 10, max 500 characters.
  - `consentImplications` (String, Optional): Describes what data is shared with the dependency and implications for user consent. Min 10, max 300 characters. Omit if no data sharing occurs.
  - `condition` (Object, Optional): Defines when this dependency is activated (conditional dependency).
    - `when` (String, Required): Condition expression in pseudo-code or natural language. Max 200 characters.
    - `enforcementLevel` (String, Required): Enum: `mandatory`, `recommended`, `optional`

---

### 📚 DHAIE Relationship Taxonomy

**Category: Data Flow**
- `data.provider.primary` — *This dependency is the authoritative source of data*
  - Example: "Customer profile data comes from the CRM service"
- `data.provider.cache` — *This dependency provides cached/replicated data*
  - Example: "Uses cached product catalog from the CDN service"
- `data.provider.realtime` — *This dependency streams real-time data*
  - Example: "Consumes real-time market prices from the ticker service"
- `data.consumer.analytics` — *This dependency consumes our data for analytics*
  - Example: "Transaction data is sent to the BI warehouse"
- `data.consumer.backup` — *This dependency stores backup copies of our data*
  - Example: "Daily snapshots are sent to the archive service"
- `data.consumer.export` — *This dependency receives data for external export*
  - Example: "Sends financial reports to the regulatory filing service"

**Category: Risk & Compliance**
- `risk.assessment.required` — *Mandatory risk evaluation before proceeding*
  - Example: "Fraud check is required for all transactions"
- `risk.assessment.optional` — *Optional risk scoring for optimization*
  - Example: "Credit score check for premium tier users"
- `compliance.verification.mandatory` — *Required compliance check*
  - Example: "AML screening is legally required for cross-border payments"
- `compliance.verification.optional` — *Optional compliance enhancement*
  - Example: "Enhanced due diligence for high-value customers"

**Category: Orchestration**
- `orchestration.trigger` — *This service initiates a workflow in the dependency*
  - Example: "Triggers the order fulfillment workflow after payment confirmation"
- `orchestration.coordinate` — *This service coordinates with the dependency in a saga/choreography*
  - Example: "Coordinates inventory reservation with the warehouse service"

**Category: Computation**
- `computation.specialized` — *Offloads specialized computation*
  - Example: "Offloads ML inference to the recommendation engine"
- `computation.offload` — *Offloads general heavy computation*
  - Example: "Offloads PDF generation to the document service"

**Category: Notifications**
- `notification.trigger` — *Triggers a notification to be sent*
  - Example: "Sends payment confirmation email via the notification service"
- `notification.subscribe` — *Subscribes to notifications from the dependency*
  - Example: "Receives alerts when inventory is low"

**Category: Authentication & Authorization**
- `auth.delegation` — *Delegates authentication to this service*
  - Example: "Uses SSO via the identity provider service"
- `auth.verification` — *Verifies authentication tokens/credentials*
  - Example: "Validates JWT tokens against the auth service"

**Category: Ledger & Audit**
- `ledger.append_only` — *Writes immutable audit logs*
  - Example: "Appends transaction records to the blockchain ledger"
- `ledger.query` — *Queries historical audit data*
  - Example: "Retrieves audit trail from the compliance database"

---

### 🔗 Semantic Dependencies: Complete Example

```json
"dhaie:semanticDependencies": [
  {
    "target": "FraudDetector",
    "targetUri": "https://api.example.com/services/fraud-detector/v1/manifest",
    "relationship": "risk.assessment.required",
    "businessReason": "AML regulation requires risk scoring for all transactions exceeding $10,000 USD to comply with FinCEN reporting requirements.",
    "consentImplications": "Shares transaction amount, sender/recipient account numbers, and geolocation data for risk analysis.",
    "condition": {
      "when": "transaction.amount.usd > 10000",
      "enforcementLevel": "mandatory"
    }
  },
  {
    "target": "LedgerService",
    "targetUri": "https://api.example.com/services/ledger/v2/manifest",
    "relationship": "ledger.append_only",
    "businessReason": "All financial transactions must be recorded in an immutable audit log for regulatory compliance and dispute resolution.",
    "consentImplications": "No PII shared; only transaction IDs and timestamps."
  },
  {
    "target": "NotificationService",
    "targetUri": "https://api.example.com/services/notifications/v1/manifest",
    "relationship": "notification.trigger",
    "businessReason": "Users must receive real-time confirmation of payment status for transparency and fraud prevention.",
    "consentImplications": "Shares recipient email/phone and transaction summary."
  },
  {
    "target": "IdentityProvider",
    "targetUri": "https://api.example.com/services/idp/v3/manifest",
    "relationship": "auth.delegation",
    "businessReason": "Centralizes authentication and SSO for all internal services to reduce attack surface.",
    "consentImplications": "Shares user ID and session context; no password data."
  }
]
```

---

## 🧪 Validation & Testing

### JSON Schema Validation

All manifests MUST validate against the official JSON Schema file: `schema/service-manifest.schema.json`

**Using AJV (Node.js):**
```bash
npm install -g ajv-cli ajv-formats
ajv validate -s schema/service-manifest.schema.json \
             -d examples/payment-service.manifest.json \
             --strict=true
```

**Using Python (jsonschema):**
```python
import json
from jsonschema import validate, ValidationError

with open('schema/service-manifest.schema.json') as f:
    schema = json.load(f)

with open('examples/payment-service.manifest.json') as f:
    manifest = json.load(f)

try:
    validate(instance=manifest, schema=schema)
    print("✅ Manifest is valid!")
except ValidationError as e:
    print(f"❌ Validation error: {e.message}")
```

---

### Semantic Coherence Checks

Beyond syntactic validation, perform these semantic checks:

#### 1. **Dependency Existence**
All `semanticDependencies[].target` services must have resolvable manifests.
```bash
# Pseudo-code check
for dep in manifest.semanticDependencies:
    assert can_fetch(dep.targetUri), f"{dep.target} manifest not found"
```

#### 2. **Consent Alignment**
If ANY dependency has `consentImplications`, the parent service MUST declare `consentMechanism`.
```python
has_consent_implications = any(
    'consentImplications' in dep 
    for dep in manifest.get('dhaie:semanticDependencies', [])
)
if has_consent_implications:
    assert 'dhaie:consentMechanism' in manifest
```

#### 3. **Domain Hierarchy Validation**
The `domainContext` must match your organizational taxonomy.
```bash
# Example: Validate against controlled vocabulary
allowed_domains = ["FinTech", "Healthcare", "Ecommerce", "Manufacturing"]
top_level = manifest["dhaie:domainContext"].split(".")[0]
assert top_level in allowed_domains
```

#### 4. **PII Declaration Consistency**
If `operations[].piiFields` is present, `consentMechanism` MUST NOT be `"no_pii_processed"`.
```python
has_pii = any(
    op.get('piiFields') 
    for op in manifest.get('dhaie:operations', [])
)
if has_pii:
    assert manifest['dhaie:consentMechanism'] != 'no_pii_processed'
```

#### 5. **Social Impact Metrics Structure**
If `socialImpact.metrics` is present, each entry MUST be an object with `name` and `value` fields.
```python
if 'dhaie:socialImpact' in manifest:
    metrics = manifest['dhaie:socialImpact'].get('metrics', [])
    for metric in metrics:
        assert isinstance(metric, dict), "Metrics must be objects, not strings"
        assert 'name' in metric and 'value' in metric, "Each metric needs name and value"
```

---

## 🗺️ Neo4j Knowledge Graph Integration

### RDF Conversion

The manifest's JSON-LD structure can be directly ingested into Neo4j using APOC procedures or converted to RDF triples.

**Example RDF Triples:**
```turtle
@prefix dhaie: <https://designhumanai.com/ontology/v1#> .
@prefix schema: <https://schema.org/> .

<https://api.example.com/services/payment-engine/v2/manifest>
    a dhaie:ReflexiveServiceManifest ;
    schema:name "Cross-Border Payment Engine" ;
    dhaie:businessPurpose "Enable secure cross-border transfers..." ;
    dhaie:domainContext "FinTech.Payments.International" ;
    dhaie:dependsOn <https://api.example.com/services/fraud-detector/v1/manifest> .
```

---

### Cypher Query Examples

**Find all services in FinTech domain with GDPR constraints:**
```cypher
MATCH (s:Service {domainContext: "FinTech.Payments.International"})
-[:COMPLIES_WITH]->(c:EthicalConstraint {regulation: "GDPR"})
RETURN s.name, s.businessPurpose, c.implementation
```

**Discover dependency chains (who depends on FraudDetector?):**
```cypher
MATCH (s:Service)-[r:DEPENDS_ON]->(target:Service {name: "FraudDetector"})
RETURN s.name, r.relationship, r.businessReason
ORDER BY s.name
```

**Find services with conditional dependencies:**
```cypher
MATCH (s:Service)-[r:DEPENDS_ON]->(target:Service)
WHERE r.condition IS NOT NULL
RETURN s.name, target.name, r.condition.when, r.condition.enforcementLevel
```

**Identify services with high social impact:**
```cypher
MATCH (s:Service)
WHERE s.socialImpact IS NOT NULL 
  AND size(s.socialImpact.metrics) > 0
RETURN s.name, 
       s.socialImpact.description,
       [m IN s.socialImpact.metrics | m.name] AS metrics
ORDER BY size(s.socialImpact.metrics) DESC
```

---

## 🔄 Schema Evolution Policy

The DHAIE Manifest Schema follows **Semantic Versioning 2.0.0**:

### Version Number Format: `MAJOR.MINOR.PATCH`

- **MAJOR** (1.x → 2.x): Breaking changes
  - Removing required fields
  - Changing field types or formats
  - Removing enum values from controlled vocabularies
  - Changing validation rules that would invalidate existing manifests
  - **Migration Required:** Services must update manifests to comply

- **MINOR** (1.0 → 1.1): Backward-compatible additions
  - Adding new optional fields
  - Adding new enum values to controlled vocabularies
  - Relaxing validation constraints
  - **No Migration Required:** Existing manifests remain valid

- **PATCH** (1.0.0 → 1.0.1): Non-functional changes
  - Documentation clarifications
  - Example corrections
  - Schema metadata updates (descriptions, titles)
  - **No Impact:** No changes to validation behavior

### Validator Requirements

- Validators MUST accept manifests with the same MAJOR version.
- Validators SHOULD warn (not error) on unknown optional fields to support forward compatibility.
- Validators MUST reject manifests with unsupported MAJOR versions.

### Deprecation Policy

- Fields/values will be marked as deprecated for at least 1 MINOR version before removal.
- Deprecated fields will be documented in `CHANGELOG.md` with migration guidance.
- Removal of deprecated fields triggers a MAJOR version bump.

---

## 💻 Implementation Guidelines

### For Developers Creating Manifests

#### 1. **Start with Business Purpose**
Don't start with technical details. First articulate:
- Why does this service exist?
- What business problem does it solve?
- Who benefits from it?

#### 2. **Be Explicit About Ethics**
- Every service MUST declare at least one ethical constraint.
- If you handle PII, declare it in `operations[].piiFields` and specify `consentMechanism`.
- When in doubt, over-communicate compliance measures.

#### 3. **Rich Dependency Semantics**
- Don't just list dependencies—explain WHY they exist.
- Use the DHAIE Relationship Taxonomy consistently.
- If data is shared, always declare `consentImplications`.

#### 4. **Conditional Dependencies Are Powerful**
Use the `condition` field to model business rules:
```json
{
  "target": "PremiumFeaturesService",
  "relationship": "data.provider.primary",
  "businessReason": "Premium users get access to advanced analytics.",
  "condition": {
    "when": "user.tier == 'premium'",
    "enforcementLevel": "optional"
  }
}
```

#### 5. **Omit Empty Optional Fields**
- Do NOT include optional fields with `null`, `[]`, or `{}` values.
- If you don't have `socialImpact` metrics yet, omit the entire field.
- Clean manifests are easier to read and validate.

#### 6. **Use Stable URIs**
- `@id` and `targetUri` MUST be persistent and versioned.
- Bad: `https://staging.example.com/temp/service123`
- Good: `https://api.example.com/services/payment-engine/v2/manifest`

---

### For Organizations Adopting DHAIE RAI

#### 1. **Define Your Domain Taxonomy**
Before writing manifests, establish:
```yaml
FinTech:
  Payments:
    - Domestic
    - International
    - Cryptocurrency
  RiskManagement:
    - Fraud
    - Compliance
    - CreditScoring
```

#### 2. **Create a Relationship Taxonomy Guide**
Document when to use each relationship type:
```markdown
| Relationship | Use When | Example |
|--------------|----------|---------|
| data.provider.primary | Service is authoritative source | CRM → Customer data |
| risk.assessment.required | Legal/regulatory mandate | AML screening |
| orchestration.trigger | Initiates async workflow | Order → Fulfillment |
```

#### 3. **Establish Ethical Constraint Standards**
Define org-wide constraints:
```json
{
  "standardConstraints": {
    "gdpr": {
      "regulation": "GDPR",
      "uri": "https://eur-lex.europa.eu/...",
      "articles": ["Article 6(1)(a)", "Article 7"]
    },
    "hipaa": {
      "regulation": "HIPAA",
      "uri": "https://www.hhs.gov/hipaa/..."
    }
  }
}
```

#### 4. **Automate Validation in CI/CD**
```yaml
# .github/workflows/validate-manifests.yml
name: Validate Service Manifests
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Validate JSON Schema
        run: |
          npm install -g ajv-cli
          ajv validate -s schema/service-manifest.schema.json \
                       -d "manifests/*.json"
      - name: Semantic Coherence Check
        run: python scripts/validate-semantic-coherence.py
```

---

## 🎯 Best Practices & Anti-Patterns

### ✅ Best Practices

#### **1. Business Language Over Technical Jargon**
```json
// ❌ Bad
"dhaie:businessPurpose": "REST API for CRUD operations on payment entities"

// ✅ Good
"dhaie:businessPurpose": "Enable customers to send money internationally with real-time tracking and transparent fees"
```

#### **2. Explicit Over Implicit**
```json
// ❌ Bad (implicit consent)
"dhaie:consentMechanism": "implied_consent"

// ✅ Good (explicit when handling PII)
"dhaie:consentMechanism": "explicit_consent_required"
```

#### **3. Measurable Social Impact**
```json
// ❌ Bad (vague, no metrics)
"dhaie:socialImpact": {
  "description": "Helps people save money"
}

// ❌ Bad (old format - metrics as strings)
"dhaie:socialImpact": {
  "metrics": ["financial_inclusion_index"],  // Wrong: array of strings
  "description": "Improves financial inclusion"
}

// ✅ Good (structured metrics with measurable values)
"dhaie:socialImpact": {
  "metrics": [
    {
      "name": "cross_border_cost_reduction",
      "value": 54.2,
      "baseline": 100.0,
      "unit": "percentage",
      "measurementMethod": "Average cost vs traditional wire transfer"
    }
  ],
  "description": "Reduces remittance costs by 54%, saving migrant workers $2.1B annually"
}
```

#### **4. Conditional Dependencies with Business Context**
```json
// ❌ Bad (technical only)
"condition": {
  "when": "amount > 10000",
  "enforcementLevel": "mandatory"
}

// ✅ Good (business context)
"condition": {
  "when": "transaction.amount.usd > 10000",
  "enforcementLevel": "mandatory"
},
"businessReason": "FinCEN Bank Secrecy Act requires enhanced due diligence for transactions exceeding $10,000"
```

---

### ❌ Anti-Patterns to Avoid

#### **1. Placeholder Text**
```json
// ❌ NEVER DO THIS
"description": "TODO: Add description later"
"dhaie:businessPurpose": "TBD"
```

#### **2. Empty Optional Fields**
```json
// ❌ Bad
"dhaie:operations": []
"dhaie:socialImpact": {
  "metrics": [],
  "description": ""
}

// ✅ Good (omit entirely)
// Just don't include the field
```

#### **3. Generic Relationship Types**
```json
// ❌ Bad (no semantic value)
"relationship": "uses"
"relationship": "depends_on"

// ✅ Good (specific taxonomy term)
"relationship": "risk.assessment.required"
"relationship": "data.provider.cache"
```

#### **4. Inconsistent Naming**
```json
// ❌ Bad (mixing conventions)
"name": "payment_service"
"operations": [
  {"name": "FundsTransfer"},
  {"name": "get-balance"}
]

// ✅ Good (consistent camelCase)
"name": "Payment Service"
"operations": [
  {"name": "fundsTransfer"},
  {"name": "getBalance"}
]
```

#### **5. Unstable URIs**
```json
// ❌ Bad (will break)
"@id": "http://localhost:3000/manifest"
"@id": "https://dev-env-42.example.com/services/temp"

// ✅ Good (stable, versioned)
"@id": "https://api.example.com/services/payment-engine/v2/manifest"
```

---

## 📚 Domain-Specific Examples

### Example 1: FinTech Payment Service
```json
{
  "@context": {
    "@vocab": "https://schema.org/",
    "dhaie": "https://designhumanai.com/ontology/v1#"
  },
  "@type": "dhaie:ReflexiveServiceManifest",
  "@id": "https://api.example.com/services/payment-engine/v2/manifest",
  "name": "Cross-Border Payment Engine",
  "version": "2.5.1",
  "dhaie:manifestVersion": "1.0",
  "description": "Processes international fiat currency transactions using SWIFT and SEPA protocols with real-time fraud detection.",
  "dhaie:businessPurpose": "Enable fast, secure, and cost-effective cross-border monetary transfers for migrant workers, reducing economic friction and promoting financial inclusion in underserved markets.",
  "dhaie:domainContext": "FinTech.Payments.International",
  "provider": {
    "name": "Example FinTech Corp",
    "url": "https://www.example.com"
  },
  "dhaie:ethicalConstraints": [
    {
      "regulation": "GDPR",
      "uri": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679",
      "articles": ["Article 6(1)(a)", "Article 7"],
      "implementation": "Explicit user consent obtained before processing. Right to erasure implemented via DELETE /users/{id}/data endpoint.",
      "verificationMethod": {
        "type": "automated_scan",
        "tool": "OneTrust Privacy Automation",
        "lastVerified": "2025-10-01"
      }
    },
    {
      "regulation": "AML",
      "uri": "https://www.fincen.gov/resources/statutes-regulations",
      "implementation": "Transactions >$10k trigger mandatory risk assessment and FinCEN reporting within 24h."
    }
  ],
  "dhaie:consentMechanism": "explicit_consent_required",
  "dhaie:consentMechanism": "explicit_consent_required",
  "dhaie:socialImpact": {
    "metrics": [
      {
        "name": "financial_inclusion_index",
        "value": 0.73,
        "baseline": 0.45,
        "unit": "index",
        "measurementMethod": "World Bank Financial Inclusion Index"
      }
    ],
    "description": "Reduces average remittance cost by 54%, saving migrant workers $2.1B annually."
  },
  "dhaie:operations": [
    {
      "name": "fundsTransfer",
      "description": "Initiates international money transfer with fraud detection and compliance checks.",
      "category": "financial",
      "mutates": true,
      "piiFields": ["accountNumber", "recipientName", "senderName"],
      "auditRequired": true
    }
  ],
  "dhaie:semanticDependencies": [
    {
      "target": "FraudDetector",
      "targetUri": "https://api.example.com/services/fraud-detector/v1/manifest",
      "relationship": "risk.assessment.required",
      "businessReason": "AML regulation requires risk scoring for transactions >$10k.",
      "consentImplications": "Shares transaction amount, geolocation, and account metadata.",
      "condition": {
        "when": "transaction.amount.usd > 10000",
        "enforcementLevel": "mandatory"
      }
    }
  ]
}
```

---

### Example 2: Healthcare Patient Portal
```json
{
  "@context": {
    "@vocab": "https://schema.org/",
    "dhaie": "https://designhumanai.com/ontology/v1#"
  },
  "@type": "dhaie:ReflexiveServiceManifest",
  "@id": "https://api.healthsys.example.com/services/patient-portal/v1/manifest",
  "name": "Patient Portal",
  "version": "1.3.0",
  "dhaie:manifestVersion": "1.0",
  "description": "Secure web and mobile interface for patients to access medical records, schedule appointments, and communicate with providers.",
  "dhaie:businessPurpose": "Empower patients with direct access to their health information, improving care coordination and reducing administrative burden on clinical staff.",
  "dhaie:domainContext": "Healthcare.PatientEngagement.Portal",
  "provider": {
    "name": "HealthSys Digital Health Division",
    "url": "https://www.healthsys.example.com"
  },
  "dhaie:ethicalConstraints": [
    {
      "regulation": "HIPAA",
      "uri": "https://www.hhs.gov/hipaa/",
      "articles": ["Privacy Rule 164.502", "Security Rule 164.306"],
      "implementation": "End-to-end encryption for all PHI. Access logs maintained for 7 years. Patient consent required for third-party data sharing.",
      "verificationMethod": {
        "type": "third_party_certification",
        "tool": "HITRUST CSF Certification",
        "lastVerified": "2025-08-15"
      }
    }
  ],
  "dhaie:consentMechanism": "explicit_consent_required",
  "dhaie:socialImpact": {
    "metrics": [
      {
        "name": "healthcare_access_improvement",
        "value": 67.3,
        "baseline": 42.1,
        "unit": "percentage",
        "measurementMethod": "Patients able to access records within 24h"
      }
    ],
    "description": "Increases patient engagement by 60% and reduces appointment no-shows by 40% through automated reminders."
  },
  "dhaie:operations": [
    {
      "name": "viewMedicalRecords",
      "description": "Retrieve patient's electronic health records including diagnoses, medications, and test results.",
      "category": "dataQuery",
      "mutates": false,
      "piiFields": ["patientId", "dateOfBirth", "medicalRecordNumber"],
      "auditRequired": true
    }
  ],
  "dhaie:semanticDependencies": [
    {
      "target": "EHR System",
      "targetUri": "https://api.healthsys.example.com/services/ehr/v4/manifest",
      "relationship": "data.provider.primary",
      "businessReason": "EHR is the authoritative source for all clinical data.",
      "consentImplications": "Accesses full patient medical history including sensitive diagnoses."
    },
    {
      "target": "ConsentManager",
      "targetUri": "https://api.healthsys.example.com/services/consent/v2/manifest",
      "relationship": "compliance.verification.mandatory",
      "businessReason": "HIPAA requires explicit consent verification before any PHI access.",
      "consentImplications": "Validates patient consent status; no PHI shared."
    }
  ]
}
```

---

### Example 3: E-commerce Product Catalog
```json
{
  "@context": {
    "@vocab": "https://schema.org/",
    "dhaie": "https://designhumanai.com/ontology/v1#"
  },
  "@type": "dhaie:ReflexiveServiceManifest",
  "@id": "https://api.shop.example.com/services/product-catalog/v3/manifest",
  "name": "Product Catalog Service",
  "version": "3.2.0",
  "dhaie:manifestVersion": "1.0",
  "description": "Manages product inventory, pricing, availability, and search indexing for the e-commerce platform.",
  "dhaie:businessPurpose": "Provide fast, accurate, and personalized product discovery to customers, increasing conversion rates and reducing cart abandonment.",
  "dhaie:domainContext": "Ecommerce.Catalog.Management",
  "provider": {
    "name": "ShopCo Engineering",
    "url": "https://www.shop.example.com"
  },
  "dhaie:ethicalConstraints": [
    {
      "regulation": "Accessibility Standards (WCAG 2.1 AA)",
      "uri": "https://www.w3.org/WAI/WCAG21/quickref/",
      "implementation": "All product images have alt text. Search supports screen readers. Color contrast ratios meet AA standards."
    },
    {
      "regulation": "Consumer Protection (FTC)",
      "uri": "https://www.ftc.gov/legal-library",
      "implementation": "Pricing displayed clearly with no hidden fees. Out-of-stock items marked prominently."
    }
  ],
  "dhaie:consentMechanism": "no_pii_processed",
  "dhaie:socialImpact": {
    "metrics": [
      {
        "name": "accessibility_improvement",
        "value": 95.2,
        "baseline": 67.8,
        "unit": "percentage",
        "measurementMethod": "WCAG 2.1 AA compliance score via automated testing"
      }
    ],
    "description": "Achieves 95% WCAG compliance, enabling visually impaired users to independently browse and purchase products."
  },
  "dhaie:operations": [
    {
      "name": "searchProducts",
      "description": "Full-text search with filters for category, price, rating, and availability.",
      "category": "dataQuery",
      "mutates": false,
      "auditRequired": false
    },
    {
      "name": "updateInventory",
      "description": "Updates product stock levels and availability status.",
      "category": "dataMutation",
      "mutates": true,
      "auditRequired": true
    }
  ],
  "dhaie:semanticDependencies": [
    {
      "target": "RecommendationEngine",
      "targetUri": "https://api.shop.example.com/services/recommendations/v2/manifest",
      "relationship": "computation.specialized",
      "businessReason": "ML-powered personalized recommendations increase conversion by 30%.",
      "consentImplications": "Shares anonymized browsing history; no PII."
    },
    {
      "target": "PricingService",
      "targetUri": "https://api.shop.example.com/services/pricing/v1/manifest",
      "relationship": "data.provider.realtime",
      "businessReason": "Dynamic pricing adjusts based on demand, competitor prices, and promotions.",
      "consentImplications": "No data sharing; read-only access to pricing data."
    }
  ]
}
```

---

## 🔬 Advanced Topics

### Handling Multi-Tenancy

For services operating in multi-tenant architectures:

```json
"dhaie:businessPurpose": "...",
"dhaie:deploymentModel": {
  "type": "multi_tenant",
  "tenantIsolation": "database_per_tenant",
  "tenantIdentification": "subdomain"
},
"dhaie:ethicalConstraints": [
  {
    "regulation": "Data Residency (GDPR)",
    "implementation": "EU customer data stored exclusively in EU data centers. Tenant data never co-mingled."
  }
]
```

### Handling Deprecated Operations

When phasing out functionality:

```json
"dhaie:operations": [
  {
    "name": "legacyFundsTransfer",
    "description": "DEPRECATED: Use fundsTransferV2. Removal planned for v3.0.0.",
    "category": "financial",
    "deprecated": true,
    "replacedBy": "fundsTransferV2",
    "sunsetDate": "2026-06-01"
  }
]
```

### Machine Learning Ethics

For services using ML models:

```json
"dhaie:ethicalConstraints": [
  {
    "regulation": "Algorithmic Fairness",
    "implementation": "Fraud detection model tested for bias across demographic groups. Disparate impact ratio <1.2 for all protected classes.",
    "verificationMethod": {
      "type": "continuous_monitoring",
      "tool": "Fairlearn Bias Auditor",
      "policyUri": "https://policies.example.com/ml-fairness.md"
    }
  }
]
```

---

## 🆘 Troubleshooting

### Common Validation Errors

#### Error: `"@id must start with https://"`
**Solution:** Use stable HTTPS URIs.
```json
// ❌ Bad
"@id": "http://example.com/manifest"

// ✅ Good
"@id": "https://api.example.com/services/payment-engine/v2/manifest"
```

#### Error: `"consentMechanism required when piiFields present"`
**Solution:** Declare consent mechanism if handling PII.
```json
"dhaie:operations": [
  {
    "name": "getUserProfile",
    "piiFields": ["email", "phoneNumber"]
  }
],
"dhaie:consentMechanism": "explicit_consent_required"
```

#### Error: `"domainContext must have at least 3 levels"`
**Solution:** Use minimum 3-level hierarchy.
```json
// ❌ Bad
"dhaie:domainContext": "FinTech.Payments"

// ✅ Good
"dhaie:domainContext": "FinTech.Payments.International"
```

#### Error: `"socialImpact metrics must be objects, not strings"`
**Solution:** Use structured metric objects with `name`, `value`, and optional fields.
```json
// ❌ Bad (old format)
"dhaie:socialImpact": {
  "metrics": ["financial_inclusion_index"]
}

// ✅ Good (structured format)
"dhaie:socialImpact": {
  "metrics": [
    {
      "name": "financial_inclusion_index",
      "value": 0.73,
      "baseline": 0.45,
      "unit": "index"
    }
  ],
  "description": "Increases financial access for underbanked populations"
}
```

---
**Solution:** Use exact enum values from DHAIE Relationship Taxonomy.
```json
// ❌ Bad
"relationship": "uses_data_from"

// ✅ Good
"relationship": "data.provider.primary"
```

---

## 📞 Contacts

**General Inquiries:**
- 📧 Email: `info@designhumanai.com`
- 💬 GitHub: [github.com/designhumanai/dhaie-rai-core](https://github.com/designhumanai/dhaie-rai-core)

**Research Partnerships:**
- 📧 Email: `research@designhumanai.com`

**Technical Discussions:**
- 💬 GitHub Discussions: [Architecture and schema discussions](https://github.com/designhumanai/dhaie-rai-core/discussions)

**Commercial Licensing:**
- 📧 Email: `dhaie@designhumanai.com`

---

## 📜 License

[![Apache-2.0](https://img.shields.io/badge/Code-Apache--2.0-blue.svg?style=for-the-badge)](LICENSE)
[![CC BY-NC-SA 4.0](https://img.shields.io/badge/Docs-CC_BY_NC_SA_4.0-lightgrey.svg?style=for-the-badge)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![DHAIE ECS: 92%](https://img.shields.io/badge/DHAIE_ECS-92%25-green.svg?style=for-the-badge)](ETHICS.md)

### 📄 For This Document
- **License:** [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/)
- **SPDX Identifier:** `CC-BY-NC-SA-4.0`
- **Copyright:** © Viktor Savitskiy, 1995–2025

### 🖥️ For Code Implementation
- **License:** [Apache License 2.0](LICENSE)
- **Applies to:** JSON schema files, validation code, reference implementations

**Complete licensing information:** [LICENSE](LICENSE) | [NOTICE](NOTICE)

---

**Copyright © Viktor Savitskiy, 1995–2025**

---

## 📊 Appendix: Field Quick Reference

| Field | Required | Type | Purpose |
|-------|----------|------|---------|
| `@context` | ✅ | Object | JSON-LD vocabulary definition |
| `@type` | ✅ | String | RDF type (always `dhaie:ReflexiveServiceManifest`) |
| `@id` | ✅ | URI | Globally unique manifest identifier |
| `name` | ✅ | String | Human-readable service name |
| `version` | ✅ | String | Service implementation version (semver) |
| `dhaie:manifestVersion` | ✅ | String | Schema version (currently `"1.0"`) |
| `description` | ✅ | String | Technical summary of functionality |
| `dhaie:businessPurpose` | ✅ | String | Why the service exists (business value) |
| `dhaie:domainContext` | ✅ | String | Location in business architecture |
| `provider` | ✅ | Object | Organization responsible for service |
| `dhaie:ethicalConstraints` | ✅ | Array | Regulatory and ethical compliance declarations |
| `dhaie:consentMechanism` | ⚠️ | String | How user consent is obtained (conditional) |
| `dhaie:operations` | ❌ | Array | Service capabilities and operations |
| `dhaie:socialImpact` | ❌ | Object | Social benefit metrics |
| `dhaie:semanticDependencies` | ❌ | Array | Relationships with other services |

**Legend:**
- ✅ Always required
- ⚠️ Conditionally required (see field documentation)
- ❌ Optional

---

## 🎓 Glossary

**Reflexive Service:** A service that can semantically describe its own purpose, dependencies, and ethical constraints.

**Semantic Dependency:** A relationship between services enriched with business context and consent implications.

**Business Purpose:** The fundamental reason a service exists in business terms, not technical terms.

**Domain Context:** A hierarchical path locating a service within an organization's business architecture.

**Ethical Constraint:** A regulatory, legal, or moral requirement that governs service behavior.

**Consent Mechanism:** The method by which user permission is obtained for data processing.

**Social Impact:** Measurable positive contribution to society or alignment with cognitive equity principles.

**Knowledge Graph:** A semantic network of services, their relationships, and constraints (typically stored in Neo4j).

**Drift Detection:** Validation that runtime behavior matches the declared manifest intent.

---

**End of Specification**
