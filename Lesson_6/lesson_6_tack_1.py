from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_options = webdriver.ChromeOptions()
wait = WebDriverWait(driver, 40, 0.1)

try:
    driver.maximize_window()
    driver.get("http://uitestingplayground.com/ajax")
    blue_button = driver.find_element("xpath", "//button[@id='ajaxButton']").click()
    pole = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "bg-success")))
    itog = pole.text
    print(itog)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
