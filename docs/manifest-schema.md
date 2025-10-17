<!--
SPDX-License-Identifier: CC-BY-NC-SA-4.0
Copyright © Viktor Savitskiy, 1995–2025
-->

# DHAIE RAI Service Manifest Schema v1.0

> **Semantic Self-Description for Reflexive AI Systems**
>
> *"Systems should describe and explain themselves in human-meaningful terms."*

## 📖 Overview

The **DHAIE RAI Service Manifest** is the core of a Reflexive AI infrastructure. It is a machine-readable, semantically rich document that allows a service to declare not only *what* it does, but **why** it exists, **what** it means in a business context, and **how** it complies with ethical and regulatory constraints.

This document specifies the structure, semantics, and intended use of the Service Manifest Schema v1.0.

### Design Philosophy

- **Meaning Before Mechanism:** The business purpose and intent are primary; technical details are secondary.
- **Clarity Before Complexity:** The schema is designed to be understood by developers and stakeholders without a deep background in semantics.
- **Ethics Before Efficiency:** Ethical constraints and compliance are first-class citizens, not optional additions.

## 🎯 Core Concepts

### What is a Reflexive Service?

A Reflexive Service is a software component that can explain its own role, dependencies, and boundaries within a larger system. It goes beyond a technical API description to include:

- **Business Purpose:** The value it provides in the problem domain.
- **Domain Context:** Its place in the business architecture.
- **Semantic Dependencies:** The other services it relies on, and the *reason* for those dependencies.
- **Ethical Layer:** The regulations, consent mechanisms, and social impact considerations it must adhere to.

### The Role of the Manifest

The Manifest acts as a "service passport" within the DHAIE RAI ecosystem. It is used by:

1.  **Semantic Observers:** To build and maintain a live knowledge graph of the system.
2.  **Drift Detectors:** To validate that a service's runtime behavior matches its declared intent.
3.  **Developers & Architects:** To understand service boundaries and interactions at a semantic level.
4.  **Auditors & Regulators:** To verify compliance and ethical alignment.

## 🏗️ Schema Fundamentals

### Format & Compliance

- **Format:** JSON-LD 1.1
- **JSON Schema:** Draft 2020-12 for validation.
- **Core Vocabulary:** Hybrid `schema.org` + `DHAIE` ontology.

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

### Top-Level Identity & Purpose

#### `@id`
- **Type:** `URI` (String, formatted as a Uniform Resource Identifier)
- **Required:** Yes
- **Description:** A globally unique and persistent identifier for this specific service manifest instance. This URI SHOULD be dereferenceable and SHOULD NOT change over the service's lifecycle. It is used to uniquely identify the service node in the RDF knowledge graph.
- **Format:** SHOULD follow a stable, organizational URI pattern. **Best Practice:** Use HTTPS and versioned paths (e.g., `/v1/manifest`).
- **Example:**
  ```json
  "@id": "https://api.example.com/services/payment-engine/v2/manifest"
  ```

#### `name`
- **Type:** `String` (schema.org/Text)
- **Required:** Yes
- **Description:** The human-readable name of the service. This should be a simple, recognizable name used in communications and dashboards.
- **Constraints:** Max 100 characters. MUST match regex: `^[a-zA-Z0-9][\w\s-]{1,98}[a-zA-Z0-9]$` (letters, numbers, spaces, hyphens, underscores; **no leading/trailing whitespace**)
- **Example:**
  ```json
  "name": "Cross-Border Payment Engine"
  ```

#### `version`
- **Type:** `String` (schema.org/Text)
- **Required:** Yes
- **Description:** The version of the service software implementation itself. Follows semantic versioning (MAJOR.MINOR.PATCH).
- **Format:** `semver` (e.g., `2.5.1`)
- **Example:**
  ```json
  "version": "2.5.1"
  ```

#### `dhaie:manifestVersion`
- **Type:** `String`
- **Required:** Yes
- **Description:** The version of the DHAIE Service Manifest schema this document complies with. This allows for schema evolution and runtime validation against the correct specification.
- **Format:** Fixed string for this specification.
- **Example:**
  ```json
  "dhaie:manifestVersion": "1.0"
  ```

#### `description`
- **Type:** `String` (schema.org/Text)
- **Required:** Yes
- **Description:** A clear, concise, and technical summary of *what* the service does functionally. This complements the `dhaie:businessPurpose` which describes the *why*.
- **Constraints:** 1-3 sentences recommended. Max 500 characters.
- **Example:**
  ```json
  "description": "Processes and settles international fiat currency transactions between financial institutions."
  ```

