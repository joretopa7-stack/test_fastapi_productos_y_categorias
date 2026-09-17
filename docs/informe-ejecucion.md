# Informe de ejecución de pruebas

Proyecto: Product API — productos y categorías  
Versión: 1.0.0  
Fecha: 17/09/2026  
Responsable: Jorge Alejandro Torres Paez

## 1. Resumen

| Resultado | Cantidad |
|---|---:|
| Casos diseñados | 10 |
| Casos ejecutados | 10 |
| Aprobados | 10 |
| Fallidos | 0 |
| Bloqueados | 0 |

La ejecución corresponde a los diez casos definidos para el Módulo IV: cuatro positivos, cuatro negativos y dos de frontera.

## 2. Métricas

| Métrica | Fórmula | Resultado |
|---|---|---:|
| Tasa de aprobación | Casos aprobados / casos ejecutados × 100 | 10 / 10 × 100 = 100 % |
| Tasa de fallos | Casos fallidos / casos ejecutados × 100 | 0 / 10 × 100 = 0 % |
| Cobertura de ejecución | Casos ejecutados / casos diseñados × 100 | 10 / 10 × 100 = 100 % |

## 3. Distribución por tipo

| Tipo | Diseñados | Ejecutados | Aprobados | Fallidos |
|---|---:|---:|---:|---:|
| Positivos | 4 | 4 | 4 | 0 |
| Negativos | 4 | 4 | 4 | 0 |
| Frontera | 2 | 2 | 2 | 0 |
| **Total** | **10** | **10** | **10** | **0** |

## 4. Defectos relevantes

- **DEF-001:** El archivo `requirements.txt` no permite instalar todas las dependencias declaradas en un entorno nuevo. Severidad media, prioridad alta, estado abierto.

Este defecto no impidió la ejecución final porque se instaló un conjunto compatible de dependencias funcionales. Debe corregirse para que el procedimiento de instalación sea reproducible.

## 5. Comparación contra criterios de salida

| Criterio de salida | Resultado real | Estado |
|---|---|---|
| 100 % de casos críticos ejecutados | 10 de 10 | Cumplido |
| 0 defectos críticos abiertos | 0 defectos críticos | Cumplido |
| Al menos 95 % de casos aprobados | 100 % | Cumplido |
| Reglas de negocio críticas verificadas | RN02, RN04, RN06 y RN07 verificadas | Cumplido |
| Retest y regresión después de una corrección | No se corrigió DEF-001 durante el ciclo | Pendiente |

## 6. Regresión

Después de ejecutar el Módulo IV se ejecutó la suite completa:

- Casos ejecutados: 33.
- Casos aprobados: 33.
- Casos fallidos: 0.
- Casos bloqueados: 0.
- Tasa de aprobación: 100 %.

## 7. Conclusión técnica

Los diez casos del Módulo IV fueron ejecutados y aprobados. La tasa de aprobación fue del 100 % y la cobertura de ejecución fue del 100 %. Los criterios de salida funcionales se cumplen. El ciclo queda pendiente de cierre administrativo porque DEF-001 permanece abierto y requiere corrección, retest y regresión del procedimiento de instalación.

## Referencias

[1]: ../modulo-iv-evidence.txt "Evidencia de ejecución del Módulo IV"
[2]: ../pytest-evidence-final.txt "Evidencia de ejecución de regresión"
[3]: ./registro-defectos.md "Registro de defectos"
[4]: /home/ubuntu/upload/Guia_Modulo_IV_Plan_Pruebas.pdf "Guía del aprendiz: Plan y documentación de pruebas"
