# Urban Routes — Suite de Automatización E2E con Selenium 🚕

Proyecto de automatización de pruebas End-to-End para **Urban Routes**, una aplicación web de solicitud de transporte y taxis que integra configuración de rutas, selección de tarifas, métodos de pago y confirmación de conductor en tiempo real.

La suite automatiza el flujo crítico de negocio para validar la estabilidad de la plataforma mediante pruebas de regresión ágiles e independientes.

**Stack Tecnológico:** Python 3.11 · Selenium WebDriver · Pytest · Page Object Model (POM) · Chrome/Edge WebDriver · CDP Logs

---

## Contexto del Proyecto 📝

El proceso de reserva en *Urban Routes* involucra interacciones complejas entre múltiples componentes dinámicos de UI, validaciones de formularios y autenticación mediante código SMS (interceptado dinámicamente mediante logs de protocolo **CDP - Chrome DevTools Protocol**).

La ejecución manual de esta regresión consumía aproximadamente 38 minutos por ciclo. Con la implementación del patrón **Page Object Model en 3 capas**, se logró aislar la lógica de UI de los datos de prueba, maximizando el mantenimiento, la reutilización del código y reduciendo drásticamente el tiempo de ejecución.

> ⚡ **Resultado Clave:** Reducción del **97% en el tiempo de regresión** (de ~38 minutos manuales a menos de 1 minuto automatizado).

---

## Arquitectura del Proyecto (POM - 3 Capas) 🛠️

El proyecto sigue una estructura modular limpia para garantizar la mantenibilidad y escalabilidad del código:

| Archivo / Módulo | Responsabilidad |
| :--- | :--- |
| `pages.py` | Localizadores (XPath/CSS) y acciones por página (capa de UI). |
| `helpers.py` | Lógica reutilizable y utilidades (p. ej. captura de código SMS vía CDP). |
| `data.py` | Datos de prueba: direcciones, tarjetas de crédito, mensajes. |
| `test_main.py` | Casos de prueba E2E organizados con Pytest y aserciones. |

---

## Cobertura del Flujo E2E (8 Pasos) ✅

1. **Definición de Ruta:** Configurar dirección de origen y destino.
2. **Selección de Tarifa:** Elección de la tarifa *Comfort*.
3. **Registro Telefónico:** Ingreso de número de celular.
4. **Verificación SMS:** Captura e intercepción del código de confirmación vía CDP.
5. **Método de Pago:** Inserción y confirmación de tarjeta de crédito.
6. **Notas al Conductor:** Adición de mensaje personalizado al conductor.
7. **Servicios Adicionales:** Activación de opciones complementarias (manta y pañuelos).
8. **Confirmación:** Solicitud del servicio y verificación del modal de asignación de conductor.

---

## Métricas y Resultados 📊

| Métrica | Valor |
| :--- | :--- |
| **Casos automatizados** | 8 pasos en el flujo E2E crítico |
| **Tiempo de ejecución manual** | ~38 minutos |
| **Tiempo de ejecución automatizado** | < 1 minuto |
| **Optimización de tiempo** | **97%** |
| **Efectividad del test suite** | Cobertura completa del flujo principal |

---

## Instalación y Ejecución🚦

1. **Clonar el repositorio:** git clone https://github.com/kdtrujillor-gif/qa-project-Urban-Routes-es
2. **Instalar dependencias:** pip install -r
3. **Verificar** que Edge WebDriver está en la ruta configurada en main.py
4. **Ejecutar las pruebas:** pytest test_main.py  
