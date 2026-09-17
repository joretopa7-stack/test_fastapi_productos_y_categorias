# Registro de defectos

## DEF-001

**Título:** El archivo `requirements.txt` no permite instalar todas las dependencias declaradas.

**Severidad:** Media  
**Prioridad:** Alta  
**Endpoint:** No aplica; defecto de configuración del proyecto  
**Caso relacionado:** Criterio de entrada del plan  
**Requisito afectado:** Disponibilidad reproducible del ambiente de pruebas  
**Estado:** Abierto

**Precondición:** Python 3.x y un entorno virtual nuevo.

**Pasos para reproducir:**

1. Crear un entorno virtual con `python3 -m venv .venv`.
2. Activarlo.
3. Ejecutar `python -m pip install -r requirements.txt`.

**Resultado esperado:** Todas las dependencias declaradas se instalan correctamente y el ambiente queda listo para ejecutar pytest.

**Resultado obtenido:** La instalación falla porque no se encuentra `truststore-0.10.4` para el entorno disponible. Para ejecutar las pruebas fue necesario instalar manualmente las dependencias funcionales compatibles.

**Evidencia:** La ejecución de instalación devolvió `No matching distribution found for truststore-0.10.4`; se conserva en [`install-evidence.txt`](../install-evidence.txt).

**Causa probable:** Nombre o versión de paquete incorrectos en `requirements.txt`.

**Corrección aplicada:** No aplicada durante este ciclo.

**Retest:** Pendiente. Después de corregir `requirements.txt`, repetir la instalación desde un entorno virtual limpio y ejecutar `python -m pytest -v tests/test_modulo_iv.py`.

**Regresión:** Pendiente de la corrección. Ejecutar `python -m pytest -v` después del retest.

## Severidad y prioridad

La severidad es **media** porque el defecto no afecta directamente el comportamiento de los endpoints una vez instaladas las dependencias, pero impide reproducir el ambiente mediante el procedimiento documentado. La prioridad es **alta** porque bloquea la preparación normal del proyecto para otro aprendiz o integrante del equipo.

## Estado de la ejecución funcional

No se confirmaron defectos funcionales en los diez casos del Módulo IV: los diez casos pasaron. El defecto DEF-001 corresponde al ambiente de instalación y permanece abierto.

## Referencias

[1]: ../requirements.txt "Dependencias declaradas del proyecto"
[2]: ../modulo-iv-evidence.txt "Evidencia de ejecución de los 10 casos"
[3]: ../pytest-evidence-final.txt "Evidencia de regresión"
[4]: /home/ubuntu/upload/Guia_Modulo_IV_Plan_Pruebas.pdf "Guía del aprendiz: Plan y documentación de pruebas"
