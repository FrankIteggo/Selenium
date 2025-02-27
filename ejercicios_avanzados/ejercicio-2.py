# 2. Manejo de Captchas y Autenticación Multi-Factor
#------------------------------- PARTE 1 ----------------------------------------------#
# 􊺪􊺫 URL: https://www.irctc.co.in/nget/train-search
# 􈄥􍿁 Simula la autenticación en un sistema con CAPTCHA (puedes usar OCR con Tesseract).
#------------------------------- PARTE 2 ----------------------------------------------#
# 􊺪􊺫 URL: https://the-internet.herokuapp.com/basic_auth
# 􈄥􍿁 Automatiza el login en una página con autenticación básica
# (http://username:password@url).


import io
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytesseract
from PIL import Image

# Iniciar el navegador
driver = webdriver.Chrome()

#--------------------------------------------------------------------------------------#
#------------------------------------PARTE 1 ------------------------------------------#
#--------------------------------------------------------------------------------------#

pytesseract.pytesseract.tesseract_cmd = r'C:/Users/frank_iteggo/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

driver.get('https://nopecha.com/captcha/textcaptcha')
try:
    # Espera hasta que los iframes sean cargados dinámicamente
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'iframe'))
    )

    # Encuentra todos los elementos iframe en la página
    iframes = driver.find_elements(By.TAG_NAME, 'iframe')

    # Muestra la cantidad de iframes encontrados
    print(f'Se encontraron {len(iframes)} iframes en la página.')

    # Itera sobre cada iframe utilizando su índice
    for index in range(len(iframes)):
        try:
            # Espera hasta que el iframe esté disponible y cambia al contexto del iframe
            WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, 'iframe')))
            print(f'Ahora en el iframe con índice: {index}')
            
            # Aquí puedes realizar las acciones necesarias dentro del iframe
            try:
                elemento = driver.find_element(By.CLASS_NAME, 'captchapict')
                print(f'Se encontró el elemento con clase "captchapict" en el iframe con índice {index}.')
            except Exception as e:
                print(f'No se pudo encontrar el elemento en el iframe con índice {index}: {e}')
            
            # Regresa al contenido principal antes de continuar con el siguiente iframe
            driver.switch_to.default_content()
        except Exception as e:
            print(f'No se pudo cambiar al iframe con índice {index}: {e}')

    # Itera sobre cada iframe utilizando su índice
    for index, iframe in enumerate(iframes):
        try:
            # Cambia al iframe por su índice
            driver.switch_to.frame(iframe)
            print(f'Ahora en el iframe con índice: {index}')

            # Espera hasta que la imagen del CAPTCHA esté presente
            captcha_image = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'img'))
            )

            # Captura una captura de pantalla del elemento de la imagen del CAPTCHA
            captcha_image.screenshot(f'imgs/captcha_{index}.png')

            # Abre la imagen del CAPTCHA
            image = Image.open(f'imgs/captcha_{index}.png')

            # Convierte la imagen a escala de grises
            gray_image = image.convert('L')

            # Aplica un umbral para binarizar la imagen
            binary_image = gray_image.point(lambda x: 0 if x < 140 else 255, '1')

            # Utiliza Tesseract para extraer el texto
            captcha_text = pytesseract.image_to_string(binary_image, config='--psm 8')

            # Limpia el texto extraído
            captcha_text = captcha_text.strip()
            print(f'Texto del CAPTCHA en el iframe {index}: {captcha_text}')

            captchainput = driver.find_element(By.CLASS_NAME, "captcha")
            captchainput.send_keys(captcha_text)

        except Exception as e:
            print(f'No se pudo procesar el iframe con índice {index}: {e}')

        finally:
            # Regresa al contenido principal antes de continuar con el siguiente iframe
            driver.switch_to.default_content()      

except Exception as e:
    print(f"❌ Error detectado: {e}")

#--------------------------------------------------------------------------------------#
#------------------------------------PARTE 2 ------------------------------------------#
#--------------------------------------------------------------------------------------#

time.sleep(5)

# Navegar a la pagina de espera dinamica
driver.get('https://authenticationtest.com/simpleFormAuth/')

try:

    emialInput = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )

    passwordInput = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )

    emialInput.clear()
    passwordInput.clear()

    email = "simpleForm@authenticationtest.com"
    password = "pa$$w0rd"

    print("Escribimos las credenciales")
    emialInput.send_keys(email)
    passwordInput.send_keys(password)

    submitButton = driver.find_element(By.XPATH, "//input[@type='submit']")

    print("Iniciamos sesion")
    submitButton.click()

    assert "https://authenticationtest.com/loginSuccess/" in driver.current_url, "Error: No se ha iniciado sesion"

    print("Sesion iniciada con exito")

    signOutButton = driver.find_element(By.CLASS_NAME, "navbar-text")
    signOutButton.click()

    assert 'https://authenticationtest.com/' in driver.current_url, "Error: No se ha cerrado sesion"

    print("Sesion cerrada con exito")




except Exception as e:
    print(f"❌ Error detectado: {e}")

finally:
    input("Presiona Enter para salir...")
    driver.quit()