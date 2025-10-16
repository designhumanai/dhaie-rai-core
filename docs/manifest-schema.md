# Схема семантического манифеста

*JSON-LD спецификация для самоописывающихся сервисов.*

## Статус
✅ Черновая версия готова

## Пример
```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareService",
  "name": "ServiceName",
  "businessPurpose": "Описание назначения",
  "ethicalConstraints": ["constraint1", "constraint2"]
}
