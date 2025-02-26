# Ejercicio 3
# Localización de Elementos y Envío de Datos

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Iniciar el navegador
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

try:
    # Solicitar entrada del usuario con validación
    while True:
        try:
            clicks = int(input("Ingrese cuántos elementos desea añadir (solo números enteros): "))
            if clicks > 0:
                break
            print("⚠ Debe ingresar un número entero mayor a 0.")
        except ValueError:
            print("❌ Error: Ingrese un número entero válido.")

    # Esperar que el botón 'Add Element' esté presente y obtenerlo
    add_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Add Element']"))
    )

    # Agregar elementos
    for _ in range(clicks):
        add_button.click()
    
    print(f"✅ Se agregaron {clicks} botones correctamente.")

    # Esperar que los botones 'Delete' aparezcan antes de eliminarlos
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Delete']"))
    )

    # Eliminar los botones sin hacer múltiples búsquedas
    delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")
    for button in delete_buttons:
        button.click()

    print("✅ Todos los botones han sido eliminados con éxito.")

except Exception as e:
    print(f"❌ Error detectado: {e}")

finally:
    input("Presiona Enter para salir...")
    driver.quit()
