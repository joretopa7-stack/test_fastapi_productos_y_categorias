# Casos de prueba

Los casos se diseñaron contra el contrato de TechStore API de la guía evaluable. `PASSED`, `FAILED`, `BLOCKED` y `NOT EXECUTED` se refieren a la ejecución de la auditoría documentada.

## Etapa A — Categorías

### CP-CAT-01 — Crear categoría válida

- **Requisito/regla:** RF01.
- **Prioridad:** Alta.
- **Precondiciones:** API disponible.
- **Datos de prueba:** `POST /categories`, `{"name":"Periféricos"}`.
- **Pasos:** 1. Enviar la solicitud. 2. Revisar código y JSON.
- **Resultado esperado:** HTTP 201 y objeto creado.
- **Resultado obtenido:** HTTP 201 y categoría creada.
- **Estado:** PASSED.
- **Automatización:** `test_cp_cat_01_create_category_valid`.

### CP-CAT-02 — Listar categorías

- **Requisito/regla:** RF02.
- **Prioridad:** Media.
- **Precondiciones:** Existe al menos una categoría.
- **Datos de prueba:** `GET /categories`.
- **Pasos:** 1. Ejecutar GET. 2. Verificar que la respuesta sea una lista.
- **Resultado esperado:** HTTP 200 y lista de categorías.
- **Resultado obtenido:** HTTP 200 y lista.
- **Estado:** PASSED.
- **Automatización:** `test_cp_cat_02_list_categories`.

### CP-CAT-03 — Consultar categoría existente

- **Requisito/regla:** RF03.
- **Prioridad:** Alta.
- **Precondiciones:** Existe categoría con ID 1.
- **Datos de prueba:** `GET /categories/1`.
- **Pasos:** 1. Ejecutar GET. 2. Revisar el ID devuelto.
- **Resultado esperado:** HTTP 200 y categoría con ID 1.
- **Resultado obtenido:** HTTP 200 y categoría con ID 1.
- **Estado:** PASSED.
- **Automatización:** `test_cp_cat_03_get_existing_category`.

### CP-CAT-04 — Consultar categoría inexistente

- **Requisito/regla:** RF04.
- **Prioridad:** Alta.
- **Precondiciones:** No existe el ID 99999.
- **Datos de prueba:** `GET /categories/99999`.
- **Pasos:** 1. Ejecutar GET. 2. Revisar el código.
- **Resultado esperado:** HTTP 404.
- **Resultado obtenido:** HTTP 404.
- **Estado:** PASSED.
- **Automatización:** `test_cp_cat_04_get_unknown_category_404`.

### CP-CAT-05 — Rechazar nombre menor a tres caracteres

- **Requisito/regla:** RN01.
- **Prioridad:** Alta.
- **Precondiciones:** API disponible.
- **Datos de prueba:** `{"name":"AB"}`.
- **Pasos:** 1. Enviar POST. 2. Revisar el código.
- **Resultado esperado:** HTTP 422.
- **Resultado obtenido:** HTTP 422.
- **Estado:** PASSED.
- **Automatización:** `test_cp_cat_05_category_name_too_short`.

### CP-CAT-06 — Aceptar nombre de exactamente tres caracteres

- **Requisito/regla:** RN01.
- **Prioridad:** Media.
- **Precondiciones:** API disponible.
- **Datos de prueba:** `{"name":"ABC"}`.
- **Pasos:** 1. Enviar POST. 2. Revisar la respuesta.
- **Resultado esperado:** HTTP 201.
- **Resultado obtenido:** HTTP 201.
- **Estado:** PASSED.
- **Automatización:** `test_cp_cat_06_category_name_exactly_three_characters`.

### CP-CAT-07 — Rechazar categoría duplicada ignorando mayúsculas

- **Requisito/regla:** RN02.
- **Prioridad:** Alta.
- **Precondiciones:** Existe una categoría `Audio`.
- **Datos de prueba:** Crear `Audio` y luego `audio`.
- **Pasos:** 1. Crear Audio. 2. Crear audio. 3. Revisar la segunda respuesta.
- **Resultado esperado:** HTTP 409.
- **Resultado obtenido:** HTTP 201; la implementación permite el duplicado.
- **Estado:** FAILED.
- **Automatización:** `test_cp_cat_07_duplicate_category_observed_behavior`.
- **Defecto:** DEF-CAT-001.

## Etapa B — Productos

### CP-PROD-01 — Crear producto válido

- **Requisito/regla:** RF05.
- **Prioridad:** Alta.
- **Precondiciones:** Existe categoría válida según el contrato.
- **Datos de prueba:** `name=Mouse inalámbrico`, `price=120000`, `stock=5`, `category_id=1`.
- **Pasos:** 1. Ejecutar POST `/products`. 2. Enviar JSON. 3. Revisar código.
- **Resultado esperado:** HTTP 201 y producto asociado a categoría.
- **Resultado obtenido:** No ejecutado contra el JSON contractual; la implementación usa `category` textual.
- **Estado:** NOT EXECUTED.

