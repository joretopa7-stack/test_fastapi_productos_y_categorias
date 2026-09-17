# Matriz de trazabilidad

## 1. Relación requisito–caso de prueba

| ID requisito | Requisito / regla | Caso(s) relacionado(s) |
|---|---|---|
| RF01 | Consultar productos | CP002 |
| RF02 | Consultar producto por ID | CP003, CP005 |
| RF03 | Crear producto | CP001, CP009, CP010 |
| RF04 | Actualizar parcialmente un producto | No cubierto por los 10 casos del Módulo IV |
| RF05 | Eliminar un producto | No cubierto por los 10 casos del Módulo IV |
| RF06 | Consultar categorías | No cubierto por los 10 casos del Módulo IV |
| RF07 | Consultar categoría por ID | CP006 |
| RF08 | Crear categoría | CP004, CP007 |
| RF09 | Actualizar parcialmente una categoría | No cubierto por los 10 casos del Módulo IV |
| RF10 | Eliminar una categoría | No cubierto por los 10 casos del Módulo IV |
| RN01 | Nombre del producto entre 2 y 100 caracteres | No cubierto explícitamente |
| RN02 | Nombre de la categoría entre 3 y 50 caracteres | CP007 |
| RN03 | Precio mayor que cero | No cubierto explícitamente |
| RN04 | Stock mayor o igual que cero | CP009, CP010 |
| RN05 | Campos obligatorios presentes | CP001, CP004 |
| RN06 | Recurso inexistente no se devuelve como válido | CP005, CP006 |
| RN07 | ID no numérico responde HTTP 422 | CP008 |

## 2. Relación caso–prueba automatizada

| Caso | Test automatizado |
|---|---|
| CP001 | `test_cp001_create_product_valid` |
| CP002 | `test_cp002_list_products` |
| CP003 | `test_cp003_get_existing_product` |
| CP004 | `test_cp004_create_category_valid` |
| CP005 | `test_cp005_get_non_existing_product` |
| CP006 | `test_cp006_get_non_existing_category` |
| CP007 | `test_cp007_reject_category_name_too_short` |
| CP008 | `test_cp008_reject_non_numeric_category_id` |
| CP009 | `test_cp009_accept_product_with_zero_stock` |
| CP010 | `test_cp010_reject_product_with_negative_stock` |

## 3. Revisión de huecos de cobertura

La matriz demuestra la cobertura de los diez casos seleccionados para el Módulo IV. Los requisitos RF04, RF05, RF06, RF09 y RF10 pertenecen al alcance general de la API, pero no forman parte de los diez casos mínimos de esta actividad. También deberán añadirse casos específicos para RN01 y RN03 si se requiere cobertura completa de todas las validaciones Pydantic.

## Referencias

[1]: ./plan-pruebas.md "Plan de pruebas"
[2]: ../tests/test_modulo_iv.py "Tests automatizados del Módulo IV"
[3]: /home/ubuntu/upload/Guia_Modulo_IV_Plan_Pruebas.pdf "Guía del aprendiz: Plan y documentación de pruebas"
