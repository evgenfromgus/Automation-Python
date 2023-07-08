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
    driver.get("http://the-internet.herokuapp.com/entry_ad")
    # Ждем, пока модальное окно не появится и кнопка "Close" станет кликабельной
    wait = WebDriverWait(driver, 10)
    modal_window = wait.until(EC.visibility_of_element_located((By.ID, "modal")))
    close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='modal']//div[@class='modal-footer']//p[text()='Close']")))

    # Шаг 2: Нажимаем кнопку "Close" в модальном окне
    close_button.click()
    time.sleep(3)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
