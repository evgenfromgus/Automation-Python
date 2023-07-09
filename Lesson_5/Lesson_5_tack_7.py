import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--window-size=1920,1080")

try:
    driver.maximize_window()
    driver.get("http://the-internet.herokuapp.com/inputs")
    input_field = driver.find_element(By.TAG_NAME, "input")
    input_field.send_keys("1000")
    time.sleep(2)
    input_field.clear()
    input_field = driver.find_element(By.TAG_NAME, "input")
    input_field.send_keys("999")
    time.sleep(2)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
