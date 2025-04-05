from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import time


driver = webdriver.Firefox()

driver.get("http://localhost:3006")

def login(driver, password):
    try:
        password_input = driver.find_element(By.XPATH, "//input[@placeholder='Ingrese su contraseña']")
        password_input.send_keys(password + Keys.RETURN)
        time.sleep(2)

        try:
            driver.find_element(By.XPATH, "//input[@placeholder='Buscar por nombre o rut']")
            print("[✔] Login exitoso.")
            return True
        except NoSuchElementException:
            print("[✘] Login fallido: contraseña incorrecta.")
            return False

    except NoSuchElementException:
        print("[✘] Campo de contraseña no encontrado.")
        return False
    except Exception as e:
        print(f"[✘] Error inesperado durante login: {e}")
        return False


def run_test():
    login(driver, "1234")


run_test()
driver.quit()
