# Plan de pruebas

## 1. Identificación del proyecto

| Campo | Información |
|---|---|
| Proyecto | TechStore API — Products & Categories |
| Versión auditada | 1.0.0 |
| Aprendiz | Jorge Alejandro Torres Paez |
| Fecha de inicio | 17/09/2026 |
| Fecha de entrega | 17/09/2026 |
| Repositorio | `test_fastapi_productos_y_categorias` |
| Aplicación | `app.main:app` |

## 2. Objetivo de la auditoría

Determinar, mediante evidencia trazable, si la implementación de la API cumple el contrato funcional de TechStore para categorías y productos. La auditoría relaciona requisitos, riesgos, casos, automatización pytest, resultados observados, defectos, retest, regresión y criterios de salida.

## 3. Alcance

### Etapa A: Categorías

Se auditan RF01–RF04 y RN01–RN02 mediante `POST /categories`, `GET /categories` y `GET /categories/{id}`.

### Etapa B: Productos

Se auditan RF05–RF12 y RN03–RN08 mediante creación, consulta, actualización, eliminación y validaciones de productos.

### Endpoints contractuales

| ID | Método | Endpoint | Éxito esperado |
|---|---|---|---:|
| EP01 | POST | `/categories` | 201 |
| EP02 | GET | `/categories` | 200 |
| EP03 | GET | `/categories/{id}` | 200 |
| EP04 | POST | `/products` | 201 |
| EP05 | GET | `/products` | 200 |
| EP06 | GET | `/products/{id}` | 200 |
| EP07 | PUT | `/products/{id}` | 200 |
| EP08 | DELETE | `/products/{id}` | 204 |

### Diferencias observadas de implementación

La implementación usa `PATCH` para actualizar productos, `/products/` para listar productos y devuelve HTTP `200` con el producto eliminado. Además, usa `category` como texto en lugar de `category_id`. Estas diferencias se auditan contra el contrato de la guía y se registran como defectos o riesgos cuando corresponde.

### Fuera de alcance

Autenticación, rendimiento, carga, estrés, seguridad especializada, interfaz gráfica, despliegue productivo y persistencia externa.

## 4. Requisitos y reglas del contrato

| ID | Descripción |
|---|---|
| RF01 | Crear una categoría válida. |
| RF02 | Listar categorías registradas. |
| RF03 | Consultar una categoría existente por ID. |
| RF04 | Responder 404 al consultar categoría inexistente. |
| RF05 | Crear producto válido asociado a categoría existente. |
| RF06 | Listar productos registrados. |
| RF07 | Consultar producto existente por ID. |
| RF08 | Responder 404 al consultar producto inexistente. |
| RF09 | Actualizar producto existente con datos válidos. |
| RF10 | Responder 404 al actualizar producto inexistente. |
| RF11 | Eliminar producto existente. |
| RF12 | Responder 404 al eliminar producto inexistente. |
| RN01 | Nombre de categoría obligatorio, entre 3 y 60 caracteres. |
| RN02 | Nombre de categoría no repetido sin distinguir mayúsculas/minúsculas; respuesta 409. |
| RN03 | Nombre de producto obligatorio, entre 3 y 80 caracteres. |
| RN04 | Precio estrictamente mayor que 0. |
| RN05 | Stock mayor o igual que 0. |
| RN06 | `category_id` corresponde a categoría existente; si no, 404. |
| RN07 | Stock igual a 0 debe aceptarse. |
| RN08 | La actualización conserva las validaciones de creación. |

## 5. Riesgos