#### `dhaie:businessPurpose`
- **Type:** `String` (schema.org/Text)
- **Required:** Yes
- **Description:** A foundational field for reflexivity. A statement explaining the *raison d'être* of the service—the business value it provides and the problem it solves in the domain.
- **Philosophy:** Answers "Why would a business pay for this to exist?"
- **Constraints:** Max 700 characters. Should be a concise value proposition.
- **Example:**
  ```json
  "dhaie:businessPurpose": "To enable fast, secure, and cost-effective cross-border monetary transfers for migrant workers, thereby promoting financial inclusion and reducing economic friction."
  ```

#### `dhaie:domainContext`
- **Type:** `String`
- **Required:** Yes
- **Description:** A dot-separated path that locates the service within the business architecture and domain ontology. It provides semantic context for discovery and relationship mapping.
- **Format:** MUST match regex: `^[a-zA-Z][a-zA-Z0-9]*(\.[a-zA-Z][a-zA-Z0-9]*){2,}$` (letters, numbers, and dots only; minimum 3 levels; **no whitespace**)
- **Best Practice:** Define a controlled vocabulary within your organization.
- **Examples:**
  ```json
  "dhaie:domainContext": "FinTech.Payments.International"
  ```

### Operational & Technical Context

#### `provider`
- **Type:** `Object` (schema.org/Organization)
- **Required:** Yes
- **Description:** The entity (team, company, department) responsible for developing, maintaining, and operating this service.
- **Fields:**
  - `name` (String, Required): The name of the providing organization.
  - `url` (URI, Optional): A link to the provider's homepage or information page.
- **Example:**
  ```json
  "provider": {
    "name": "Example FinTech Corp",
    "url": "https://www.example.com"
  }
  ```

#### `dhaie:operations`
- **Type:** `Array` of `Object`
- **Required:** No
- **Description:** A list of the primary actions, capabilities, or operations the service exposes. This describes *what* the service can do at a functional level.
- **Object Fields:**
  - `name` (String, Required): A unique, machine-readable identifier for the operation. MUST match regex: `^[a-z][a-zA-Z0-9]{2,49}$` (lowercase first letter, alphanumeric; **no whitespace**)
  - `description` (String, Required): A human-readable explanation of the operation.
  - `category` (String, Optional): A high-level grouping. Suggested values: `financial`, `dataQuery`, `admin`, `compute`, `orchestration`.
- **Example:**
  ```json
  "dhaie:operations": [
    {
      "name": "fundsTransfer",
      "description": "Initiates a transfer of funds between two specified accounts.",
      "category": "financial"
    }
    // ... additional entries as needed (each must follow the specified format)
  ]
  ```

### The Ethical Layer

#### `dhaie:ethicalConstraints`
- **Type:** `Array` of `Object`
- **Required:** Yes
- **Description:** A structured declaration of the ethical, legal, and regulatory frameworks that govern the service's operation. This is a core tenet of the DHAIE Reflexive AI principle, making constraints explicit and machine-readable.
- **Object Fields:**
  - `regulation` (String, Required): The common name of the regulation or standard (e.g., `GDPR`, `HIPAA`, `AML`).
  - `uri` (URI, Strongly Recommended): A direct link to the official text or authoritative definition of the constraint.
  - `articles` (Array of String, Optional): Specific articles, sections, or rules within the regulation that are relevant. **Omit if not applicable.**
  - `implementation` (String, Required): A brief, human-readable description of how the service implements this constraint.
- **Example:**
  ```json
  "dhaie:ethicalConstraints": [
    {
      "regulation": "GDPR",
      "uri": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679",
      "articles": ["Article 6(1)(a)", "Article 7"],
      "implementation": "Explicit user consent is obtained and logged before processing any PII."
    }
    // ... additional entries as needed
  ]
  ```

#### `dhaie:consentMechanism`
- **Type:** `String`
- **Required:** Conditional. Required if the service processes PII. Otherwise, should be set to `"no_pii_processed"`.
- **Description:** Defines the primary mechanism by which user consent is obtained for data processing activities.
- **Allowed Values (Controlled Vocabulary):**
  - `explicit_consent_required`: Consent must be explicitly granted by the user via a clear affirmative action.
  - `implied_consent`: Consent is inferred from user actions and context.
  - `no_pii_processed`: The service does not handle any PII, thus consent is not applicable.
  - `consent_managed_externally`: Consent is handled by a dedicated upstream service.
- **Example:**
  ```json
  "dhaie:consentMechanism": "explicit_consent_required"
  ```

