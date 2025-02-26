# Navegación entre Páginas y Volver Atrás
# Enunciado: Crea un script que abra https://www.selenium.dev, haga clic en el enlace "Downloads", verifique que cambió la URL y luego regrese a la página
# anterior.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Iniciar el controlador de Chrome
driver = webdriver.Chrome()

# Navegar a la pagina de espera dinamica
driver.get('https://www.selenium.dev')

try:

    # Navegar a downloads
    downloadNav = driver.find_element(By.LINK_TEXT, "Downloads")
    downloadNav.click()

    assert "https://www.selenium.dev/downloads" in driver.current_url, "Error: La URL no ha cambiado"

    # Volver atras
    driver.back()

except Exception as e:
    print(f"❌ Error detectado: {e}")

finally:
    input("Presiona Enter para salir...")
    driver.quit()