| ID | Riesgo | Probabilidad | Impacto | Prioridad | Casos mitigadores |
|---|---|---|---|---|---|
| R01 | Permitir categoría duplicada con diferente capitalización. | Media | Alto | Alta | CP-CAT-07 |
| R02 | Aceptar nombres menores al mínimo. | Alta | Medio | Alta | CP-CAT-05, CP-PROD-09 |
| R03 | Aceptar precio cero o negativo. | Media | Alto | Alta | CP-PROD-11, CP-PROD-12 |
| R04 | Aceptar stock negativo. | Media | Alto | Alta | CP-PROD-15 |
| R05 | No validar categoría inexistente. | Media | Alto | Alta | CP-PROD-16, CP-PROD-18 |
| R06 | Usar método o código HTTP diferente al contrato. | Alta | Alto | Crítica | CP-PROD-05, CP-PROD-07 |
| R07 | Consultar, actualizar o eliminar IDs inexistentes incorrectamente. | Media | Alto | Alta | CP-CAT-04, CP-PROD-04, CP-PROD-06, CP-PROD-08 |
| R08 | Contaminar datos entre pruebas. | Media | Alto | Alta | Fixture `reset_db` |

## 6. Estrategia

Se aplican pruebas funcionales positivas, negativas y de frontera. Los casos se diseñan antes de automatizarse. Se automatiza una selección representativa con pytest y TestClient, conservando el ID del caso en el nombre del test. Los fallos se clasifican primero como problema de prueba, datos, ambiente o defecto del producto.

## 7. Ambiente y herramientas

| Elemento | Configuración |
|---|---|
| Sistema operativo | Linux |
| Python | 3.12.3 |
| FastAPI | 0.141.1 |
| Pydantic | 2.13.5 |
| pytest | 9.1.1 |
| Cliente | `fastapi.testclient.TestClient` |
| Datos | Listas en memoria reiniciadas por fixture |
| Comando principal | `python -m pytest -v` |

El `requirements.txt` actual presenta un defecto de reproducibilidad: declara `truststore-0.10.4`, paquete que no pudo instalarse en el ambiente auditado. La evidencia se conserva en `install-evidence.txt`.

## 8. Datos de prueba

Categorías: `Periféricos`, `Audio`, `Computadores` y `Accesorios`.  
Producto válido: `Mouse inalámbrico`, precio `120000`, stock `5`.  
Producto frontera: `Monitor`, precio `850000`, stock `0`.  
ID inexistente: `99999`.  
Precio frontera inválido: `0`.  
Precio inválido: `-1000`.  
Stock inválido: `-1`.

## 9. Criterios de entrada

La API debe poder importarse, pytest debe recolectar las pruebas, TestClient debe inicializarse, los fixtures deben reiniciar el estado y el contrato RF/RN debe estar disponible.

## 10. Criterios de suspensión

Se suspende si la aplicación no importa, el ambiente no permite ejecutar pytest, los datos no se reinician o un defecto bloqueante impide ejecutar la mayoría de los casos críticos.

## 11. Criterios de reanudación

Se reanuda después de corregir la causa bloqueante, instalar la versión corregida, restablecer los datos y repetir el caso que provocó la suspensión.

## 12. Criterios de salida

- Cobertura documental del 100 % de RF01–RF12 y RN01–RN08.
- 100 % de casos críticos y al menos 90 % del total ejecutados.
- 0 defectos críticos abiertos.
- Mínimo 15 casos automatizados.
- Al menos 90 % de casos ejecutados aprobados.
- Todo defecto trazable a caso y requisito/regla.

## 13. Roles y responsables

El aprendiz responsable diseña casos, ejecuta pruebas, conserva evidencias, analiza fallos y actualiza los cinco documentos. La revisión final debe verificar que las métricas coincidan con la salida real de pytest.

## Referencias

[1]: ../app/main.py "Implementación real de TechStore API"
[2]: ../app/schemas.py "Esquemas Pydantic reales"
[3]: ../tests/conftest.py "Fixtures de pruebas"
[4]: /home/ubuntu/upload/Mini_Proyecto_Evaluable_Modulo_IV_Auditoria_Pruebas.pdf "Mini proyecto evaluable: Auditoría completa de pruebas"
