# DHAIE Semantic Observer

**Real-time Architecture Intelligence Aggregator for Reflexive AI Systems**

[![Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](../LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![Neo4j 5.13](https://img.shields.io/badge/Neo4j-5.13-008CC1.svg)](https://neo4j.com/)

---

## 🎯 What is Semantic Observer?

The **Semantic Observer** is the central intelligence service that:

1. **Collects** service manifests from distributed services
2. **Builds** a live knowledge graph in Neo4j
3. **Exposes** semantic queries via REST API
4. **Validates** manifest coherence and drift detection
5. **Monitors** consent compliance and ethical alignment

> **"The brain of the reflexive system that makes architecture understandable"**

---

## 📋 Project Status

| Phase | Status | Completion |
|-------|--------|------------|
| **Step 1: FastAPI Setup** | ✅ Complete | 100% |
| **Step 2: Neo4j Integration** | ✅ Complete | 100% |
| **Step 3: Manifest Ingestion** | ⏳ Next | 0% |
| **Step 4: Graph Queries** | 📋 Planned | 0% |
| **Step 5: Integration Tests** | 📋 Planned | 0% |

---

## 🚀 Quick Start

### Prerequisites

- **Docker** 24+ and **Docker Compose** 2.20+
- **Python** 3.11+ (for local development)
- **Neo4j** 5.13+ (or use Docker)

### Using Docker Compose (Recommended)

```bash
# Start Neo4j + Semantic Observer
docker-compose -f docker-compose.dev.yml up

# Access services:
# - Semantic Observer API: http://localhost:8080
# - OpenAPI docs: http://localhost:8080/docs
# - Neo4j Browser: http://localhost:7474
```

### Local Development

```bash
# 1. Start Neo4j
docker run -d \
  --name neo4j-dev \
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/dhaie-rai-dev \
  neo4j:5.13-community

# 2. Install dependencies
cd semantic-observer
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Run Semantic Observer
uvicorn app.main:app --reload --port 8080

# Or directly:
python app/main.py
```

---

## 📊 API Endpoints

### Health Check
```bash
curl http://localhost:8080/health
```

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-10-19T12:34:56Z",
  "version": "1.0.0",
  "neo4j_connected": true,
  "manifest_count": 0
}
```

### Root Info
```bash
curl http://localhost:8080/
```

**Response (JSON-LD):**
```json
{
  "@context": "https://schema.org/",
  "@type": "SoftwareApplication",
  "name": "DHAIE Semantic Observer",
  "version": "1.0.0",
  "description": "Real-time architecture intelligence aggregator",
  "documentation": "/docs",
  "health": "/health"
}
```

### OpenAPI Documentation
Visit http://localhost:8080/docs for interactive API documentation.

---

## 🧪 Testing

### Run Tests
```bash
# Install test dependencies
pip install pytest pytest-asyncio pytest-cov

# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=app --cov-report=html

# Run specific test file
pytest tests/test_neo4j_client.py -v
```

### Test Coverage
```bash
# Generate coverage report
pytest tests/ --cov=app --cov-report=term-missing

# View HTML coverage report
open htmlcov/index.html
```

---

## 🗂️ Project Structure

```
semantic-observer/
├── app/
│   ├── __init__.py              # Package initialization
│   ├── main.py                  # FastAPI application (Step 1 ✅)
│   ├── neo4j_client.py          # Neo4j client wrapper (Step 2 ✅)
│   ├── models.py                # Pydantic models (Step 3)
│   └── routes/                  # API endpoints (Step 4)
│       ├── __init__.py
│       ├── manifests.py         # Manifest ingestion
│       ├── graph.py             # Graph queries
│       └── health.py            # Health checks
├── neo4j/
│   ├── schema.cypher            # Graph schema (Step 2 ✅)
│   └── queries.py               # Query templates (Step 4)
├── tests/
│   ├── __init__.py              # Test package init (Step 2 ✅)
│   ├── test_neo4j_client.py    # Neo4j tests (Step 2 ✅)
│   ├── test_api.py              # API tests (Step 5)
│   └── test_integration.py     # E2E tests (Step 5)
├── Dockerfile                   # Production container (Step 1 ✅)
├── requirements.txt             # Python dependencies (Step 1 ✅)
├── README.md                    # This file
└── .gitignore                   # Git ignore rules
```

---

## 🔧 Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `NEO4J_URI` | `bolt://localhost:7687` | Neo4j connection URI |
| `NEO4J_USER` | `neo4j` | Neo4j username |
| `NEO4J_PASSWORD` | `dhaie-rai-dev` | Neo4j password |
| `LOG_LEVEL` | `INFO` | Logging level |

### Example `.env` file
```bash
NEO4J_URI=bolt://neo4j:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your-secure-password
LOG_LEVEL=DEBUG
```

---

## 📚 Neo4j Schema

### Node Labels
- `:Service` - Core service entity from manifests
- `:EthicalConstraint` - Regulatory compliance declarations
- `:Operation` - Service operations/capabilities
- `:SocialImpact` - Social impact metrics

### Relationship Types
- `:DEPENDS_ON` - Semantic dependencies between services
- `:COMPLIES_WITH` - Service compliance with ethical constraints
- `:HAS_OPERATION` - Service capabilities
- `:HAS_IMPACT` - Social impact declarations

### Example Queries

**Find all services:**
```cypher
MATCH (s:Service)
RETURN s.name, s.domainContext, s.businessPurpose
ORDER BY s.name
```

**Find services in FinTech domain:**
```cypher
MATCH (s:Service)
WHERE s.domainContext STARTS WITH 'FinTech'
RETURN s.name, s.businessPurpose
```

**Get database statistics:**
```cypher
MATCH (s:Service)
RETURN count(s) as service_count
```

---

## 🛡️ Security

### Development
- Neo4j default password: `dhaie-rai-dev`
- No authentication on API endpoints
- Docker containers run as non-root user

### Production Recommendations
- ✅ Change default Neo4j password
- ✅ Enable TLS for Neo4j (use `neo4j+s://` URI)
- ✅ Add API authentication (JWT tokens)
- ✅ Use secrets management (Vault, AWS Secrets Manager)
- ✅ Enable CORS only for trusted origins
- ✅ Run behind reverse proxy (nginx, Traefik)

---

## 📊 Monitoring

### Health Checks

**Docker healthcheck:**
```dockerfile
HEALTHCHECK --interval=30s --timeout=10s \
  CMD curl -f http://localhost:8080/health || exit 1
```

**Kubernetes liveness probe:**
```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 30
  periodSeconds: 10
```

### Metrics (Coming in Step 5)
- Prometheus metrics endpoint: `/metrics`
- Grafana dashboard templates
- Neo4j query performance metrics

---

## 🐛 Troubleshooting

### Neo4j Connection Failed

**Error:** `ServiceUnavailable: Could not connect to Neo4j`

**Solution:**
```bash
# Check Neo4j is running
docker ps | grep neo4j

# Check Neo4j logs
docker logs dhaie-neo4j

# Verify credentials
docker exec dhaie-neo4j cypher-shell -u neo4j -p dhaie-rai-dev "RETURN 1"
```

### Port Already in Use

**Error:** `Address already in use: 8080`

**Solution:**
```bash
# Find process using port
lsof -i :8080  # macOS/Linux
netstat -ano | findstr :8080  # Windows

# Kill process or change port
uvicorn app.main:app --port 8081
```

### Module Import Errors

**Error:** `ModuleNotFoundError: No module named 'app'`

**Solution:**
```bash
# Ensure you're in the correct directory
cd semantic-observer

# Reinstall dependencies
pip install -r requirements.txt

# Run from project root
python -m app.main
```

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create feature branch: `git checkout -b feature/step3-manifest-ingestion`
3. Commit with semantic message: `git commit -m "Add: manifest validation endpoint"`
4. Push and create Pull Request

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

---

## 📜 License

**Code:** Apache License 2.0  
**Documentation:** CC BY-NC-SA 4.0

See [LICENSE](../LICENSE) for details.

---

## 📞 Support

- 📧 Email: info@designhumanai.com
- 💬 GitHub: [dhaie-rai-core](https://github.com/designhumanai/dhaie-rai-core)
- 📖 Docs: [manifest-schema.md](../docs/manifest-schema.md)

---

**Copyright © Viktor Savitskiy, 2025**  
**DHAIE Project – Reflexive AI Infrastructure**
