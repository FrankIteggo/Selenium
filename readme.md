# Practica de Selenium en Python

## Pasos a seguir

### Instalación

1. Instalar python https://www.python.org/downloads/
2. Instalar Selenium para python: `pip install selenium`

>[!CAUTION]
>Comprueba que el interprete de python es el acorde a tu versión de Python instalada para que detecte adecuadamente el import de Selenium

# Ejercicios Básicos de Selenium

>[!TIP]
>Haz uso del Expected Conditions (EC) junto al WebDriverWait
>Puedes ver mas informacion aqui: https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html

>[!TIP]
>Haz uso de bloque Try, Except para mejorar la integridad del código y el manejo de errores 

1. Acceder a una Página Web y Verificar el Título
   Enunciado: Crea un script en Selenium que abra la página
   https://www.selenium.dev, obtenga el título de la página y verifique que
   contiene la palabra "Selenium".

2. Localización de Elementos y Envío de Datos
   Enunciado: Escribe un script que acceda al formulario de
   https://www.selenium.dev/selenium/web/web-form.html, complete los campos
   de texto, seleccione una opción de la lista desplegable y envíe el formulario.

3. Clic en un Botón y Validación de Mensaje
   Enunciado: Abre la página https://theinternet.
   herokuapp.com/add_remove_elements/, haz clic en el botón “Add
   Element” varias veces y luego elimina todos los elementos generados. Verifica que no quede ninguno.

4. Manejo de Checkboxes y Radiobuttons
   Enunciado: Accede a https://the-internet.herokuapp.com/checkboxes,
   selecciona ambos checkboxes y luego deselecciona uno de ellos.

5. Captura de Texto y Comparación
   Enunciado: Ve a https://the-internet.herokuapp.com/inputs, ingresa un número en el campo de texto, luego obtén su valor y confirma que es correcto.

6. Esperas en Selenium (Explicit Waits)
   Enunciado: Accede a https://the-internet.herokuapp.com/dynamic_loading/1,
   haz clic en el botón “Start” y espera hasta que el mensaje “Hello World!” aparezca en la pantalla.

7. Manejo de Alertas y Pop-ups
   Enunciado: Entra a https://the-internet.herokuapp.com/javascript_alerts, activa la alerta de JavaScript y acéptala. Luego, captura el mensaje mostrado en la
   página.

8. Navegación entre Páginas y Volver Atrás
   Enunciado: Crea un script que abra https://www.selenium.dev, haga clic en el enlace "Downloads", verifique que cambió la URL y luego regrese a la página
   anterior.

9. Captura de Screenshots
   Enunciado: Accede a https://www.selenium.dev y toma una captura de pantalla de la página guardándola como "screenshot.png".

10. Manejo de iFrames
    Enunciado: Visita https://the-internet.herokuapp.com/iframe, cambia el foco al iframe, edita el texto dentro del editor y verifica el cambio.
