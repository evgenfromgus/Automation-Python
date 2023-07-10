import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_options = webdriver.ChromeOptions()
wait = WebDriverWait(driver, 40, 0.1)

def test_data_types_form():
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        first_name = "Иван"
        last_name = "Петров"
        address = "Ленина, 55-3"
        email = "test@skypro.com"
        phone = "+7985899998787"
        zip_code = ""
        city = "Москва"
        country = "Россия"
        job_position = "QA"
        company = "SkyPro"

        # Ввод данных в соответствующие поля
        driver.find_element(By.NAME, "first-name").send_keys(first_name)
        driver.find_element(By.NAME, "last-name").send_keys(last_name)
        driver.find_element(By.NAME, "address").send_keys(address)
        driver.find_element(By.NAME, "e-mail").send_keys(email)
        driver.find_element(By.NAME, "phone").send_keys(phone)
        driver.find_element(By.NAME, "zip-code").send_keys(zip_code)
        driver.find_element(By.NAME, "city").send_keys(city)
        driver.find_element(By.NAME, "country").send_keys(country)
        driver.find_element(By.NAME, "job-position").send_keys(job_position)
        driver.find_element(By.NAME, "company").send_keys(company)
        # Ожидание появления кнопки Submit и ее нажатие
        wait.until(EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()

        # Проверка подсветки полей
        assert "danger" in driver.find_element(By.ID, "zip-code").get_attribute("class")
        assert "success" in driver.find_element(By.ID, "first-name").get_attribute("class")
        assert "success" in driver.find_element(By.ID, "last-name").get_attribute("class")
        assert "success" in driver.find_element(By.ID, "address").get_attribute("class")
        assert "success" in driver.find_element(By.ID, "e-mail").get_attribute("class")
        assert "success" in driver.find_element(By.ID, "phone").get_attribute("class")
        assert "success" in driver.find_element(By.ID, "city").get_attribute("class")
        assert "success" in driver.find_element(By.ID, "country").get_attribute("class")
        assert "success" in driver.find_element(By.ID, "job-position").get_attribute("class")
        assert "success" in driver.find_element(By.ID, "company").get_attribute("class")
