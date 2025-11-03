# TODO List - Testing (Ejemplo TDD)

## Requisitos
- Python 3.8+
- pip install -r requirements.txt

## Ejecutar tests

```bash
pytest -q
coverage run -m pytest && coverage report -m
````

## Flujo recomendado (TDD)

1. Red: escribe test
2. Green: implementa mínimo
3. Refactor: mejora diseño
4. Commit con mensajes descriptivos

## CI

Incluye un workflow de GitHub Actions en `.github/workflows/ci.yml` que ejecuta pytest y muestra coverage.