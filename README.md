
automaizacion de test funcionales
---------------------------------------
sudo apt install python3-pip
python3 -m pip install --upgrade pip
pip3 install selenium
pip3 install chromedriver-binary
pip3 install getch

Drivers - descargar
--------------------
Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads
Firefix: https://github.com/mozilla/geckodriver/releases
Safari: https://webkit.org/blog/6900/webdriver-support-in-safari-10/


copiar el fichero y crear carpeta para los drivers.
añadir el fichero al path
-------------------------------------------------------

export PATH=$PATH:~/Desktop/proyectos/python_selenium/WebDirvers

ejecutar python
---------------------
python3 wa.py