# Casos de prueba

## CP001 — Crear producto correctamente

**Tipo:** Positiva  
**Requisito:** RF03  
**Prioridad:** Alta  
**Precondición:** La API está disponible y se puede enviar un producto válido.  
**Datos:**

```json
{"name":"Mouse Gamer","category":"Laptops","price":120.0,"stock":5,"available":true}
```

**Pasos:**

1. Ejecutar `POST /products`.
2. Enviar el JSON indicado.
3. Revisar la respuesta.

**Resultado esperado:** HTTP `201`; el producto se crea, contiene un ID y conserva los datos enviados.

## CP002 — Consultar productos

**Tipo:** Positiva  
**Requisito:** RF01  
**Prioridad:** Media  
**Precondición:** El fixture contiene cinco productos.  
**Datos:** No aplica.  
**Pasos:**

1. Ejecutar `GET /products/`.
2. Revisar el código y el cuerpo de respuesta.

**Resultado esperado:** HTTP `200`; se devuelve una lista con cinco productos.

## CP003 — Consultar producto por ID

**Tipo:** Positiva  
**Requisito:** RF02  
**Prioridad:** Alta  
**Precondición:** Existe el producto con ID `1`.  
**Datos:** `product_id=1`.  
**Pasos:**

1. Ejecutar `GET /products/1`.
2. Revisar la respuesta.

**Resultado esperado:** HTTP `200`; el producto devuelto tiene `id=1`.

## CP004 — Crear categoría correctamente

**Tipo:** Positiva  
**Requisito:** RF08  
**Prioridad:** Media  
**Precondición:** La API está disponible.  
**Datos:**

```json
{"name":"Tablets","description":"Dispositivos táctiles","active":true}
```

**Pasos:**

1. Ejecutar `POST /categories`.
2. Enviar el JSON indicado.
3. Revisar la respuesta.

**Resultado esperado:** HTTP `201`; la categoría se crea con un ID generado.

## CP005 — Rechazar producto inexistente

**Tipo:** Negativa  
**Requisito:** RF02, RN06  
**Prioridad:** Alta  
**Precondición:** No existe el producto `999`.  
**Datos:** `product_id=999`.  
**Pasos:**

1. Ejecutar `GET /products/999`.
2. Revisar la respuesta.

**Resultado esperado:** HTTP `404`; el cuerpo es `{"detail":"Product not found"}`.

## CP006 — Rechazar categoría inexistente

**Tipo:** Negativa  
**Requisito:** RF07, RN06  
**Prioridad:** Alta  
**Precondición:** No existe la categoría `999`.  
**Datos:** `category_id=999`.  
**Pasos:**

1. Ejecutar `GET /categories/999`.
2. Revisar la respuesta.

**Resultado esperado:** HTTP `404`; el cuerpo es `{"detail":"Category not found"}`.

## CP007 — Rechazar nombre de categoría corto

**Tipo:** Negativa  
**Requisito:** RF08, RN02  
**Prioridad:** Alta  
**Precondición:** La API está disponible.  
**Datos:** `{"name":"AB"}`.  
**Pasos:**

1. Ejecutar `POST /categories`.
2. Enviar el JSON indicado.
3. Revisar la respuesta.

**Resultado esperado:** HTTP `422`; la categoría no se crea.

## CP008 — Rechazar ID no numérico

**Tipo:** Negativa  
**Requisito:** RN07  
**Prioridad:** Alta  
**Precondición:** La API está disponible.  
**Datos:** `category_id=abc`.  
**Pasos:**

1. Ejecutar `GET /categories/abc`.
2. Revisar la respuesta.

**Resultado esperado:** HTTP `422`; FastAPI rechaza el parámetro de ruta.

## CP009 — Aceptar stock igual a cero

**Tipo:** Frontera  
**Requisito:** RF03, RN04  
**Prioridad:** Alta  
**Precondición:** La API está disponible.  
**Datos:** Producto válido con `price=10.0` y `stock=0`.

```json
{"name":"Producto sin existencias","category":"Laptops","price":10.0,"stock":0,"available":false}
```

**Pasos:**

1. Ejecutar `POST /products`.
2. Enviar el JSON indicado.
3. Revisar la respuesta.

**Resultado esperado:** HTTP `201`; el producto se acepta porque el stock cero es el límite inferior permitido.

## CP010 — Rechazar stock negativo

**Tipo:** Frontera  
**Requisito:** RF03, RN04  
**Prioridad:** Alta  
**Precondición:** La API está disponible.  
**Datos:** Producto válido con `stock=-1`.

```json
{"name":"Producto inválido","category":"Laptops","price":10.0,"stock":-1,"available":false}
```

**Pasos:**

1. Ejecutar `POST /products`.
2. Enviar el JSON indicado.
3. Revisar la respuesta.

**Resultado esperado:** HTTP `422`; el producto no se crea porque el stock no puede ser negativo.

## Resumen

| Tipo | Casos | Total |
|---|---|---:|
| Positivos | CP001, CP002, CP003, CP004 | 4 |
| Negativos | CP005, CP006, CP007, CP008 | 4 |
| Frontera | CP009, CP010 | 2 |
| **Total** | **CP001–CP010** | **10** |

## Referencias

[1]: ../tests/test_modulo_iv.py "Automatización de los casos del Módulo IV"
[2]: /home/ubuntu/upload/Guia_Modulo_IV_Plan_Pruebas.pdf "Guía del aprendiz: Plan y documentación de pruebas"