### CP-PROD-02 — Listar productos

- **Requisito/regla:** RF06.
- **Prioridad:** Media.
- **Precondiciones:** Existen productos.
- **Datos de prueba:** `GET /products`.
- **Pasos:** Ejecutar GET y revisar lista.
- **Resultado esperado:** HTTP 200 y lista.
- **Resultado obtenido:** HTTP 200 usando `/products/` con barra final.
- **Estado:** FAILED.
- **Defecto:** DEF-PROD-001.

### CP-PROD-03 — Consultar producto existente

- **Requisito/regla:** RF07.
- **Prioridad:** Alta.
- **Precondiciones:** Existe producto ID 1.
- **Datos de prueba:** `GET /products/1`.
- **Pasos:** Ejecutar GET y revisar ID.
- **Resultado esperado:** HTTP 200 y producto ID 1.
- **Resultado obtenido:** HTTP 200 y producto ID 1.
- **Estado:** PASSED.

### CP-PROD-04 — Consultar producto inexistente

- **Requisito/regla:** RF08.
- **Prioridad:** Alta.
- **Precondiciones:** No existe ID 99999.
- **Datos de prueba:** `GET /products/99999`.
- **Pasos:** Ejecutar GET y revisar código.
- **Resultado esperado:** HTTP 404.
- **Resultado obtenido:** HTTP 404.
- **Estado:** PASSED.
- **Automatización:** `test_cp_prod_04_get_unknown_product_404`.

### CP-PROD-05 — Actualizar producto válido

- **Requisito/regla:** RF09.
- **Prioridad:** Alta.
- **Precondiciones:** Existe producto ID 1.
- **Datos de prueba:** `PUT /products/1` con precio válido.
- **Pasos:** Ejecutar PUT y consultar el producto.
- **Resultado esperado:** HTTP 200 y datos actualizados.
- **Resultado obtenido:** El endpoint PUT no está implementado; la implementación expone PATCH.
- **Estado:** FAILED.
- **Defecto:** DEF-PROD-002.

### CP-PROD-06 — Actualizar producto inexistente

- **Requisito/regla:** RF10.
- **Prioridad:** Alta.
- **Precondiciones:** No existe ID 99999.
- **Datos de prueba:** `PUT /products/99999`.
- **Pasos:** Ejecutar PUT y revisar código.
- **Resultado esperado:** HTTP 404.
- **Resultado obtenido:** No ejecutado con el método contractual.
- **Estado:** NOT EXECUTED.

### CP-PROD-07 — Eliminar producto existente

- **Requisito/regla:** RF11.
- **Prioridad:** Alta.
- **Precondiciones:** Existe un producto creado para la prueba.
- **Datos de prueba:** `DELETE /products/{id}`.
- **Pasos:** Ejecutar DELETE y consultar el ID.
- **Resultado esperado:** HTTP 204; el producto queda eliminado.
- **Resultado obtenido:** HTTP 200 con el producto eliminado.
- **Estado:** FAILED.
- **Defecto:** DEF-PROD-003.

### CP-PROD-08 — Eliminar producto inexistente

- **Requisito/regla:** RF12.
- **Prioridad:** Alta.
- **Precondiciones:** No existe ID 99999.
- **Datos de prueba:** `DELETE /products/99999`.
- **Pasos:** Ejecutar DELETE y revisar código.
- **Resultado esperado:** HTTP 404.
- **Resultado obtenido:** No ejecutado en la suite evaluable.
- **Estado:** NOT EXECUTED.

### CP-PROD-09 — Rechazar nombre menor a tres caracteres

- **Requisito/regla:** RN03.
- **Prioridad:** Alta.
- **Precondiciones:** API disponible.
- **Datos de prueba:** Producto con `name=AB`.
- **Pasos:** Ejecutar POST `/products`.
- **Resultado esperado:** HTTP 422.
- **Resultado obtenido:** HTTP 201; la implementación acepta el nombre de dos caracteres.
- **Estado:** FAILED.
- **Defecto:** DEF-PROD-001.
- **Automatización:** `test_cp_prod_09_product_name_too_short`.

### CP-PROD-10 — Aceptar nombre exactamente de tres caracteres

- **Requisito/regla:** RN03.
- **Prioridad:** Media.
- **Precondiciones:** API disponible.
- **Datos de prueba:** Producto con `name=ABC`.
- **Pasos:** Ejecutar POST `/products`.
- **Resultado esperado:** HTTP 201.
- **Resultado obtenido:** HTTP 201.
- **Estado:** PASSED.
- **Automatización:** `test_cp_prod_10_product_name_exactly_three_characters`.

