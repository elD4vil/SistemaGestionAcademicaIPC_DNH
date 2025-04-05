from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

password = "1234"
ruts_para_buscar = ["20318177-9", "11111111-1", "22222222-2", "20573680-8"]

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

def buscar_por_rut(driver, rut):
    try:
        rut_input = driver.find_element(By.XPATH, "//input[@placeholder='Buscar por nombre o rut']")
        rut_input.clear()
        rut_input.send_keys(rut + Keys.RETURN)
        time.sleep(2)

        try:
            sin_resultados = driver.find_element(By.XPATH, "//*[contains(text(), 'Sin Resultados')]")
            if sin_resultados:
                print(f"[i] Búsqueda realizada correctamente. El RUT {rut} NO existe.")
        except NoSuchElementException:
            # Si no aparece "Sin resultados", asumimos que encontró datos
            print(f"[✔] Búsqueda realizada correctamente. El RUT {rut} SÍ existe.")
            
    except NoSuchElementException:
        print(f"[✘] No se encontró el campo de búsqueda para RUT: {rut}")
    except Exception as e:
        print(f"[✘] Error inesperado al buscar RUT {rut}: {e}")

def run_test(rut, password):
    driver = webdriver.Firefox()
    try:
        driver.get("http://localhost:3006")
        time.sleep(2)

        print("Título de la página:", driver.title)

        if login(driver, password):
            buscar_por_rut(driver, rut)
        else:
            print("Deteniendo test...")

    finally:
        driver.quit()


for i, rut in enumerate(ruts_para_buscar, start=1):
    print(f"\n-- Iteración {i} con RUT: {rut} --")
    run_test(rut, password)
