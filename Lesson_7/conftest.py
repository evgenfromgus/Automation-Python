import pytest
from selenium import webdriver  # импорт драйвера для взаимодействия с браузером
from selenium.webdriver.chrome.service import \
    Service as ChromeService  # класс отвечающий за установку драйвера, закрытие и открытие браузера


@pytest.fixture()
def chrome_browsers():
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) #не работает с версией драйвера 115 и выше
    service = ChromeService(executable_path='Lesson_7/chrome_driver/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920,1080")
    yield driver
    driver.quit()
