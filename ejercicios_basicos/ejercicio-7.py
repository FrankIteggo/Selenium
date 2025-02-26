# Manejo de Alertas y Pop-ups
# Enunciado: Entra a https://the-internet.herokuapp.com/javascript_alerts, activa la alerta de JavaScript y acéptala. Luego, captura el mensaje mostrado en la
# página.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar el controlador de Chrome
driver = webdriver.Chrome()

# Navegar a la página de espera dinámica
driver.get('https://the-internet.herokuapp.com/javascript_alerts')

try:

    # ---------------------------- MENSAJE ALERTA JS ---------------------------------------------
    print("------------------------------ EJECUTANTO PRIMER BLOQUE ---------------------------------------")
    alertButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Click for JS Alert']"))
    )

    alertButton.click()

    WebDriverWait(driver,10).until(
        EC.alert_is_present()
    )
    alert = driver.switch_to.alert

    alertText = alert.text
    print(f"Mensaje de la alerta: {alertText}")
    alert.accept()

    # Mensaje del result
    result = driver.find_element(By.ID, "result")
    

    resultText = result.text
    print(f"Result: {resultText}")

    # ---------------------------- MENSAJE CONFIRM JS ---------------------------------------------
    print("------------------------------ EJECUTANTO SEGUNDO BLOQUE ---------------------------------------")
    confirmButton = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Confirm']"))
    )

    confirmButton.click()

    WebDriverWait(driver,10).until(
        EC.alert_is_present()
    )
    confirm = driver.switch_to.alert

    confirmText = confirm.text
    print(f"Mensaje del confirm: {confirmText}")
    confirm.accept()

    # Mensaje del result
    result = driver.find_element(By.ID, "result")
    

    resultText = result.text
    print(f"Result: {resultText}")

    # ---------------------------- PROMPT JS ---------------------------------------------
    print("------------------------------ EJECUTANTO TERCER BLOQUE ---------------------------------------")
    promptButton = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")

    promptButton.click()

    WebDriverWait(driver,10).until(
        EC.alert_is_present()
    )

    prompt = driver.switch_to.alert

    promptText = prompt.text
    print(f"Mensaje del prompt: {promptText}")

    promptInput = "Hola mundo"
    prompt.send_keys(promptInput)

    alert.accept()

    # Mensaje del result
    result = driver.find_element(By.ID, "result")
    

    resultText = result.text
    print(f"Result: {resultText}")




except Exception as e:
    print(f"❌ Error detectado: {e}")

finally:
    input("Presiona Enter para salir...")
    driver.quit()  