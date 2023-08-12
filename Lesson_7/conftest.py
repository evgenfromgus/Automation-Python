import pytest
from selenium import webdriver #импорт драйвера для взаимодействия с браузером
from webdriver_manager.chrome import ChromeDriverManager # для установки без бинарного файла, наш драйвер
from selenium.webdriver.chrome.service import Service as ChromeService #класс отвечающий за установку драйвера, закрытие и открытие браузера

@pytest.fixture()
def chrome_browser2():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920,1080")
    yield driver
    driver.quit()
