import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

try:
    driver.get("http://uitestingplayground.com/classattr")
    # Запускаем скрипт 3 раза
    for _ in range(3):
    # Кликаем на синюю кнопку
        blue_button = driver.find_element("xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
        blue_button.click()
        time.sleep(2)
    # Кликаем на ок в модальном окне
        driver.switch_to.alert.accept()
        time.sleep(2)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
