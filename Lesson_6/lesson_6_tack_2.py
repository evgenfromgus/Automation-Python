import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_options = webdriver.ChromeOptions()
wait = WebDriverWait(driver, 40, 0.1)

try:
    driver.maximize_window()
    driver.get("http://uitestingplayground.com/textinput")
    pole = driver.find_element("id", "newButtonName").send_keys("SkyPro")
    button = driver.find_element("id", "updatingButton").click()
    button_new = driver.find_element("id", "updatingButton").text
    print(button_new)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
