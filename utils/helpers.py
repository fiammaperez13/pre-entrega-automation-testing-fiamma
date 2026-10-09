def iniciar_sesion(driver):
    usuario = driver.find_element("id", "user-name")
    usuario.send_keys("standard_user")

    contrasena = driver.find_element("id", "password")
    contrasena.send_keys("secret_sauce")

    login = driver.find_element("id", "login-button")
    login.click()