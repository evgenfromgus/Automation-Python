import pytest
from selenium import webdriver #импорт драйвера для взаимодействия с браузером
from webdriver_manager.chrome import ChromeDriverManager # для установки без бинарного файла, наш драйвер
from selenium.webdriver.chrome.service import Service as ChromeService #класс отвечающий за установку драйвера, закрытие и открытие браузера
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
@pytest.fixture()
def chrome_browsers():
    #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) #не работает с версией драйвера 115 и выше
    # driver = webdriver.Chrome()
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    yield driver
    driver.quit()
