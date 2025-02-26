# Captura de Screenshots
# Enunciado: Accede a https://www.selenium.dev y toma una captura de pantalla de la página guardándola como "screenshot.png".


from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image


# Inicializar el controlador de Chrome
driver = webdriver.Chrome()

# Navegar a la página de espera dinámica
driver.get('https://www.selenium.dev')

try:

    # Tomar una captura de pantalla y guardarla solo de la parte visible
    driver.save_screenshot("C:/Users/frank_iteggo/Pictures/Screenshots/screenshot.png") # Poner aqui la ruta deseada
    # Abrir la captura de pantalla
    screenshot = Image.open("C:/Users/frank_iteggo/Pictures/Screenshots/screenshot.png") 
    screenshot.show()


except Exception as e:  
    print(f"❌ Error detectado: {e}")

finally:
    input("Presiona Enter para salir...")
    driver.quit()