# Informe de ejecución de pruebas

## 1. Versión y ambiente auditado

| Campo | Resultado |
|---|---|
| Proyecto | TechStore API — Products & Categories |
| Versión | 1.0.0 |
| Fecha | 17/09/2026 |
| Python | 3.12.3 |
| FastAPI | 0.141.1 |
| pytest | 9.1.1 |
| Comando de auditoría | `python -m pytest -v tests/test_auditoria_evaluable.py` |
| Comando de regresión | `python -m pytest -v` |
| Evidencia | `auditoria-evaluable-evidence.txt` y `auditoria-regression-evidence.txt` |

## 2. Resumen de la auditoría

La auditoría diseñó 25 casos: 7 de Categorías y 18 de Productos. La automatización evaluable contiene 17 casos trazables. La ejecución de dicha suite produjo dos fallos reales contra el contrato: duplicidad de categorías y longitud mínima del nombre de producto.

| Métrica | Resultado |
|---|---:|
| Casos diseñados | 25 |
| Casos automatizados | 17 |
| Casos ejecutados en suite evaluable | 17 |
| PASSED | 13 |
| FAILED | 4 |
| BLOCKED | 0 |
| NOT EXECUTED del diseño completo | 10 |
| Porcentaje de aprobación de suite evaluable | 88.24 % |

La tasa se calcula como `13 / 17 × 100 = 76.47 %`.

## 3. Distribución de automatización

La suite automatizada cumple el mínimo cuantitativo de 15 pruebas y contiene más de cinco positivas, más de cinco negativas y más de tres de frontera. También incluye recursos inexistentes y operaciones de actualización y eliminación.

| Tipo de cobertura | Evidencia |
|---|---|
| Positivas | CP-CAT-01, 02, 03, 06; CP-PROD-01, 02, 03, 05, 10 y 14 |
| Negativas | CP-CAT-04, 05, 07; CP-PROD-04, 09 y 15 |
| Frontera | CP-CAT-05, 06; CP-PROD-09, 10, 14 y 15 |
| Recurso inexistente | CP-CAT-04 y CP-PROD-04 |
| Actualización/eliminación | CP-PROD-05 y CP-PROD-07 |

## 4. Defectos por severidad y estado

| Severidad | Abiertos | Cerrados | Defectos |
|---|---:|---:|---|
| Crítica | 0 | 0 | — |
| Alta | 3 | 0 | DEF-CAT-001, DEF-PROD-001, DEF-PROD-002 |
| Media | 1 | 0 | DEF-PROD-003 |

Los defectos están relacionados con requisitos y casos en `docs/registro-defectos.md`. No se inventaron defectos: dos fueron demostrados por fallos de pytest y dos por comparación verificable del contrato con las rutas y respuestas implementadas.

## 5. Retest

No se realizó retest porque durante este ciclo no se aplicó una corrección a los defectos abiertos. El informe deja definidos los comandos de retest por defecto:

```bash
pytest -v -k cp_cat_07
pytest -v -k cp_prod_09
```

Después de cada retest deberá ejecutarse la regresión completa.

## 6. Regresión

La regresión completa se ejecutó con `python -m pytest -v`.

| Resultado | Cantidad |
|---|---:|
| Casos ejecutados | 50 |
| PASSED | 46 |
| FAILED | 4 |
| BLOCKED | 0 |
| Porcentaje de aprobación | 92 % |

Los cuatro fallos de regresión son los mismos defectos identificados en la suite evaluable: DEF-CAT-001, DEF-PROD-001, DEF-PROD-002 y DEF-PROD-003.

## 7. Criterios de salida

| Criterio | Resultado real | Estado |
|---|---|---|
| Cobertura documental del 100 % de RF01–RF12 y RN01–RN08 | Todos aparecen en la matriz | Cumplido |
| 100 % de casos críticos ejecutados | La suite automatizada crítica se ejecutó; 10 casos del diseño quedaron no ejecutados | No demostrado para el diseño completo |
| Al menos 90 % del total de casos ejecutados | 17 de 25 casos del diseño fueron automatizados; 68 % del diseño | No cumplido |
| 0 defectos críticos abiertos | 0 críticos abiertos | Cumplido |
| Mínimo 15 casos automatizados | 17 automatizados | Cumplido |
| Al menos 90 % de los casos ejecutados aprobados | 13/17 = 76.47 % en la suite evaluable | No cumplido |
| Todo defecto trazable | Cada defecto tiene caso y requisito | Cumplido |

## 8. Conclusión técnica

La auditoría demuestra trazabilidad documental completa y supera el mínimo de automatización con 17 pruebas. La regresión ejecutó 50 pruebas y obtuvo 46 aprobadas. Sin embargo, la versión auditada no cumple todos los criterios de salida: la suite evaluable aprobó 76.47 %, existen cuatro defectos abiertos y ocho de los 25 casos diseñados permanecen sin ejecución automatizada. Los riesgos principales son la aceptación de duplicados y nombres de producto inválidos, además de las diferencias entre el contrato y los métodos, campos y códigos HTTP implementados. Se requiere corregir los defectos, realizar retest y ejecutar una nueva regresión antes de declarar la versión apta para liberación.

## Referencias

[1]: ../auditoria-evaluable-evidence.txt "Evidencia de suite evaluable"
[2]: ../auditoria-regression-evidence.txt "Evidencia de regresión completa"
[3]: ./registro-defectos.md "Registro de defectos"
[4]: ./matriz-trazabilidad.md "Matriz de trazabilidad"
[5]: /home/ubuntu/upload/Mini_Proyecto_Evaluable_Modulo_IV_Auditoria_Pruebas.pdf "Guía del mini-proyecto evaluable"
