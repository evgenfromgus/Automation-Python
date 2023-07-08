#import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

try:
    driver.get("http://uitestingplayground.com/dynamicid")
    # Кликаем на синюю кнопку
    blue_button = driver.find_element("xpath", '//button[text()="Button with Dynamic ID"]')
    blue_button.click()

    # Запускаем скрипт 3 раза
    for _ in range(3):
    # Рекликаем на синюю кнопку
        blue_button = driver.find_element("xpath", '//button[text()="Button with Dynamic ID"]')
        blue_button.click()

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
