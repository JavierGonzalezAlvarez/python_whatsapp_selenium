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

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

#Hay que cerrar las conexiones del whatsApp con el navegador
print("Abriendo el Navegador ...")
driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")

name = "Javier"
while name != "salir":
	name = input('Introducir el nombre o grupo (Salir) = salir: ')
	msg = input('Introducir en mensaje : ')
	if name == "salir":
	    sys.exit()
	else:
	    #Nombre del Chat
		user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
		user.click()
		#Textobox que define la class CSS JS de WhatsApp
		msg_box = driver.find_element_by_class_name("_1awRl.copyable-text.selectable-text")
		msg_box.send_keys(msg)
		#Button de envío        
        driver.find_element_by_xpath("//span[@data-icon='send']")
        element = driver.find_element_by_xpath("//form[input/@name ='search']") 
        #boton_enviar = driver.find_element_by_xpath('//span[@data-icon='send']')
		#driver.find_element_by_class_name("_3uMse").click()        
        boton_enviar.click()

#Salir del navegador
#driver.quit()
