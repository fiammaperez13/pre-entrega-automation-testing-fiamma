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
2. **Catálogo:** verifica que haya un producto visible, su nombre y precio, el menú lateral y el filtro de ordenamiento.
3. **Carrito:** agrega Sauce Labs Backpack, comprueba el contador y verifica que el producto aparezca en el carrito.

## Instalación

Instalar las dependencias con:

```bash
pip install -r requirements.txt
```

## Ejecución de las pruebas

Ejecutar los tests con:

```bash
python -m pytest tests/test_saucedemo.py -v
```

## Reporte HTML

Generar el reporte de resultados con:

```bash
python -m pytest tests/test_saucedemo.py -v --html=reports/reporte.html
```

El reporte HTML se guarda en `reports/reporte.html`.

## Evidencias de ejecución

El proyecto incluye las siguientes evidencias:

- `reports/reporte.html`: reporte HTML con los resultados de las pruebas.
- `reports/ejecucion.log`: registro de la ejecución de las pruebas.
- Capturas de pantalla automáticas ante fallos, configuradas en `conftest.py`.

Para ejecutar las pruebas y actualizar el reporte HTML y el registro de ejecución desde PowerShell:

```powershell
python -m pytest tests/test_saucedemo.py -v --html=reports/reporte.html 2>&1 | Tee-Object -FilePath reports/ejecucion.log
```

## Estructura del proyecto

- `tests/`: contiene los casos de prueba automatizados.
- `utils/`: contiene funciones auxiliares reutilizables.
- `reports/`: contiene el reporte HTML, el registro de ejecución y las capturas generadas ante fallos.
- `conftest.py`: configura el navegador y las capturas automáticas ante fallos.
- `requirements.txt`: lista las dependencias del proyecto.
- `.gitignore`: indica qué archivos y carpetas no se deben subir a Git.
- `README.md`: documenta el proyecto y explica cómo instalar y ejecutar las pruebas.