# Changelog

## [1.1.0] - 2025-10-18

### Added
- $comment field support in schema for license headers and educational notes
- Educational $comment annotations on 18 key schema properties
- Comprehensive relationship taxonomy guide in $defs
- Reference implementation examples in $defs
- Enhanced descriptions for social impact metrics

### Changed
- manifestVersion const updated from "1.0" to "1.1"
- Schema $id updated to v1.1 URL

### Migration
- Update `"dhaie:manifestVersion": "1.0"` → `"1.1"` in existing manifests
- No other changes required - full backward compatibility

## [1.0.0] - 2025-10-15

### Initial Release
- Complete DHAIE RAI Service Manifest Schema
- JSON-LD 1.1 and JSON Schema Draft 2020-12 compliance
- Ethical constraints and consent mechanisms
- Semantic dependencies with relationship taxonomy
- Social impact metrics
```

---

## 🚀 Все готово!

### Файлы для скачивания (всего 4):

1. ✅ `service-manifest.schema.json` v1.1 (артефакт: `schema_v1_1`)
2. ✅ `fraud-detector.manifest.json` v1.1 (артефакт: `fraud_detector_correct`)
3. ✅ `payment-service.manifest.json` v1.1 (артефакт: `payment_service_correct`)
4. ✅ `patient-portal.manifest.json` v1.1 (артефакт: `patient_portal_correct`)

### Структура репозитория:
```
dhaie-rai-core/
├── schema/
│   └── service-manifest.schema.json  ← v1.1 (NEW)
├── examples/
│   ├── fraud-detector.manifest.json  ← v1.1 (UPDATED)
│   ├── payment-service.manifest.json ← v1.1 (UPDATED)
│   └── patient-portal.manifest.json  ← v1.1 (UPDATED)
└── docs/
    ├── manifest-schema.md            ← TODO: update references
    └── CHANGELOG.md                  ← TODO: create