### CP-PROD-11 — Rechazar precio igual a cero

- **Requisito/regla:** RN04.
- **Prioridad:** Alta.
- **Precondiciones:** API disponible.
- **Datos de prueba:** Producto con `price=0`.
- **Pasos:** Ejecutar POST `/products`.
- **Resultado esperado:** HTTP 422.
- **Resultado obtenido:** No ejecutado.
- **Estado:** NOT EXECUTED.

### CP-PROD-12 — Rechazar precio negativo

- **Requisito/regla:** RN04.
- **Prioridad:** Alta.
- **Precondiciones:** API disponible.
- **Datos de prueba:** Producto con `price=-1000`.
- **Pasos:** Ejecutar POST `/products`.
- **Resultado esperado:** HTTP 422.
- **Resultado obtenido:** No ejecutado.
- **Estado:** NOT EXECUTED.

### CP-PROD-13 — Aceptar precio mínimo positivo

- **Requisito/regla:** RN04.
- **Prioridad:** Media.
- **Precondiciones:** API disponible.
- **Datos de prueba:** Producto con `price=0.01`.
- **Pasos:** Ejecutar POST `/products`.
- **Resultado esperado:** HTTP 201.
- **Resultado obtenido:** No ejecutado.
- **Estado:** NOT EXECUTED.

### CP-PROD-14 — Aceptar stock igual a cero

- **Requisito/regla:** RN05, RN07.
- **Prioridad:** Alta.
- **Precondiciones:** API disponible.
- **Datos de prueba:** Producto Monitor, `price=850000`, `stock=0`.
- **Pasos:** Ejecutar POST `/products` y revisar stock.
- **Resultado esperado:** HTTP 201; stock cero aceptado.
- **Resultado obtenido:** HTTP 201; stock cero aceptado.
- **Estado:** PASSED.
- **Automatización:** `test_cp_prod_14_stock_zero_is_accepted`.

### CP-PROD-15 — Rechazar stock negativo

- **Requisito/regla:** RN05.
- **Prioridad:** Alta.
- **Precondiciones:** API disponible.
- **Datos de prueba:** Producto con `stock=-1`.
- **Pasos:** Ejecutar POST `/products`.
- **Resultado esperado:** HTTP 422.
- **Resultado obtenido:** HTTP 422.
- **Estado:** PASSED.
- **Automatización:** `test_cp_prod_15_negative_stock_is_rejected`.

### CP-PROD-16 — Rechazar categoría inexistente al crear

- **Requisito/regla:** RN06.
- **Prioridad:** Alta.
- **Precondiciones:** No existe `category_id=99999`.
- **Datos de prueba:** Producto con `category_id=99999`.
- **Pasos:** Ejecutar POST `/products`.
- **Resultado esperado:** HTTP 404.
- **Resultado obtenido:** El esquema actual no usa `category_id`; no ejecutado contra el contrato.
- **Estado:** NOT EXECUTED.

### CP-PROD-17 — Rechazar precio inválido al actualizar

- **Requisito/regla:** RN08.
- **Prioridad:** Alta.
- **Precondiciones:** Existe producto ID 1.
- **Datos de prueba:** Actualización con `price=0`.
- **Pasos:** Ejecutar PUT `/products/1`.
- **Resultado esperado:** HTTP 422.
- **Resultado obtenido:** No ejecutado con el método contractual.
- **Estado:** NOT EXECUTED.

### CP-PROD-18 — Rechazar categoría inexistente al actualizar

- **Requisito/regla:** RN08, RN06.
- **Prioridad:** Alta.
- **Precondiciones:** Existe producto ID 1.
- **Datos de prueba:** Actualización con `category_id=99999`.
- **Pasos:** Ejecutar PUT `/products/1`.
- **Resultado esperado:** HTTP 404 o 422 según validación.
- **Resultado obtenido:** No ejecutado con el esquema contractual.
- **Estado:** NOT EXECUTED.

## Resumen

| Módulo | Casos diseñados | PASSED | FAILED | BLOCKED | NOT EXECUTED |
|---|---:|---:|---:|---:|---:|
| Categorías | 7 | 6 | 1 | 0 | 0 |
| Productos | 18 | 7 | 3 | 0 | 8 |
| **Total** | **25** | **13** | **4** | **0** | **8** |

## Referencias

[1]: ../app/main.py "Implementación auditada"
[2]: ../app/schemas.py "Esquemas auditados"
[3]: ../tests/test_auditoria_evaluable.py "Automatización trazable"
[4]: /home/ubuntu/upload/Mini_Proyecto_Evaluable_Modulo_IV_Auditoria_Pruebas.pdf "Guía del mini-proyecto evaluable"