#### `dhaie:socialImpact`
- **Type:** `Object`
- **Required:** No (but strongly encouraged)
- **Description:** Qualitative or quantitative metrics that describe the service's intended positive contribution to society or its alignment with DHAIE's cognitive equity principles.
- **Object Fields:**
  - `metrics` (Array of String, Optional): A list of standardized social impact metrics. All values MUST be unique (**case-sensitive**).
  - `description` (String, Required): A narrative description of the social impact.
- **Standardized Metrics Examples:** `financial_inclusion_index`, `cross_border_cost_reduction`, `carbon_footprint_reduction`, `accessibility_improvement`
- **Example:**
  ```json
  "dhaie:socialImpact": {
    "metrics": ["financial_inclusion_index", "cross_border_cost_reduction"],
    "description": "Reduces the average cost of remittances for migrant workers by over 50%."
  }
  ```

### Semantic Dependencies

#### `dhaie:semanticDependencies`
- **Type:** `Array` of `Object`
- **Required:** No
- **Description:** Declares other services that this service relies upon to fulfill its purpose, enriching the basic "dependency" with the *semantic reason* for that dependency. This is crucial for the Semantic Observer to build an accurate knowledge graph.
- **Object Fields:**
  - `target` (String, Required): The `name` of the dependent-upon service.
  - `targetUri` (URI, Optional): The `@id` of the dependent-upon service's manifest for explicit semantic linking. **Best Practice:** Use stable HTTPS URIs. **Omit if not available.**
  - `relationship` (String, Required): The nature of the dependency. Uses the DHAIE Relationship Taxonomy.
  - `businessReason` (String, Required): A clear explanation of *why* this dependency exists.
  - `consentImplications` (String, Optional): Describes what data is shared and implications for user consent. **Omit if no data sharing occurs.**
- **DHAIE Relationship Taxonomy with Examples:**
  - `data.provider.primary` - *"Customer profile data comes from this service"*
  - `data.provider.cache` - *"Uses cached product catalog from this service"*
  - `risk.assessment.required` - *"Mandatory fraud check for all transactions"*
  - `risk.assessment.optional` - *"Optional credit score check"*
  - `compliance.verification.mandatory` - *"Legal identity verification required"*
  - `orchestration.trigger` - *"Initiates the order fulfillment workflow"*
  - `computation.specialized` - *"Offloads complex ML inference"*
- **Example:**
  ```json
  "dhaie:semanticDependencies": [
    {
      "target": "FraudDetector",
      "targetUri": "https://api.example.com/services/fraud-detector/v1/manifest",
      "relationship": "risk.assessment.required",
      "businessReason": "AML regulation requires risk scoring for transactions >$10k.",
      "consentImplications": "Shares transaction data for analysis."
    },
    {
      "target": "ProductCatalog",
      "targetUri": "https://api.example.com/services/product-catalog/v3/manifest", 
      "relationship": "data.provider.cache",
      "businessReason": "Needs product pricing and availability data.",
      "consentImplications": "No PII shared; only product IDs."
    }
    // ... additional entries as needed (each must follow the specified format)
  ]
  ```

---

💻 Notes for Developers & Validators
This specification is designed for both human comprehension and machine validation. Please observe the following principles when implementing Service Manifests:

Implementation Principles
Optional Field Handling

Omit empty optional fields: Do not include optional fields with null, empty arrays [], or empty objects {} values. If the data is not available or applicable, the field should be absent from the manifest entirely.

Conditional Requirements: Pay close attention to conditionally required fields (e.g., dhaie:consentMechanism). Ensure they are present when conditions are met.

Identifier Stability

Stable URIs: The @id and targetUri fields must use persistent, versioned URIs that do not change over the service's lifecycle. These are fundamental for building reliable knowledge graphs.

Immutable Names: The name and dhaie:operations[].name fields should be treated as immutable identifiers after the first publication. Changes require creating a new service manifest.

Validation & Examples

Examples are Format Templates: The JSON examples provided throughout this document demonstrate the required structure and format, not business logic. Replace all placeholder values with your actual service data.

Schema Compliance: All manifests must validate against the official JSON Schema (service-manifest.schema.json). The human-readable specification and JSON Schema are complementary and must be consistent.

Semantic Integrity

Use Controlled Vocabularies: Adhere to the specified allowed values and relationship taxonomies. Do not extend them without prior coordination, as this breaks semantic interoperability.

Meaningful Descriptions: All description and businessReason fields must contain genuine, human-meaningful explanations. Avoid placeholder text in production manifests.

By following these guidelines, you ensure that your Service Manifests are not only technically valid but also semantically robust and truly reflexive.

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
