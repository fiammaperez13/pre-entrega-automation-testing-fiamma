
import pytest
from selenium import webdriver


# Crea un navegador independiente para cada prueba.
@pytest.fixture
def driver():
    navegador = webdriver.Chrome()
    yield navegador
    navegador.quit()


# Guarda una captura si falla una prueba.
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    resultado = yield
    reporte = resultado.get_result()

    if reporte.when == "call" and reporte.failed:
        navegador = item.funcargs.get("driver")

        if navegador:
            import os
            os.makedirs("reports", exist_ok=True)
            nombre_archivo = f"reports/{item.name}.png"
            navegador.save_screenshot(nombre_archivo)
            print(f"Captura guardada en: {nombre_archivo}")

