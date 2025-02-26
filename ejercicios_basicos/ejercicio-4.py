# Ejercicio 4: Manejo de Checkboxes con Selenium

import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar el controlador de Chrome
driver = webdriver.Chrome()

# Navegar a la página de checkboxes
driver.get('https://the-internet.herokuapp.com/checkboxes')

try:
    # Esperar hasta que los checkboxes estén presentes en el DOM
    checkboxes = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//input[@type='checkbox']"))
    )

    # Contar el número de checkboxes
    num_checkboxes = len(checkboxes)
    print(f"Se encontraron {num_checkboxes} checkboxes en la página.")

    # Iterar sobre cada checkbox para marcarlos
    for index, checkbox in enumerate(checkboxes, start=1):
        if not checkbox.is_selected():
            checkbox.click()
            print(f"El checkbox {index} ha sido marcado.")
        else:
            print(f"El checkbox {index} ya estaba marcado.")

    # Seleccionar un índice aleatorio para desmarcar
    random_checkbox_index = random.randint(1, num_checkboxes)
    random_checkbox = checkboxes[random_checkbox_index - 1]  # Ajustar índice para lista (0-based)

    # Desmarcar el checkbox seleccionado aleatoriamente
    random_checkbox.click()
    print(f"El checkbox {random_checkbox_index} ha sido desmarcado.")

except Exception as e:
    print(f"❌ Error detectado: {e}")

finally:
    input("Presiona Enter para salir...")
    driver.quit()
