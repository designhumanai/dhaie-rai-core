<!--
SPDX-License-Identifier: CC-BY-NC-SA-4.0
Copyright © Viktor Savitskiy, 1995–2025
-->

# DHAIE RAI Service Manifest Schema v1.1

> **Semantic Self-Description for Reflexive AI Systems**
>
> *"Systems should describe and explain themselves in human-meaningful terms."*

---

## 📖 Overview

The **DHAIE RAI Service Manifest** is the foundational contract of a Reflexive AI infrastructure. It is a machine-readable, semantically rich document that allows a service to declare not only *what* it does, but **why** it exists, **what** it means in a business context, **how** it complies with ethical and regulatory constraints, and **what relationships** it has with other services.

This document specifies the structure, semantics, and intended use of the Service Manifest Schema v1.1.

### What's New in v1.1

**Released:** October 18, 2025

- ✅ **`$comment` field support** for license headers and educational annotations
- ✅ **Educational comments** added to schema for better developer guidance
- ✅ **Comprehensive relationship taxonomy guide** in schema `$defs`
- ✅ **Enhanced social impact metrics** descriptions with measurement examples
- ✅ **Improved documentation** based on real reference implementation experience
- ✅ **Full backward compatibility** with v1.0 manifests

See [CHANGELOG.md](../CHANGELOG.md) for complete version history.

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
- **Schema Version:** v1.1 (October 2025)
- **Schema URL:** `https://designhumanai.com/schemas/service-manifest/v1.1/schema.json`
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

#### `$comment` (v1.1+)
- **Type:** `String` or `Array` of `String`
- **Required:** ❌ No
- **Description:** Optional metadata comments for documentation, license headers, and educational purposes. Ignored by validators but valuable for human readers.
- **Best Practice:** Use for SPDX license identifiers, copyright notices, and inline documentation in reference implementations.
- **Example:**
  ```json
  "$comment": "SPDX-License-Identifier: Apache-2.0",
  "$comment": "Copyright © Viktor Savitskiy, 1995-2025",
  "$comment": "Part of DHAIE RAI Core: https://github.com/designhumanai/dhaie-rai-core"
  ```

---

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
- **Best Practice:** Use business-friendly names, not technical identifiers. Example: "Cross-Border Payment Engine" not "payment-svc-v2".
- **Example:**
  ```json
  "name": "Cross-Border Payment Engine"
  ```

---

