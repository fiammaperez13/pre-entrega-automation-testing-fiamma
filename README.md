# Pre-entrega - Automatización

## Descripción
Proyecto de automatización de pruebas web realizado como pre-entrega del curso de QA Automation.

El objetivo es automatizar los flujos principales de la página SauceDemo utilizando Selenium WebDriver y Pytest.

## Tecnologías utilizadas
- Python
- Selenium WebDriver
- Pytest
- pytest-html
- Git y GitHub

## Casos de prueba
1. **Login:** verifica el inicio de sesión y el acceso al catálogo.
2. **Catálogo:** verifica que haya un producto visible, el menú lateral y el filtro de ordenamiento.
3. **Carrito:** agrega Sauce Labs Backpack, comprueba el contador y verifica que el producto aparezca en el carrito.

## Instalación
Instalar las dependencias con:


pip install -r requirements.txt


## Ejecución de las pruebas
Ejecutar todos los tests con:


python -m pytest tests/test_saucedemo.py -v


## Reporte HTML
Generar el reporte de resultados con:


python -m pytest tests/test_saucedemo.py -v --html=reports/reporte.html


El reporte se guarda en la carpeta `reports`

## Estructura del proyecto
- `tests/`: contiene los casos de prueba automatizados.
- `utils/`: contiene funciones auxiliares reutilizables.
- `reports/`: contiene el reporte HTML.
- `requirements.txt`: lista las dependencias del proyecto.