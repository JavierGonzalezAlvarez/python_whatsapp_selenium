from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path
import os
import os.path
import sys
#windows
#import msvcrt
#linux
import getch

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

#windows tabs
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_element_located

#Hay que cerrar las conexiones del whatsApp con el navegador
print("Abriendo el Navegador ...")
driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")
driver.current_window_handle
url = driver.current_url
print("Actual URL: ", url)
title = driver.title
print("Actual title: ", title)
tab = driver.current_window_handle
print("Actual tab: ", tab)

try:
    name = "Javier"
    while name != "salir":
        name = input('Introducir el nombre o grupo (para salir teclear => salir): ')  
        if name == "salir":
            sys.exit()
            driver.close()
        else:
            #Nombre del Chat
            user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
            user.click()            
            msg = input('Introducir en mensaje : ')            
            #Textobox que define la class CSS JS de WhatsApp
            #msg_box = driver.find_element_by_xpath("//input[@class='_1awRl.copyable-text.selectable-text']")

            #segunda ocurrencia y busqueda plural - hay 2 posiciones en una de las clases
            #los espacios se sustituyen por puntos
            #localizar con inspector de elementos la clase
            msg_box = driver.find_elements_by_class_name('_1awRl.copyable-text.selectable-text')[1]
            #msg_box = driver.find_element_by_class_name('_1awRl.copyable-text.selectable-text')
            #
            #element.send_keys => <input type="text" name="passwd" id="passwd-id" /> 
            #ingresar valores en el textbox
            #msg_box.send_keys(msg)
            msg_box.send_keys(msg)
            
            #Button de envío - lcoalizar el boton  => <button class="_2Ujuu">     
            driver.find_element_by_class_name("_2Ujuu").click()
            print("Mensaje enviado por WhatsApp")            
            
finally:
    #Salir del driver en caso de error
    driver.quit()