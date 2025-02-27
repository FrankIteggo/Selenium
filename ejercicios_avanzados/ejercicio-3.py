# 3. Descarga y Validación de Archivos

# - **URL**: https://the-internet.herokuapp.com/download
# - Descarga archivos y verifica su existencia en el sistema de archivos.
# - **URL**: https://the-internet.herokuapp.com/download
# - Descarga un PDF y usa PyMuPDF o pdfminer para extraer y validar el texto.


import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import fitz  # PyMuPDF


# Configurar el directorio de descargas
download_dir = "C:/Users/frank_iteggo/Downloads"

# Iniciar el navegador
driver = webdriver.Chrome()

# Navegar a la página de descarga
driver.get('https://the-internet.herokuapp.com/download')

try:
    # Esperar a que los archivos estén presentes
    files = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@class='example']//a"))
    )

    print(f"Se encontraron {len(files)} archivos en la página.")

    # Descargar los primeros 5 archivos
    for index in range(5):
        file_link = files[index]
        file_name = file_link.get_attribute("href").split("/")[-1]
        print(f"Descargando {file_name}...")

        # Hacer clic en el enlace para descargar
        file_link.click()

        # Esperar que el archivo se descargue (verificar que el archivo esté presente en el directorio)
        time.sleep(2)  # Pausa para dar tiempo a la descarga

        # Verificar si el archivo existe en el directorio de descargas
        if os.path.exists(os.path.join(download_dir, file_name)):
            print(f"Archivo {file_name} descargado con éxito.")

            # Ahora que el archivo está descargado, extraer el texto si es un PDF
            if file_name.endswith(".pdf"):
                pdf_path = os.path.join(download_dir, file_name)
                print(f"Extrayendo texto de {file_name}...")

                # Usar PyMuPDF para abrir y extraer texto del PDF
                with fitz.open(pdf_path) as doc:
                    text = ""
                    for page_num in range(len(doc)):
                        page = doc.load_page(page_num)
                        text += page.get_text()

                print(f"Texto extraído del PDF: {text[:500]}...")  # Imprimir los primeros 500 caracteres del texto extraído

        else:
            print(f"Error: El archivo {file_name} no se descargó correctamente.")

except Exception as e:
    print(f"❌ Error detectado: {e}")

finally:
    input("Presiona Enter para salir...")
    driver.quit()

