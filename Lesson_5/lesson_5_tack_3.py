#import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

try:
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

    # Нажимаем на кнопку Add Element 5 раз
    for _ in range(5):
        add_button = driver.find_element("xpath", '//button[text()="Add Element"]')
        add_button.click()

    # Собираем список кнопок Delete
        delete_buttons = driver.find_elements("xpath", '//button[text()="Delete"]')

    # Выводим размер списка
    print(f"Размер списка кнопок Delete: {len(delete_buttons)}")

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
