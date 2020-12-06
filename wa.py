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
#from selenium.webdriver.support.ui import WebDriverWait
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
        name = input('Introducir el nombre o grupo. Para salir teclear salir: ')
        #Nombre del Chat
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        user.click()
        if name == "salir":
            sys.exit()
            driver.close()
        else:
            #colocarse en el textbox
            #driver.FindElementsByClassName("_1awRl.copyable-text.selectable-text")
            #driver.find_element_by_class_name('_1awRl.copyable-text.selectable-text').click()
            msg = input('Introducir en mensaje : ')            
            #Textobox que define la class CSS JS de WhatsApp
            #msg_box = driver.find_element_by_xpath("//input[@class='_1awRl.copyable-text.selectable-text']")

            #segunda ocurrencia y busqueda plural - hay 2 posiciones en una de las clases
            msg_box = driver.find_elements_by_class_name('_1awRl.copyable-text.selectable-text')[1]
            #msg_box = driver.find_element_by_class_name('_1awRl.copyable-text.selectable-text')
            #
            #element.send_keys => <input type="text" name="passwd" id="passwd-id" /> 
            #ingresar valores en el textbox
            #msg_box.send_keys(msg)
            msg_box.send_keys(msg)
            
            #Button de envío
            driver.find_element_by_class_name("_3qpzV").click()
            #bt.click()
            #msg_box = driver.find_element_by_class_name("Srlyw")
            #msg_box = driver.find_element_by_class_name("_1awRl copyable-text selectable-text")
            #msg_box.send_keys(msg)
            #envio = driver.find_element_by_class_name("_3SvgF _1mHgA copyable-area")
            #envio.click()
            #boton_enviar = driver.find_element_by_xpath("//span[@data-icon='send']")
            #boton_enviar = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
            #boton_enviar.click()

            #element = driver.find_element_by_xpath("//form[input/@name ='search']") 
            #driver.find_element_by_xpath('//span[@data-icon='send']')
            #driver.find_element_by_class_name("_3uMse").click()        
            
finally:
    #Salir del navegador
    driver.quit()