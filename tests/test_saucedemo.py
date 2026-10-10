from selenium import webdriver
from utils.helpers import iniciar_sesion
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Verifica que el usuario pueda iniciar sesión y acceder al catálogo.
def test_login():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com")

    iniciar_sesion(driver)

    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://www.saucedemo.com/inventory.html")
    )

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    assert driver.title == "Swag Labs"

# Verifica que el catálogo muestre un producto, el menú y el filtro de ordenamiento.
def test_catalogo():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com")

    iniciar_sesion(driver) 

    producto = driver.find_element("css selector", ".inventory_item_name")   
    assert producto.is_displayed()

    nombre_producto = producto.text

    precio_producto = driver.find_element( 
    "css selector", ".inventory_item_price"
 ).text
    
    assert nombre_producto != ""
    assert precio_producto != "" 

    menu = driver.find_element("id", "react-burger-menu-btn")
    assert menu.is_displayed()

    filtro = driver.find_element("class name", "product_sort_container")
    assert filtro.is_displayed()

# Verifica que se pueda agregar un producto al carrito y que aparezca en él.
def test_carrito():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com")

    iniciar_sesion(driver)

    producto = driver.find_element("id", "add-to-cart-sauce-labs-backpack")
    producto.click()
    
    contador = driver.find_element("css selector", ".shopping_cart_badge")
    assert contador.text == "1" 

    carrito = driver.find_element("class name", "shopping_cart_link")
    carrito.click() 

    producto_carrito = driver.find_element("class name", "inventory_item_name")
    assert producto_carrito.text == "Sauce Labs Backpack"

