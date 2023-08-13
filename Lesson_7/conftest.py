import pytest
from selenium import webdriver  # импорт драйвера для взаимодействия с браузером


@pytest.fixture()
def chrome_browsers():
    driver = webdriver.Chrome()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920,1080")
    yield driver
    driver.quit()
