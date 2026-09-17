# Registro de defectos

La guía indica registrar defectos reales y no inventarlos. Los siguientes defectos se confirmaron comparando el comportamiento observado con el contrato evaluable y con la salida de pytest.

## DEF-CAT-001

**Título:** La API permite crear categorías duplicadas ignorando la regla de mayúsculas y minúsculas.  
**Requisito/regla:** RN02.  
**Caso relacionado:** CP-CAT-07.  
**Severidad:** Alta.  
**Prioridad:** Alta.  
**Estado:** Abierto.  
**Ambiente/versión:** Python 3.12.3, FastAPI 0.141.1, versión 1.0.0.

### Precondición

La API está disponible y el fixture reinicia la lista de categorías.

### Pasos para reproducir

1. Ejecutar `POST /categories` con `{"name":"Audio"}`.
2. Ejecutar nuevamente `POST /categories` con `{"name":"audio"}`.
3. Revisar la segunda respuesta.

### Resultado esperado

HTTP `409`, porque el nombre duplicado debe rechazarse sin distinguir mayúsculas de minúsculas.

### Resultado obtenido

HTTP `201`; la implementación crea la segunda categoría.

### Evidencia

`tests/test_auditoria_evaluable.py::test_cp_cat_07_duplicate_category_observed_behavior` falló con `assert 201 == 409`.

### Retest y regresión

No aplica todavía. No se ha aplicado una corrección. Cuando se corrija, debe ejecutarse primero `pytest -v -k cp_cat_07` y luego `pytest -v`.

## DEF-PROD-001

**Título:** La API acepta nombres de producto menores a tres caracteres.  
**Requisito/regla:** RN03.  
**Caso relacionado:** CP-PROD-09.  
**Severidad:** Alta.  
**Prioridad:** Alta.  
**Estado:** Abierto.  
**Ambiente/versión:** Python 3.12.3, FastAPI 0.141.1, versión 1.0.0.

### Precondición

La API está disponible.

### Pasos para reproducir

1. Ejecutar `POST /products`.
2. Enviar un producto con `name=AB`, `price=10` y `stock=1`.
3. Revisar la respuesta.

### Resultado esperado

HTTP `422`, porque el nombre debe tener entre 3 y 80 caracteres.

### Resultado obtenido

HTTP `201`; el producto se crea con un nombre de dos caracteres.

### Evidencia

`tests/test_auditoria_evaluable.py::test_cp_prod_09_product_name_too_short` falló con `assert 201 == 422`.

### Retest y regresión

No aplica todavía. No se ha aplicado una corrección. Cuando se corrija, debe ejecutarse `pytest -v -k cp_prod_09` y luego `pytest -v`.

## DEF-PROD-002

**Título:** La actualización de productos no expone el método contractual PUT.  
**Requisito/regla:** RF09 y RN08.  
**Caso relacionado:** CP-PROD-05, CP-PROD-06, CP-PROD-17 y CP-PROD-18.  
**Severidad:** Alta.  
**Prioridad:** Alta.  
**Estado:** Abierto.  
**Ambiente/versión:** Python 3.12.3, FastAPI 0.141.1, versión 1.0.0.

### Pasos para reproducir

1. Ejecutar `PUT /products/1` con un cuerpo válido.
2. Revisar la respuesta y la documentación de rutas.

### Resultado esperado

HTTP `200` y producto actualizado mediante PUT.

### Resultado obtenido

La implementación declara `PATCH /products/{product_id}` y no declara PUT.

### Evidencia

La ruta está implementada como `@app.patch("/products/{product_id}")` en `app/main.py`.

### Retest y regresión

Pendientes de una corrección. Después de corregir, ejecutar CP-PROD-05, los casos de actualización inválida y la suite completa.

## DEF-PROD-003

**Título:** La eliminación de productos devuelve HTTP 200 en lugar de HTTP 204.  
**Requisito/regla:** RF11.  
**Caso relacionado:** CP-PROD-07.  
**Severidad:** Media.  
**Prioridad:** Alta.  
**Estado:** Abierto.  
**Ambiente/versión:** Python 3.12.3, FastAPI 0.141.1, versión 1.0.0.

### Pasos para reproducir

1. Crear un producto.
2. Ejecutar `DELETE /products/{id}`.
3. Revisar el código HTTP.

### Resultado esperado

HTTP `204`.

### Resultado obtenido

HTTP `200` con el objeto eliminado.

### Evidencia

La implementación de `delete_product` devuelve el producto y no declara `status_code=204`; la prueba existente confirma HTTP 200.

### Retest y regresión

Pendientes de una corrección. Después de corregir, ejecutar CP-PROD-07 y la suite completa.

## Resumen de defectos

| Severidad | Abiertos | Defectos |
|---|---:|---|
| Crítica | 0 | — |
| Alta | 3 | DEF-CAT-001, DEF-PROD-001, DEF-PROD-002 |
| Media | 1 | DEF-PROD-003 |

## Referencias

[1]: ../tests/test_auditoria_evaluable.py "Pruebas de auditoría evaluable"
[2]: ../app/main.py "Implementación auditada"
[3]: ../app/schemas.py "Validaciones implementadas"
[4]: ../auditoria-evaluable-evidence.txt "Salida de pytest de la auditoría"
[5]: /home/ubuntu/upload/Mini_Proyecto_Evaluable_Modulo_IV_Auditoria_Pruebas.pdf "Guía evaluable"
