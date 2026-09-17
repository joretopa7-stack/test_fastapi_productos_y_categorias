# Matriz de trazabilidad

La matriz conserva los IDs del contrato de TechStore y relaciona cada requisito o regla con al menos un caso diseñado.

| ID | Descripción corta | Caso(s) | Estado de cobertura |
|---|---|---|---|
| RF01 | Crear categoría válida | CP-CAT-01 | Cubierto |
| RF02 | Listar categorías | CP-CAT-02 | Cubierto |
| RF03 | Consultar categoría existente | CP-CAT-03 | Cubierto |
| RF04 | Consultar categoría inexistente con 404 | CP-CAT-04 | Cubierto |
| RF05 | Crear producto válido asociado | CP-PROD-01 | Cubierto |
| RF06 | Listar productos | CP-PROD-02 | Cubierto |
| RF07 | Consultar producto existente | CP-PROD-03 | Cubierto |
| RF08 | Consultar producto inexistente con 404 | CP-PROD-04 | Cubierto |
| RF09 | Actualizar producto válido | CP-PROD-05 | Cubierto; defecto de método PUT/PATCH |
| RF10 | Actualizar producto inexistente con 404 | CP-PROD-06 | Cubierto; no ejecutado |
| RF11 | Eliminar producto existente | CP-PROD-07 | Cubierto; defecto de código 200/204 |
| RF12 | Eliminar producto inexistente con 404 | CP-PROD-08 | Cubierto; no ejecutado |
| RN01 | Nombre de categoría obligatorio y de 3 a 60 caracteres | CP-CAT-05, CP-CAT-06 | Cubierto |
| RN02 | Nombre de categoría no duplicado, sin distinguir mayúsculas | CP-CAT-07 | Cubierto; incumplimiento observado |
| RN03 | Nombre de producto obligatorio y de 3 a 80 caracteres | CP-PROD-09, CP-PROD-10 | Cubierto |
| RN04 | Precio estrictamente mayor que 0 | CP-PROD-11, CP-PROD-12, CP-PROD-13 | Cubierto; no ejecutado |
| RN05 | Stock mayor o igual que 0 | CP-PROD-14, CP-PROD-15 | Cubierto |
| RN06 | `category_id` debe existir | CP-PROD-16, CP-PROD-18 | Cubierto; diferencia de contrato |
| RN07 | Stock igual a 0 debe aceptarse | CP-PROD-14 | Cubierto |
| RN08 | Actualización conserva validaciones de creación | CP-PROD-17, CP-PROD-18 | Cubierto; no ejecutado |

## Relación con automatización

| Archivo | Casos automatizados |
|---|---|
| `tests/test_auditoria_evaluable.py` | CP-CAT-01 a CP-CAT-07; CP-PROD-01, 02, 03, 04, 05, 07, 09, 10, 14 y 15 |
| `tests/test_categories.py` | Pruebas adicionales de categorías existentes |
| `tests/test_products.py` | Pruebas adicionales de productos existentes |

## Verificación

La cobertura documental es del 100 %: los 12 requisitos funcionales y las 8 reglas de negocio tienen al menos un caso relacionado. La cobertura de ejecución del diseño completo es parcial porque diez casos de producto requieren adaptar la implementación al contrato antes de ejecutarse de forma válida.

## Referencias

[1]: ./plan-pruebas.md "Plan de pruebas"
[2]: ./casos-prueba.md "Casos de prueba"
[3]: ../tests/test_auditoria_evaluable.py "Suite automatizada de auditoría"
[4]: /home/ubuntu/upload/Mini_Proyecto_Evaluable_Modulo_IV_Auditoria_Pruebas.pdf "Guía evaluable"
