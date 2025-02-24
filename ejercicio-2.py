from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Iniciar el navegador
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

try:
    # Esperar y manejar el campo de texto
    check_textInput = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "my-text")))
    check_textInput.clear()
    text = "Selenium"
    check_textInput.send_keys(text)
    assert check_textInput.get_attribute("value") == text, "Error: No se ingresó correctamente el texto"
    print(f"Texto ingresado en el campo de texto: {check_textInput.get_attribute('value')}")  # ✅ Verifica

    # Manejar el campo de contraseña
    check_passwordInput = driver.find_element(By.NAME, "my-password")
    check_passwordInput.clear()
    password = "password"
    check_passwordInput.send_keys(password)
    assert check_passwordInput.get_attribute("value") == password, "Error: La contraseña no se ingresó correctamente"
    print(f"Contraseña ingresada: {check_passwordInput.get_attribute('value')}")  # ✅ Verifica

    # Manejar el área de texto
    check_textArea = driver.find_element(By.NAME, "my-textarea")
    check_textArea.clear()
    text_area = "Selenium testing"
    check_textArea.send_keys(text_area)
    assert check_textArea.get_attribute("value") == text_area, "Error: No se ingresó correctamente el texto en el área"
    print(f"Texto ingresado en el área de texto: {check_textArea.get_attribute('value')}")  # ✅ Verifica

    # Manejar el dropdown
    select_dropdown = driver.find_element(By.NAME, "my-select")
    select = Select(select_dropdown)
    select.select_by_visible_text("One")

    selected_option = select.first_selected_option
    assert selected_option.text == "One", "Error: La opción del dropdown no es correcta"
    print(f"Opción seleccionada en el dropdown: {selected_option.text}")  # ✅ Verifica

    # Manejar el botón de envío
    submit_button = driver.find_element(By.CLASS_NAME, "btn")
    submit_button.click()
    print("Botón de enviar clickeado correctamente.")  # ✅ Verifica

except Exception as e:
    print(f"❌ Error detectado: {e}")

finally:
    input("Presiona Enter para salir...")
    driver.quit()
