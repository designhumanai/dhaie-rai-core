# Third-Party Dependencies

This document lists all third-party software components used in DHAIE RAI Core, including their licenses and usage.

---

## Core Infrastructure

### Neo4j Community Edition
- **License:** GPL v3 (Community Edition) / Apache 2.0 (Java Driver)
- **Usage:** Semantic knowledge graph storage
- **Website:** https://neo4j.com/
- **License Details:** https://neo4j.com/licensing/
- **Note:** We use the Apache 2.0 licensed Java driver for client connections

### OpenTelemetry
- **License:** Apache 2.0
- **Usage:** Distributed tracing and semantic tag enrichment
- **Website:** https://opentelemetry.io/
- **License Details:** https://github.com/open-telemetry/opentelemetry-specification/blob/main/LICENSE

---

## Backend Frameworks

### Spring Boot
- **License:** Apache 2.0
- **Usage:** Java microservices framework for reference implementations
- **Website:** https://spring.io/projects/spring-boot
- **License Details:** https://github.com/spring-projects/spring-boot/blob/main/LICENSE.txt

### FastAPI
- **License:** MIT
- **Usage:** Python async web framework for Semantic Observer
- **Website:** https://fastapi.tiangolo.com/
- **License Details:** https://github.com/tiangolo/fastapi/blob/master/LICENSE

---

## Frontend Libraries

### React
- **License:** MIT
- **Usage:** UI framework for visualization dashboard
- **Website:** https://react.dev/
- **License Details:** https://github.com/facebook/react/blob/main/LICENSE

### D3.js
- **License:** ISC
- **Usage:** Data visualization for semantic graphs
- **Website:** https://d3js.org/
- **License Details:** https://github.com/d3/d3/blob/main/LICENSE

### Vis.js Network
- **License:** Apache 2.0 / MIT (dual)
- **Usage:** Graph visualization (alternative to D3)
- **Website:** https://visjs.org/
- **License Details:** https://github.com/visjs/vis-network/blob/master/LICENSE-APACHE-2.0

---

## Data Processing

### JSON-LD Java
- **License:** BSD 3-Clause
- **Usage:** JSON-LD processing for semantic manifests
- **Website:** https://github.com/jsonld-java/jsonld-java
- **License Details:** https://github.com/jsonld-java/jsonld-java/blob/master/LICENCE

### Apache Jena
- **License:** Apache 2.0
- **Usage:** RDF/OWL processing for knowledge graphs
- **Website:** https://jena.apache.org/
- **License Details:** https://www.apache.org/licenses/LICENSE-2.0

---

## Testing & Quality

### JUnit 5
- **License:** Eclipse Public License 2.0
- **Usage:** Unit testing framework
- **Website:** https://junit.org/junit5/
- **License Details:** https://github.com/junit-team/junit5/blob/main/LICENSE.md

### pytest
- **License:** MIT
- **Usage:** Python testing framework
- **Website:** https://pytest.org/
- **License Details:** https://github.com/pytest-dev/pytest/blob/main/LICENSE

---

## Development Tools

### Docker
- **License:** Apache 2.0
- **Usage:** Containerization for deployment
- **Website:** https://www.docker.com/
- **License Details:** https://github.com/moby/moby/blob/master/LICENSE

### Docker Compose
- **License:** Apache 2.0
- **Usage:** Multi-container orchestration
- **Website:** https://docs.docker.com/compose/
- **License Details:** https://github.com/docker/compose/blob/main/LICENSE

---

## License Considerations

### GPL v3 Components
**Neo4j Community Edition** uses GPL v3 for the database server. In our architecture:
- We use only the **Apache 2.0 licensed Java driver** for client connections
- The database server runs as a separate service
- No GPL code is linked into our Apache 2.0 codebase
- This maintains Apache 2.0 compliance for DHAIE RAI Core

### License Compliance
All direct dependencies are compatible with Apache 2.0:
- Permissive licenses (MIT, BSD, ISC): ✅ Full compatibility
- Apache 2.0: ✅ Same license
- GPL v3: ✅ Only used via separate service boundary

