# Ejercicio 1
# Acceder a una Página Web y Verificar el Título

from selenium import webdriver

driver = webdriver.Chrome()
web = driver.get('https://selenium.dev')


title = driver.title
driver.implicitly_wait(0.5)
word = 'Selenium'
if word in title:
    print('Title contains Selenium')
else:
    print('Title does not contain Selenium')

driver.quit()