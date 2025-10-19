# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Documentation
- **Timeline Update**: Shifted Phase 1 research goals from Q1 2025 to Q4 2025-Q1 2026 for chronological accuracy
- **Research Strategy**: Replaced DARPA AI Exploration application goals with international research collaboration focus
- **Roadmap Alignment**: Updated 90-day sprint to monthly stages (October 2025 - January 2026)
- **Version Synchronization**: Fully synchronized Russian and English documentation versions
- **Publication Path**: Generalized specific conference targets (ICSE 2026, HAI Conference 2026) to peer-reviewed journal focus
- **Ethics Compliance**: Updated approval references from Stanford University IRB to DHAIE Ethics Committee

### Fixed
- **Chronology**: Corrected timeline inconsistencies across all documentation
- **Geopolitical Neutrality**: Removed problematic references to specific government funding programs
- **Realism**: Ensured all dates and milestones reflect current project status (October 2025 context)
- **Consistency**: Aligned project status table with updated roadmap and research goals

## [1.1.0] - 2025-10-18

### Added
- `$comment` field support in schema for license headers and educational notes
- Educational `$comment` annotations on 18 key schema properties
- Comprehensive relationship taxonomy guide in `$defs`
- Reference implementation examples in `$defs`
- Enhanced descriptions for social impact metrics

### Changed
- `manifestVersion` const updated from `"1.0"` to `"1.1"`
- Schema `$id` updated to v1.1 URL

### Migration
- Update `"dhaie:manifestVersion": "1.0"` → `"1.1"` in existing manifests
- No other changes required - full backward compatibility

## [1.0.0] - 2025-10-15

### Added
- Initial release of the DHAIE RAI Service Manifest Schema

---

## 🚀 Release 1.1.0 - Files and Structure

### Files for Download (4 Total)

1. ✅ `service-manifest.schema.json` v1.1
2. ✅ `fraud-detector.manifest.json` v1.1  
3. ✅ `payment-service.manifest.json` v1.1
4. ✅ `patient-portal.manifest.json` v1.1

### Repository Structure

```
dhaie-rai-core/
├── schema/
│   └── service-manifest.schema.json      # v1.1 schema
├── examples/
│   ├── fraud-detector.manifest.json      # Fraud Detector example
│   ├── payment-service.manifest.json     # Payment Service example  
│   └── patient-portal.manifest.json      # Patient Portal example
├── docs/
│   ├── manifest-schema.md                # Updated to v1.1
│   ├── comparison.md                     # Research & validation docs
│   ├── validation.md                     # Validation procedures
│   ├── ethics-checklist.md               # Ethics framework
│   ├── contributing.md                   # Contribution guidelines
│   └── ... (other documentation files)
├── README.md                             # Updated with validation section
├── README.en.md                          # Updated with validation section
├── CHANGELOG.md                          # This file
├── DEPENDENCIES.md                       # Schema validation tools
├── ETHICS.md                             # Ethical framework
├── ACKNOWLEDGMENTS.md                    # Comprehensive acknowledgments
├── LICENSE                               # Apache 2.0 license
└── NOTICE                                # Project notices
```

### Documentation Updates

- **`docs/manifest-schema.md`** - Updated from v1.0 to v1.1 references
- **`README.md` & `README.en.md`** - Added manifest validation sections
- **`docs/validation.md`** - Research and validation procedures
- **`docs/ethics-checklist.md`** - Ethics and compliance framework
