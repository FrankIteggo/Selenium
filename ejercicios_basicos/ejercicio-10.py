# 10. Manejo de iFrames

# Enunciado: Visita https://testpages.eviltester.com/styled/iframes-test.html, 
# cambia el foco al iframe, edita el texto dentro del editor y verifica el cambio.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicia el navegador
driver = webdriver.Chrome()

# Navega a la página de espera dinámica
driver.get('https://testpages.eviltester.com/styled/iframes-test.html')

try:
    #-----------------IFRAME 1---------------------#
    # Cambia el foco al iframe 1
    iframe1 = driver.find_element(By.ID, "thedynamichtml")
    print("Cambiamos el foco al iframe 1:")
    driver.switch_to.frame(iframe1)

    # Obtener el contenido del iframe 1
    print("Contenido del iframe 1:")
    html = driver.page_source
    print("Obtenemos el contenido de la lista")
    elements = driver.find_elements(By.TAG_NAME, "li")
    list = [element.text for element in elements]
    print(f"Iframe1: {list}")  # Imprime la lista de elementos en la consola (list)
    
    # Volver al foco principal
    print("Cambiamos el foco al HTLM principal")
    driver.switch_to.default_content()
    time.sleep(2)

    #-----------------IFRAME 2---------------------#
    # Cambia el foco al iframe 2
    iframe2 = driver.find_element(By.ID, "theheaderhtml")
    print("Cambiamos el foco al iframe 2:")
    driver.switch_to.frame(iframe2)

    # Obtener el contenido del iframe 2
    print("Cambiamos el texto:")
    h1 = driver.find_element(By.TAG_NAME, "h1")
    print(f"Iframe2: {h1.text}") 

    # Volver al foco principal
    print("Cambiamos el foco al HTLM principal")
    driver.switch_to.default_content()
    time.sleep(2)
    

except Exception as e:
    print(f"❌ Error detectado: {e}")

finally:
    input("Presiona Enter para salir...")
    driver.quit()  