---

## Python Dependencies (Semantic Observer)

```yaml
# requirements.txt equivalent
fastapi: MIT
uvicorn: BSD 3-Clause
pydantic: MIT
neo4j-driver: Apache 2.0
opentelemetry-api: Apache 2.0
opentelemetry-sdk: Apache 2.0
jsonschema: MIT
httpx: BSD 3-Clause
python-jose: MIT
```

---

## Java Dependencies (Reference Implementations)

```xml
<!-- Maven dependencies -->
<dependencies>
  <!-- Spring Boot Starter -->
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <version>3.x</version>
    <!-- License: Apache 2.0 -->
  </dependency>
  
  <!-- Neo4j Driver -->
  <dependency>
    <groupId>org.neo4j.driver</groupId>
    <artifactId>neo4j-java-driver</artifactId>
    <version>5.x</version>
    <!-- License: Apache 2.0 -->
  </dependency>
  
  <!-- OpenTelemetry -->
  <dependency>
    <groupId>io.opentelemetry</groupId>
    <artifactId>opentelemetry-api</artifactId>
    <version>1.x</version>
    <!-- License: Apache 2.0 -->
  </dependency>
  
  <!-- JSON-LD -->
  <dependency>
    <groupId>com.github.jsonld-java</groupId>
    <artifactId>jsonld-java</artifactId>
    <version>0.13.x</version>
    <!-- License: BSD 3-Clause -->
  </dependency>
</dependencies>
```

---

## License Compatibility Matrix

| Component | License | Status | Compatible with Apache 2.0 | Notes |
|-----------|---------|---------|----------------------------|-------|
| Neo4j Driver | Apache 2.0 | ✅ Direct Use | ✅ Yes | Using client driver only |
| OpenTelemetry | Apache 2.0 | ✅ Direct Use | ✅ Yes | Same license |
| Spring Boot | Apache 2.0 | ✅ Direct Use | ✅ Yes | Same license |
| FastAPI | MIT | ✅ Direct Use | ✅ Yes | MIT is permissive |
| React | MIT | ✅ Direct Use | ✅ Yes | MIT is permissive |
| D3.js | ISC | ✅ Direct Use | ✅ Yes | ISC is permissive |
| JSON-LD Java | BSD 3-Clause | ✅ Direct Use | ✅ Yes | BSD is permissive |
| Apache Jena | Apache 2.0 | ✅ Direct Use | ✅ Yes | Same license |
| Neo4j Server | GPL v3 | 🔄 Service Boundary | ✅ Yes | Separate service, no linking |

---

## License Verification Commands

```bash
# Java projects
mvn license:add-third-party

# Python projects  
pip-licenses --format=markdown

# Full dependency tree
mvn dependency:tree
pipdeptree

# Security scanning
trivy fs --security-checks vuln,config .
snyk test
```

---

## Security Scanning

We use multiple layers of security scanning:

- **Trivy:** Container and filesystem vulnerability scanning
- **Snyk:** Open-source security monitoring
- **OWASP Dependency-Check:** Vulnerability detection
- **GitHub Dependabot:** Automated security updates

## Update Policy

- **Critical security patches:** Applied within 72 hours
- **Minor versions:** Quarterly review and testing
- **Major versions:** 6-month evaluation cycle with compatibility testing
- **License changes:** Immediate review and assessment

---

## How to Update This Document

When adding new dependencies:

1. Add the dependency to the appropriate section
2. Include: name, license, usage, website, license URL
3. Verify license compatibility with Apache 2.0
4. Update the compatibility matrix
5. Run license scanning tools: `mvn license:add-third-party` or `pip-licenses`
6. Perform security scan: `trivy fs .`

---

## Automated Dependency Scanning

We use the following tools to track dependencies:

- **Java:** Maven License Plugin
- **Python:** pip-licenses
- **Docker:** Trivy for container scanning
- **GitHub:** Dependabot for security updates
- **CI/CD:** Automated license checks in pull requests

---

**Last Updated:** October 2025  
**Maintainer:** Viktor Savitskiy (info@designhumanai.com)
