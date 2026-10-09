from selenium import webdriver
from utils.helpers import iniciar_sesion

def test_login():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com")

    iniciar_sesion(driver)

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    assert driver.title == "Swag Labs"

def test_catalogo():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com")

    iniciar_sesion(driver) 

    producto = driver.find_element("css selector", ".inventory_item_name")   
    assert producto.is_displayed()

    menu = driver.find_element("id", "react-burger-menu-btn")
    assert menu.is_displayed()

    filtro = driver.find_element("class name", "product_sort_container")
    assert filtro.is_displayed()

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

