from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path
import os
import os.path
import sys


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
#driver = webdriver.Chrome('/path/to/your_chrome_driver_dir/chromedriver',chrome_options=chrome_options)
#driver = webdriver.Chrome("C:/Users/USUARIO/Desktop/WebDriver",chrome_options=chrome_options)
#driver = webdriver.Chrome(chrome_options=chrome_options)

#Chrome Versión 78.0.3904.87
#driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Firefox()
#driver = webdriver.Chrome()
#driver = webdriver.Chrome(Options())
driver.get("https://web.whatsapp.com/")

#desired_capabilities = DesiredCapabilities()
#desired_capabilities['os'] = True #os_name
#desired_capabilities['os_version'] = os_version
#desired_capabilities['browser_version'] = browser_version
#desired_capabilities = desired_capabilities.chromedriver

name = input('Introducir el nombre o grupo : ')
msg = input('Introducir en mensaje : ')
#count = int(input('Enter the count : '))
#Scan the code before proceeding further
input('Enter anything after scanning QR code')
#Nombre del Chat
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
#Texto
msg_box = driver.find_element_by_class_name("_1awRl.copyable-text.selectable-text")
#for i in range(count):
msg_box.send_keys(msg)
driver.find_element_by_class_name("_3M-N-").click()  #Es un button



#Salir del navegador
#driver.quit()