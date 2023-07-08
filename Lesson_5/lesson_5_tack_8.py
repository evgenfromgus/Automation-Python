import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--window-size=1920,1080")

try:
    driver.maximize_window()
    driver.get("http://the-internet.herokuapp.com/login")
    input_name = driver.find_element(By.ID, "username")
    input_name.send_keys("tomsmith")
    input_pass = driver.find_element(By.ID, "password")
    input_pass.send_keys("SuperSecretPassword!")
    button = driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(2)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
