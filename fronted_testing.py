from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def getUrl():
    return 'http://127.0.0.1:5001/users/get_user_data/1'
    # inputUserID = input('enter a user ID: ')
    # return 'http://127.0.0.1:5001/users/get_user_data/' + inputUserID

# loads a web page with chrome driver by the given url parameter
def getDriverByUrl(p_url: str):
    driverPath = "/chromedriver.exe"
    chromDriver = webdriver.Chrome(service=Service(driverPath))
    chromDriver.get(p_url)
    chromDriver.maximize_window()
    return chromDriver

# Navigate to web interface URL using an existing user id
# Check that the userName element is showing (web element exists)
# Print userName (using locator)
def checkIfIDExistOnBrowser(url):
    userName = ''
    chromDriver = getDriverByUrl(url)
    elementCount = len(chromDriver.find_elements(By.ID, value="user"))
    if (elementCount > 0):
        text = chromDriver.find_element(By.ID, value="text").text + ' '
        userName = chromDriver.find_element(By.ID, value="user").text
        print(text + userName)
    else:
        print(chromDriver.find_element(By.ID, value="error").text)
    # time.sleep(2)
    return userName

if __name__ == "__main__":
    checkIfIDExistOnBrowser(getUrl())

# import clean_environment
# print('\n*********** stopWebServer ***********\n')
# clean_environment.stopWebServer()