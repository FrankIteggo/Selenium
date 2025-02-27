

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Iniciar el navegador
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_controls")

try:
    # Esperar hasta que los checkboxes estén presentes en el DOM

    #-------------------PRIMER BLOQUE----------------------------------------------
    checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox']"))
    )
    checkbox.click()

    removeButton = driver.find_element(By.XPATH, "//button[text()='Remove']")
    removeButton.click()
    print("Remove button has been clicked")

    print("Add button has appear")
    addButton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Add']"))
    )
    
    addButton.click()
    print("Add button has been clicked")

    #-------------------SEGUNDO BLOQUE----------------------------------------------
    enableButton = driver.find_element(By.XPATH, "//button[text()='Enable']")
    enableButton.click()

    print("Waiting for text input to be clickable.... ")
    textInput = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))
    )
    
    print("Text input is now clickable")
    if textInput.is_enabled:
        text = "Hola Mundo"
        textInput.send_keys(text)
    else:
        print("El text input esta deshabilitado")

 


except Exception as e:
    print(f"❌ Error detectado: {e}")

finally:
    input("Presiona Enter para salir...")
    driver.quit()