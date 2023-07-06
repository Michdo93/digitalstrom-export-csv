import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import pyautogui
#from PIL import ImageGrab # needed if you use Windows or Mac
from pynput.keyboard import Controller

pyautogui.FAILSAFE = False
ACCURACY = 0.80
BASE_PATH = "<path_to_pictures>"
keyboard = Controller()
# Setze den Pfad zum geckodriver
geckodriver_path = "<path_to_geckodriver>/geckodriver"
# Erstelle ein Service-Objekt für den geckodriver
service = Service(geckodriver_path)

username = None
password = None
signin = None
csvexport = None
advanced = None
acceptrisk = None

# Setze die Umgebungsvariable DISPLAY auf :0
os.environ["DISPLAY"] = ":0"

# Erstelle eine Instanz des Firefox-Browsers mit dem geckodriver-Pfad
options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.binary_location = '/usr/bin/firefox'

browser = webdriver.Firefox(service=service, options=options)
browser.implicitly_wait(10)

# Öffne die gewünschte URL
url = "https://<ip_to_dss>/add-ons/system-addon-metering/"
browser.get(url)

# 3 Sekunden warten
time.sleep(3)


while (username == None):
    try:
        username = pyautogui.locateOnScreen(BASE_PATH + '/' + 'username.png', confidence=ACCURACY)
    except Exception as e:
        print(e)

    if username is not None:
        usernameCenter = pyautogui.center(username)
        pyautogui.click(usernameCenter)
        time.sleep(2)
        keyboard.type("<username>")

while (password == None):
    try:
        password = pyautogui.locateOnScreen(BASE_PATH + '/' + 'password.png', confidence=ACCURACY)
    except Exception as e:
        print(e)

    if password is not None:
        passwordCenter = pyautogui.center(password)
        pyautogui.click(passwordCenter)
        time.sleep(2)
        keyboard.type("<password>")

while (signin == None):
    try:
        signin = pyautogui.locateOnScreen(BASE_PATH + '/' + 'signin.png', confidence=ACCURACY)
    except Exception as e:
        print(e)

    if signin is not None:
        signinCenter = pyautogui.center(signin)
        pyautogui.click(signinCenter)
        time.sleep(1)

time.sleep(3)

while (csvexport == None):
    try:
        csvexport = pyautogui.locateOnScreen(BASE_PATH + '/' + 'csvexport.png', confidence=ACCURACY)
    except Exception as e:
        print(e)

    if csvexport is not None:
        csvexportCenter = pyautogui.center(csvexport)
        pyautogui.click(csvexportCenter)
        time.sleep(1)

time.sleep(3)

try:
    advanced = pyautogui.locateOnScreen(BASE_PATH + '/' + 'advanced.png', confidence=ACCURACY)
except Exception as e:
    print(e)

if advanced is not None:
    advancedCenter = pyautogui.center(advanced)
    pyautogui.click(advancedCenter)
    time.sleep(1)

time.sleep(3)

try:
    acceptrisk = pyautogui.locateOnScreen(BASE_PATH + '/' + 'acceptrisk.png', confidence=ACCURACY)
except Exception as e:
    print(e)

if acceptrisk is not None:
    acceptriskCenter = pyautogui.center(acceptrisk)
    pyautogui.click(acceptriskCenter)
    time.sleep(1)

time.sleep(5)

# Beende den Firefox-Browser
browser.quit()
