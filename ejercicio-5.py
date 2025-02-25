import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar el controlador de Chrome
driver = webdriver.Chrome()

# Navegar a la página de inputs
driver.get('https://the-internet.herokuapp.com/inputs')

try:
    # Esperar hasta que el input tipo number esté presente en el DOM
    numInput = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='number']"))
    )

    # Limpiar el input
    numInput.clear()

    # Generar un número aleatorio entre 1 y 9999
    random_num = random.randint(1, 9999)

    # Convertir el número a cadena y enviarlo al input
    numInput.send_keys(str(random_num))

    # Verificar que el valor ingresado sea correcto
    # Convertimos random_num a cadena porque get_attribute retorna una cadena
    assert numInput.get_attribute("value") == str(random_num), "Error: No se ingresó correctamente el número"
    print(f"El número ingresado ha sido {random_num}")

except Exception as e:
    print(f"❌ Error detectado: {e}")

finally:
    input("Presiona Enter para salir...")
    driver.quit()
