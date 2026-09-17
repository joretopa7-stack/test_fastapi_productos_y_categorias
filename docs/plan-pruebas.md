# Plan de Pruebas

## 1. Información general

Proyecto: Product API — productos y categorías  
Versión: 1.0.0  
Tecnologías: Python, FastAPI, Pydantic, pytest, TestClient y Uvicorn  
Responsable de pruebas: Jorge Alejandro Torres Paez  
Fecha: 17/09/2026  
Persistencia: listas en memoria `products_db` y `category_db`  
Aplicación: `app.main:app`

## 2. Objetivo

Verificar que la API de productos y categorías cumpla los requisitos funcionales y las reglas de negocio establecidas, considerando entradas válidas, inválidas y casos límite. La ejecución se realizará mediante pruebas funcionales automatizadas con pytest y TestClient.

## 3. Alcance

### Incluido

- `GET /health` para comprobar el estado de la API.
- `GET /products/` para consultar productos.
- `GET /products/{product_id}` para consultar un producto por ID.
- `POST /products` para crear productos.
- `PATCH /products/{product_id}` para actualizar productos parcialmente.
- `DELETE /products/{product_id}` para eliminar productos.
- `GET /categories` para consultar y filtrar categorías.
- `GET /categories/{category_id}` para consultar una categoría por ID.
- `POST /categories` para crear categorías.
- `PATCH /categories/{category_id}` para actualizar categorías parcialmente.
- `DELETE /categories/{category_id}` para eliminar categorías.
- Códigos HTTP, estructura JSON y validaciones Pydantic.
- Filtros por `category`, `available`, `search` y `active`.

### Fuera de alcance

- Autenticación y autorización.
- Rendimiento, carga y estrés.
- Seguridad especializada.
- Interfaz gráfica.
- Despliegue en producción.
- Persistencia en una base de datos externa.

## 4. Requisitos y reglas de negocio

| ID | Tipo | Descripción |
|---|---|---|
| RF01 | Requisito funcional | Consultar productos. |
| RF02 | Requisito funcional | Consultar un producto por ID. |
| RF03 | Requisito funcional | Crear un producto. |
| RF04 | Requisito funcional | Actualizar parcialmente un producto. |
| RF05 | Requisito funcional | Eliminar un producto. |
| RF06 | Requisito funcional | Consultar categorías. |
| RF07 | Requisito funcional | Consultar una categoría por ID. |
| RF08 | Requisito funcional | Crear una categoría. |
| RF09 | Requisito funcional | Actualizar parcialmente una categoría. |
| RF10 | Requisito funcional | Eliminar una categoría. |
| RN01 | Regla de negocio | El nombre del producto debe tener entre 2 y 100 caracteres. |
| RN02 | Regla de negocio | El nombre de la categoría debe tener entre 3 y 50 caracteres. |
| RN03 | Regla de negocio | El precio debe ser mayor que cero. |
| RN04 | Regla de negocio | El stock no puede ser negativo. |
| RN05 | Regla de negocio | Los campos obligatorios no pueden omitirse. |
| RN06 | Regla de negocio | Un recurso inexistente debe responder HTTP 404. |
| RN07 | Regla de negocio | Un ID no numérico debe responder HTTP 422. |

## 5. Riesgos

| ID | Riesgo | Probabilidad | Impacto | Prioridad |
|---|---|---|---|---|
| R01 | Permitir stock negativo. | Media | Alto | Alta |
| R02 | Permitir precio cero o negativo. | Media | Alto | Alta |
| R03 | Consultar un recurso inexistente y obtener respuesta exitosa. | Alta | Medio | Alta |
| R04 | Aceptar nombres de categoría menores al mínimo. | Media | Medio | Media |
| R05 | Aceptar un ID no numérico. | Media | Medio | Alta |
| R06 | Contaminar datos entre casos de prueba. | Media | Alto | Alta |

## 6. Estrategia

Se realizarán pruebas funcionales, positivas, negativas y de frontera. Las verificaciones repetibles se automatizarán con pytest y TestClient.

La distribución principal exigida para este módulo es la siguiente:

| Tipo | Casos |
|---|---:|
| Positivos | 4 |
| Negativos | 4 |
| Frontera | 2 |
| Total | 10 |

Los casos se identifican como `CP001` a `CP010`. La regresión completa de la suite existente se ejecutará después de los diez casos del módulo.

## 7. Ambiente

Sistema operativo: Linux  
Lenguaje: Python 3.12.3  
Framework: FastAPI 0.141.1  
Servidor: Uvicorn 0.52.0  
Framework de pruebas: pytest 9.1.1  
Cliente HTTP: `fastapi.testclient.TestClient`  
Base de datos de pruebas: listas en memoria reiniciadas mediante `tests/conftest.py`

No se ejecutan pruebas destructivas contra producción. El fixture `reset_db` restaura los productos y las categorías antes de cada prueba.

## 8. Datos de prueba

| Escenario | Datos relevantes | Resultado esperado |
|---|---|---|
| Producto válido | `price=120.00`, `stock=5`, `category=Laptops` | Aceptado |
| Categoría válida | `name=Tablets`, `active=true` | Aceptada |
| Producto inexistente | `id=999` | HTTP 404 |
| Categoría inexistente | `id=999` | HTTP 404 |
| Categoría inválida | `name=AB` | HTTP 422 |
| ID inválido | `category_id=abc` | HTTP 422 |
| Stock frontera válido | `stock=0` | Aceptado |
| Stock frontera inválido | `stock=-1` | Rechazado |

## 9. Criterios de entrada

- La API puede importarse correctamente.
- Los endpoints del alcance están implementados.
- pytest está instalado.
- TestClient puede inicializarse.
- Existe un ambiente de pruebas aislado.
- Los fixtures reinician los datos antes de cada caso.

## 10. Criterios de suspensión

- La API no puede iniciar o importarse.
- TestClient no puede inicializarse.
- El ambiente de pruebas no está disponible.
- Los fixtures no pueden restablecer el estado.
- Existe un defecto bloqueante que impide ejecutar los casos críticos.

## 11. Criterios de reanudación

- El defecto bloqueante fue corregido.
- El ambiente está disponible nuevamente.
- La versión corregida fue instalada.
- Los datos de prueba fueron reiniciados.
- El caso que provocó la suspensión está listo para retest.

## 12. Criterios de salida

- 100 % de los casos del Módulo IV ejecutados.
- 0 defectos críticos abiertos.
- Al menos 95 % de casos aprobados.
- Reglas de negocio críticas verificadas.
- Retest y regresión ejecutados cuando exista una corrección.

## Referencias

[1]: ../app/main.py "Implementación de endpoints FastAPI"
[2]: ../app/schemas.py "Esquemas Pydantic"
[3]: ../tests/conftest.py "Fixtures del ambiente de pruebas"
[4]: /home/ubuntu/upload/Guia_Modulo_IV_Plan_Pruebas.pdf "Guía del aprendiz: Plan y documentación de pruebas"
