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
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    finish = wait.until(EC.text_to_be_present_in_element((By.ID, "text"), 'Done!'))
    attr = driver.find_element("id", "award").get_attribute("src")
    print(attr)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
