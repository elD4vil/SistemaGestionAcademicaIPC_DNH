import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Edge()
    driver.get("http://localhost:3006")
    time.sleep(2)
    yield driver
    driver.quit()

def login(driver, password):
    try:
        password_input = driver.find_element(By.XPATH, "//input[@placeholder='Ingrese su contraseña']")
        password_input.clear()
        password_input.send_keys(password + Keys.RETURN)
        time.sleep(1)

        # Verificar login exitoso
        driver.find_element(By.XPATH, "//input[@placeholder='Buscar por nombre o rut']")
        return True
    except NoSuchElementException:
        return False
    except Exception:
        return False

def aparece_mensaje_credenciales_invalidas(driver):
    try:
        error_msg = driver.find_element(By.XPATH, "//p[contains(text(), 'Credenciales incorrectas')]")
        return error_msg.is_displayed()
    except NoSuchElementException:
        return False

def test_intentos_de_login(driver):
    contraseñas = ["1111", "abcd", "0000", "contraseña_incorrecta", "1234"]  # Última es la correcta
    login_exitoso = False

    for i, pwd in enumerate(contraseñas):
        print(f"[i] Intento #{i+1} con contraseña: {pwd}")
        if login(driver, pwd):
            login_exitoso = True
            print("[✔] Login exitoso")
            break
        else:
            assert aparece_mensaje_credenciales_invalidas(driver), \
                f"[✘] No se mostró mensaje de error tras intento fallido #{i+1} con contraseña: {pwd}"

    assert login_exitoso, "[✘] No se logró login con ninguna contraseña"
