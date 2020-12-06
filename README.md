
automatizacion de envio de mensaje desde script en python con selenium
para navegador firefox
---------------------------------------------------------------------------
las clases dependen de whatsapp, por lo que puede que cambien los nonbres

documentación selenium
-------------------------
https://www.selenium.dev/documentation/en/

documentación selenium desarrolladores - Firefox
-----------------------------------------------------
https://www.selenium.dev/selenium/docs/api/dotnet/html/T_OpenQA_Selenium_Firefox_FirefoxWebElement.htm

requerimientos
---------------------------------------
sudo apt install python3-pip
python3 -m pip install --upgrade pip
pip3 install selenium
pip3 install chromedriver-binary
pip3 install getch

drivers - descargar drivers
------------------------------
Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads
Firefox: https://github.com/mozilla/geckodriver/releases
Safari: https://webkit.org/blog/6900/webdriver-support-in-safari-10/

copiar el fichero y crear carpeta para los drivers.
añadir el fichero al path
-------------------------------------------------------
export PATH=$PATH:~/Desktop/proyectos/python_selenium/WebDirvers

ejecutar script
---------------------
python3 wa.py