#### `version`
- **Type:** `String` (schema.org/Text)
- **Required:** ✅ Yes
- **Description:** The version of the service software implementation itself. Follows semantic versioning (MAJOR.MINOR.PATCH). This is the service version, not the manifest schema version.
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
- **Format:** Fixed string for this specification: `"1.1"`
- **Note:** Validators MUST accept manifests with manifestVersion "1.0" or "1.1" (same MAJOR version = compatible per semantic versioning).
- **Example:**
  ```json
  "dhaie:manifestVersion": "1.1"
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
- **Description:** **CRITICAL FIELD for reflexivity.** A statement explaining the *raison d'être* of the service—the business value it provides and the problem it solves in the domain.
- **Philosophy:** Answers "Why would a business pay for this to exist?" and "What human need does this serve?" Focus on human value, not technical implementation.
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
- **Best Practice:** Define a controlled vocabulary within your organization. Common top-level domains: `FinTech`, `Healthcare`, `Ecommerce`, `Manufacturing`, `Education`. Format: Domain.Subdomain.Capability (e.g., FinTech.Payments.International).
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
- **Best Practice:** Use category to group related operations. Declare primary service capabilities with semantic metadata about state changes, PII handling, and audit requirements.
- **Object Fields:**
  - `$comment` (String, Optional, v1.1+): Educational comment for this operation.
  - `name` (String, Required): A unique, machine-readable identifier for the operation.
    - MUST match regex: `^[a-z][a-zA-Z0-9]{2,49}$` (camelCase, 3-50 chars)
    - Use verb-based names: initiateTransfer, scoreRisk, viewRecords
  - `description` (String, Required): A human-readable explanation of the operation. Min 10, max 300 characters.
  - `category` (String, Optional): A high-level grouping.
    - Allowed values: `financial`, `dataQuery`, `dataMutation`, `admin`, `compute`, `orchestration`, `notification`, `authentication`
    - `compute` for stateless processing, `orchestration` for multi-service coordination
  - `mutates` (Boolean, Optional): Whether this operation changes system state (creates, updates, deletes data). True for CREATE/UPDATE/DELETE, false for READ-only queries. Critical for understanding side effects.
  - `piiFields` (Array of String, Optional): List of PII field names involved in this operation. Each must match `^[a-zA-Z][a-zA-Z0-9_]*$`. Must be unique. Triggers consentMechanism requirement at manifest level.
  - `auditRequired` (Boolean, Optional): Whether this operation requires audit logging for compliance purposes. True for compliance-critical operations (financial transactions, PHI access, admin actions).
- **Example:**
  ```json
  "dhaie:operations": [
    {
      "name": "fundsTransfer",
      "description": "Initiates a transfer of funds between two specified accounts with fraud detection.",
      "category": "financial",
      "mutates": true,
      "piiFields": ["accountNumber", "recipientName", "senderName"],
      "auditRequired": true,
      "$comment": "Requires explicit consent due to PII handling"
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
- **Description:** **REQUIRED FIELD. Every service must declare at least one ethical/regulatory constraint.** A structured declaration of the ethical, legal, and regulatory frameworks that govern the service's operation. This is a core tenet of the DHAIE Reflexive AI principle, making constraints explicit and machine-readable. This is foundational to DHAIE's ethical-by-design philosophy.
- **Object Fields:**
  - `regulation` (String, Required): The common name of the regulation or standard. Min 2, max 50 characters. Use widely recognized names: GDPR, HIPAA, SOC 2, ISO 27001, Algorithmic Fairness.
  - `uri` (URI, Optional but strongly recommended): A direct link to the official text or authoritative definition of the constraint. Links to authoritative sources enable auditors to verify compliance claims.
  - `articles` (Array of String, Optional): Specific articles, sections, or rules within the regulation that are relevant. Each must match pattern `^[A-Z][a-zA-Z]+ \d+.*$` (e.g., "Article 6", "Section 1234"). Format: 'Article 6(1)(a)', '45 CFR 164.502', 'Section 1234'. Omit if not applicable. Must be unique.
  - `implementation` (String, Required): A brief, human-readable description of how the service implements this constraint. Min 10, max 500 characters. Be specific about technical controls and procedures. This is auditable documentation.
  - `verificationMethod` (Object, Optional): Machine-actionable compliance verification. Include tools and last verification date for audit trails.
    - `type` (String, Required): Enum: `automated_scan`, `manual_audit`, `third_party_certification`, `continuous_monitoring`
      - `automated_scan`: CI/CD integrated (e.g., policy-as-code)
      - `manual_audit`: periodic reviews
      - `third_party_certification`: external auditor
      - `continuous_monitoring`: real-time compliance checking
    - `tool` (String, Optional): Name of verification tool or certification body (e.g., "OpenPolicyAgent", "Vanta"). Max 100 characters.
    - `policyUri` (URI, Optional): Link to machine-readable policy definition (e.g., OPA rego file).
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
  - **REQUIRED if:** (1) any operation has piiFields, OR (2) any dependency has consentImplications.
  - Use 'no_pii_processed' ONLY if truly no PII is handled.
  - 'explicit_consent_required' is default for GDPR/CCPA compliance.
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
- **Description:** Optional but encouraged. Quantify positive societal contribution using standardized metrics. Critical for DHAIE's cognitive equity principles. Qualitative or quantitative metrics that describe the service's intended positive contribution to society or its alignment with DHAIE's cognitive equity principles.
- **Object Fields:**
  - `metrics` (Array of Object, Optional): Structured, measurable social impact indicators. Use standardized metric names from DHAIE taxonomy. Each metric must be an object with name, value, and optional baseline/unit/measurementMethod.
    - `name` (String, Required): Standardized metric name from DHAIE taxonomy.
      - Allowed values: `financial_inclusion_index`, `cross_border_cost_reduction`, `carbon_footprint_reduction`, `accessibility_improvement`, `cognitive_equity_score`, `digital_divide_reduction`, `healthcare_access_improvement`, `education_accessibility`
      - **Examples of metrics:**
        - `financial_inclusion_index`: 0-1 scale measuring access to financial services
        - `cross_border_cost_reduction`: percentage savings vs baseline
        - `accessibility_improvement`: WCAG compliance or similar
        - `cognitive_equity_score`: fairness metric across demographic groups
    - `value` (Number, Required): The measured value.
    - `baseline` (Number, Optional): Baseline value for comparison (what it was before this service). What was the metric before this service? Essential for measuring improvement.
    - `unit` (String, Optional): Unit of measurement (e.g., "percentage", "index", "USD saved"). Max 50 characters. Examples: 'percentage', 'index (0-1)', 'USD saved', 'users served'.
    - `measurementMethod` (String, Optional): How this metric is measured/calculated. Max 200 characters. Cite methodology: 'World Bank Financial Inclusion Index', 'WCAG 2.1 AA compliance score', 'Gini coefficient calculation'.
  - `description` (String, Required): A narrative description of the social impact. Min 20, max 700 characters. Tell the human story. Who benefits? How does this reduce inequality or improve lives? Complement quantitative metrics with qualitative context.
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
- **Description:** Declares other services that this service relies upon to fulfill its purpose, enriching the basic "dependency" with the *semantic reason* for that dependency. This is crucial for the Semantic Observer to build an accurate knowledge graph and for Drift Detector to validate behavioral consistency. Declare service dependencies with business context and consent implications. Use DHAIE Relationship Taxonomy for 'relationship' field. This is semantic architecture, not just technical integration.
- **Object Fields:**
  - `$comment` (String, Optional, v1.1+): Educational comment for this dependency.
  - `target` (String, Required): The `name` of the dependent-upon service. Min 3, max 100 characters. Use the service's 'name' field value, not technical hostname or service ID.
  - `targetUri` (URI, Optional but strongly recommended): The `@id` of the dependent-upon service's manifest for explicit semantic linking. MUST start with `https://`. Omit if not available. Should point to target's @id field for explicit semantic linking. Strongly recommended for knowledge graph construction.
  - `relationship` (String, Required): The nature of the dependency from the DHAIE Relationship Taxonomy (see below). DHAIE Relationship Taxonomy categorizes dependencies by business purpose, not technical implementation. data.provider.* = source of data, risk.assessment.* = risk/fraud checking, orchestration.* = workflow coordination, ledger.* = audit trail, auth.* = authentication/authorization. See manifest-schema.md for complete taxonomy reference.
  - `businessReason` (String, Required): A clear explanation of *why* this dependency exists. Min 10, max 500 characters. **CRITICAL:** Explain the business/regulatory/operational need, not just 'we call this API'. Example: 'AML regulation requires risk scoring for transactions >$10k' not 'calls fraud detection service'.
  - `consentImplications` (String, Optional): Describes what data is shared with the dependency and implications for user consent. Min 10, max 300 characters. Omit if no data sharing occurs. Be explicit about data sharing. If present, parent service MUST declare consentMechanism. State 'No PII shared' when applicable.
  - `condition` (Object, Optional): Defines when this dependency is activated (conditional dependency). Conditional dependencies model business rules. Use pseudo-code or natural language for 'when'. Do NOT add $comment inside condition object (violates additionalProperties).
    - `when` (String, Required): Condition expression in pseudo-code or natural language. Max 200 characters. Examples: 'transaction.amount.usd > 10000', 'user.tier == premium', 'risk_score > 80 OR manual_review_requested'.
    - `enforcementLevel` (String, Required): Enum: `mandatory`, `recommended`, `optional`
      - `mandatory`: always enforced (hard requirement)
      - `recommended`: best practice but skippable
      - `optional`: optimization/enhancement only

---

### 📚 DHAIE Relationship Taxonomy

**Quick reference for choosing correct relationship types.**

**Category: Data Flow**
- `data.provider.primary` — *This dependency is the authoritative source of data*
  - Authoritative source (e.g., CRM → Customer data)
  - Example: "Customer profile data comes from the CRM service"
- `data.provider.cache` — *This dependency provides cached/replicated data*
  - Cached/replicated data (e.g., CDN → Product catalog)
  - Example: "Uses cached product catalog from the CDN service"
- `data.provider.realtime` — *This dependency streams real-time data*
  - Streaming data (e.g., Market ticker → Price feed)
  - Example: "Consumes real-time market prices from the ticker service"
- `data.consumer.analytics` — *This dependency consumes our data for analytics*
  - Analytics destination (e.g., Transactions → BI warehouse)
  - Example: "Transaction data is sent to the BI warehouse"
- `data.consumer.backup` — *This dependency stores backup copies of our data*
  - Backup storage (e.g., Daily snapshots → Archive)
  - Example: "Daily snapshots are sent to the archive service"
- `data.consumer.export` — *This dependency receives data for external export*
  - External export (e.g., Reports → Regulatory filing)
  - Example: "Sends financial reports to the regulatory filing service"

**Category: Risk & Compliance**
- `risk.assessment.required` — *Mandatory risk evaluation before proceeding*
  - Mandatory risk check (e.g., AML screening)
  - Example: "Fraud check is required for all transactions"
- `risk.assessment.optional` — *Optional risk scoring for optimization*
  - Optional risk scoring (e.g., Credit check for premium)
  - Example: "Credit score check for premium tier users"
- `compliance.verification.mandatory` — *Required compliance check*
  - Required compliance (e.g., GDPR consent check)
  - Example: "AML screening is legally required for cross-border payments"
- `compliance.verification.optional` — *Optional compliance enhancement*
  - Optional enhancement (e.g., Enhanced due diligence)
  - Example: "Enhanced due diligence for high-value customers"

**Category: Orchestration**
- `orchestration.trigger` — *This service initiates a workflow in the dependency*
  - Initiates workflow (e.g., Payment → Fulfillment)
  - Example: "Triggers the order fulfillment workflow after payment confirmation"
- `orchestration.coordinate` — *This service coordinates with the dependency in a saga/choreography*
  - Saga/choreography (e.g., Inventory reservation)
  - Example: "Coordinates inventory reservation with the warehouse service"

**Category: Computation**
- `computation.specialized` — *Offloads specialized computation*
  - ML/specialized compute (e.g., Recommendation engine)
  - Example: "Offloads ML inference to the recommendation engine"
- `computation.offload` — *Offloads general heavy computation*
  - General processing (e.g., PDF generation)
  - Example: "Offloads PDF generation to the document service"

**Category: Notifications**
- `notification.trigger` — *Triggers a notification to be sent*
  - Send notification (e.g., Payment confirmation email)
  - Example: "Sends payment confirmation email via the notification service"
- `notification.subscribe` — *Subscribes to notifications from the dependency*
  - Receive alerts (e.g., Low inventory alert)
  - Example: "Receives alerts when inventory is low"

**Category: Authentication & Authorization**
- `auth.delegation` — *Delegates authentication to this service*
  - SSO/authentication (e.g., Identity provider)
  - Example: "Uses SSO via the identity provider service"
- `auth.verification` — *Verifies authentication tokens/credentials*
  - Token validation (e.g., JWT verification)
  - Example: "Validates JWT tokens against the auth service"

**Category: Ledger & Audit**
- `ledger.append_only` — *Writes immutable audit logs*
  - Immutable audit log (e.g., Blockchain ledger)
  - Example: "Appends transaction records to the blockchain ledger"
- `ledger.query` — *Queries historical audit data*
  - Historical audit queries (e.g., Compliance database)
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

# For production manifests (strict validation)
ajv validate -s schema/service-manifest.schema.json \
             -d examples/payment-service.manifest.json \
             --strict=true

# For examples with $comment (relaxed validation)
ajv validate -s schema/service-manifest.schema.json \
             -d examples/*.manifest.json \
             --strict=false
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

### Changelog v1.1

**Added:**
- Support for `$comment` field at root and within operations/dependencies
- Educational `$comment` annotations on 15+ key properties
- Enhanced descriptions for social impact metrics
- Improved guidance on relationship taxonomy usage
- Examples in `$defs` based on reference implementations

**Unchanged:**
- All required fields remain the same
- All enum values unchanged
- All validation rules preserved
- Full backward compatibility maintained

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

#### 7. **Use `$comment` for Educational Value (v1.1+)**
- Include SPDX license identifiers in header comments
- Add domain-specific context (e.g., "HIPAA requires audit trail")
- Explain non-obvious business rules in conditional dependencies

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
                       -d "manifests/*.json" \
                       --strict=false
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

## 📚 Reference Implementation Examples

Complete, validated examples are available in the `examples/` directory:

### Example 1: FinTech Payment Service
**File:** `examples/payment-service.manifest.json`

Demonstrates:
- Conditional dependencies with business rules
- AML/GDPR compliance declarations
- Social impact metrics (financial inclusion, cost reduction)
- Cross-border payment complexity

### Example 2: ML Fraud Detection Engine
**File:** `examples/fraud-detector.manifest.json`

Demonstrates:
- ML ethics and algorithmic fairness
- Service-as-dependency pattern
- No PII processing with consent mechanism
- Cognitive equity scoring

### Example 3: Healthcare Patient Portal
**File:** `examples/patient-portal.manifest.json`

Demonstrates:
- HIPAA compliance and PHI handling
- Multi-consent mechanisms
- Emergency break-glass access patterns
- Healthcare accessibility metrics

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

#### Error: `"Unknown relationship type"`
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
| `$comment` | ❌ | String/Array | License headers, educational annotations (v1.1+) |
| `@context` | ✅ | Object | JSON-LD vocabulary definition |
| `@type` | ✅ | String | RDF type (always `dhaie:ReflexiveServiceManifest`) |
| `@id` | ✅ | URI | Globally unique manifest identifier |
| `name` | ✅ | String | Human-readable service name |
| `version` | ✅ | String | Service implementation version (semver) |
| `dhaie:manifestVersion` | ✅ | String | Schema version (currently `"1.1"`) |
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
