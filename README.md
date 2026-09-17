# TechStore API — Auditoría de pruebas

## Descripción

API FastAPI para productos y categorías. La auditoría del Módulo IV compara la implementación real con el contrato funcional de TechStore definido en `Mini_Proyecto_Evaluable_Modulo_IV_Auditoria_Pruebas.pdf`.

## Ejecución de la aplicación

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

La instalación reproducible de `requirements.txt` presenta un hallazgo de dependencia por `truststore-0.10.4`, documentado en la evidencia de instalación. Para ejecutar la auditoría en el ambiente utilizado se instalaron las dependencias funcionales compatibles.

## Ejecución de pruebas

```bash
python -m pytest -v tests/test_auditoria_evaluable.py
python -m pytest -v
```

La salida de las ejecuciones se conserva en `auditoria-evaluable-evidence.txt` y `auditoria-regression-evidence.txt`.

## Documentación

- `docs/plan-pruebas.md`: objetivo, alcance, riesgos, estrategia, ambiente y criterios.
- `docs/matriz-trazabilidad.md`: cobertura de RF01–RF12 y RN01–RN08.
- `docs/casos-prueba.md`: 7 casos de Categorías y 18 de Productos.
- `docs/registro-defectos.md`: defectos confirmados, evidencia y plan de retest.
- `docs/informe-ejecucion.md`: métricas, regresión y conclusión técnica.

## Nota de auditoría

La versión actual no cumple todos los criterios de salida. La documentación conserva los fallos y riesgos reales, sin alterar las métricas para presentar una aprobación artificial.
