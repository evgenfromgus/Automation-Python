from selenium.webdriver.common.by import By
from Lesson_7.constants import Shop_URL
import allure


class LoginPage:
    def __init__(self, browser, url=Shop_URL):
        self.browser = browser
        self.url = url

    @allure.step("Переходим по ссылке сервиса")
    def open(self):
        self.browser.get(self.url)

    @allure.step("Ищем поля авторизации, запоняем форму")
    def sign_in(self, user_name, password):
        self.browser.find_element(
            By.CSS_SELECTOR, '#user-name').send_keys(user_name)
        self.browser.find_element(
            By.CSS_SELECTOR, '#password').send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, '#login-button').click()
