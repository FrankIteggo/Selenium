# Esperas en Selenium (Explicit Waits)
# Enunciado: Accede a https://the-internet.herokuapp.com/dynamic_loading/1,
# haz clic en el botón “Start” y espera hasta que el mensaje “Hello World!” aparezca en la pantalla.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar el controlador de Chrome
driver = webdriver.Chrome()

# Navegar a la página de espera dinámica
driver.get('https://the-internet.herokuapp.com/dynamic_loading/1')

try:

    # Esperamos a que el boton start este presente en el DOM
    startButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Start']"))
    )
    startButton.click()

    print("Esperando a que aparezca el texto")
    # Esperamos a que los elementos contenidos dentro de esa ID sean visibles0
    text = WebDriverWait(driver, 10).until(
        EC.visibility_of_any_elements_located((By.ID, "finish"))
    )

    print("Hello World")

except Exception as e:
    print(f"❌ Error detectado: {e}")

finally:
    input("Presiona Enter para salir...")
    driver.quit()   