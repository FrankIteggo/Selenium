# Practica de Selenium en Python

## Pasos a seguir

### Instalación

1. Instalar python https://www.python.org/downloads/
2. Instalar Selenium para python:
   > [!NOTE]
   >
   > ```bash
   > pip install selenium
   > ```

> [!CAUTION]
> Comprueba que el interprete de python es el acorde a tu versión de Python instalada para que detecte adecuadamente el import de Selenium

# Ejercicios Básicos de Selenium

> [!TIP]
> Haz uso del Expected Conditions (EC) junto al WebDriverWait
> Puedes ver mas informacion aqui: https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html

> [!TIP]
> Haz uso de bloque Try, Except para mejorar la integridad del código y el manejo de errores

## 1. Acceder a una Página Web y Verificar el Título

Enunciado: Crea un script en Selenium que abra la página
https://www.selenium.dev, obtenga el título de la página y verifique que
contiene la palabra "Selenium".

## 2. Localización de Elementos y Envío de Datos

Enunciado: Escribe un script que acceda al formulario de
https://www.selenium.dev/selenium/web/web-form.html, complete los campos
de texto, seleccione una opción de la lista desplegable y envíe el formulario.

## 3. Clic en un Botón y Validación de Mensaje

Enunciado: Abre la página https://theinternet.
herokuapp.com/add_remove_elements/, haz clic en el botón “Add
Element” varias veces y luego elimina todos los elementos generados. Verifica que no quede ninguno.

## 4. Manejo de Checkboxes y Radiobuttons

Enunciado: Accede a https://the-internet.herokuapp.com/checkboxes,
selecciona ambos checkboxes y luego deselecciona uno de ellos.

## 5. Captura de Texto y Comparación

Enunciado: Ve a https://the-internet.herokuapp.com/inputs, ingresa un número en el campo de texto, luego obtén su valor y confirma que es correcto.

## 6. Esperas en Selenium (Explicit Waits)

Enunciado: Accede a https://the-internet.herokuapp.com/dynamic_loading/1,
haz clic en el botón “Start” y espera hasta que el mensaje “Hello World!” aparezca en la pantalla.

## 7. Manejo de Alertas y Pop-ups

Enunciado: Entra a https://the-internet.herokuapp.com/javascript_alerts, activa la alerta de JavaScript y acéptala. Luego, captura el mensaje mostrado en la
página.

## 8. Navegación entre Páginas y Volver Atrás

Enunciado: Crea un script que abra https://www.selenium.dev, haga clic en el enlace "Downloads", verifique que cambió la URL y luego regrese a la página
anterior.

## 9. Captura de Screenshots

Enunciado: Accede a https://www.selenium.dev y toma una captura de pantalla de la página guardándola como "screenshot.png".

> [!WARNING]
> Se recomienda la instalacion de la libreria Pillow
>
> ```bash
> pip install Pillow
> ```
>
> mas info [aqui](https://www.browserstack.com/guide/take-screenshot-with-selenium-python)

## 10. Manejo de iFrames

Enunciado: Visita https://testpages.eviltester.com/styled/iframes-test.html, cambia el foco entre los diferentes iframes y obten su contenido

# Ejercicios Avanzados de Selenium

## 1. Manejo de Elementos Dinámicos y AJAX

- **URL**: [https://the-internet.herokuapp.com/dynamic_controls](https://the-internet.herokuapp.com/dynamic_controls)
  - Prueba interactuar con botones que agregan o eliminan elementos dinámicamente.
  - Usa `WebDriverWait` para verificar cuándo aparecen o desaparecen los elementos.
- **URL**: [https://demoqa.com/dynamic-properties](https://demoqa.com/dynamic-properties)
  - Espera a que un botón se active después de un tiempo y haz clic en él.

## 2. Manejo de Captchas y Autenticación Multi-Factor

- **URL**: [https://www.irctc.co.in/nget/train-search](https://www.irctc.co.in/nget/train-search)
  - Simula la autenticación en un sistema con CAPTCHA (puedes usar OCR con Tesseract).
- **URL**: [https://the-internet.herokuapp.com/basic_auth](https://the-internet.herokuapp.com/basic_auth)
  - Automatiza el login en una página con autenticación básica (http://username:password@url).

## 3. Descarga y Validación de Archivos

- **URL**: [https://the-internet.herokuapp.com/download](https://the-internet.herokuapp.com/download)
  - Descarga archivos y verifica su existencia en el sistema de archivos.
- **URL**: [https://file-examples.com/index.php/sample-documents-download/samplepdf-download/](https://file-examples.com/index.php/sample-documents-download/samplepdf-download/)
  - Descarga un PDF y usa PyMuPDF o pdfminer para extraer y validar el texto.

## 4. Pruebas en Múltiples Pestañas y Ventanas

- **URL**: [https://the-internet.herokuapp.com/windows](https://the-internet.herokuapp.com/windows)
  - Abre una nueva ventana y cambia de contexto para interactuar con ella.
- **URL**: [https://demoqa.com/browser-windows](https://demoqa.com/browser-windows)
  - Automatiza el manejo de múltiples pestañas y ventanas emergentes.

## 5. Automatización en Aplicaciones SPA (React, Angular, Vue)

- **URL**: [https://demoqa.com/](https://demoqa.com/)
  - Prueba elementos dinámicos en una Single Page Application (SPA).
  - Usa `JavaScriptExecutor` para interactuar con `Shadow DOM`.

## 6. Ejecución en Headless Mode con Screenshots

- **URL**: [https://www.selenium.dev/selenium/web/web-form.html](https://www.selenium.dev/selenium/web/web-form.html)
  - Ejecuta pruebas en headless mode y toma capturas de pantalla solo cuando falle un test.

## 7. Automatización de Web Scraping con Selenium

- **URL**: [https://www.worldometers.info/coronavirus/](https://www.worldometers.info/coronavirus/)
  - Extrae datos de tablas y guárdalos en un archivo CSV con pandas.
- **URL**: [https://books.toscrape.com/](https://books.toscrape.com/)
  - Realiza scraping de libros con sus precios y títulos.

## 8. Manejo de iframes y Pop-ups

- **URL**: [https://the-internet.herokuapp.com/iframe](https://the-internet.herokuapp.com/iframe)
  - Cambia el contexto a un iframe y edita el contenido dentro del editor.
- **URL**: [https://www.w3schools.com/jsref/tryit.asp?filename=tryjs_alert](https://www.w3schools.com/jsref/tryit.asp?filename=tryjs_alert)
  - Captura y maneja una alerta emergente con `switchTo().alert()`.

## 9. Ejecutar Pruebas en Diferentes Entornos (Docker + Selenium Grid)

- **URL**: [https://opensource-demo.orangehrmlive.com/](https://opensource-demo.orangehrmlive.com/)
  - Configura Selenium Grid y ejecuta pruebas en distintos navegadores en paralelo.

## 10. Integración con APIs y Bases de Datos

- **URL**: [https://reqres.in/](https://reqres.in/)
  - Automatiza una prueba que compara datos extraídos de una web con una API REST.
