from selenium.webdriver.common.by import By
import allure


class CheckoutPage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step("Оформляем заказ, запоняем форму")
    def make_checkout(self, first_name, last_name, postal_code):
        self.browser.find_element(
            By.CSS_SELECTOR, '#first-name').send_keys(first_name)
        self.browser.find_element(
            By.CSS_SELECTOR, '#last-name').send_keys(last_name)
        self.browser.find_element(
            By.CSS_SELECTOR, '#postal-code').send_keys(postal_code)
        self.browser.find_element(By.CSS_SELECTOR, '#continue').click()

    @allure.step("Получаем значение итоговой суммы")
    def check_total(self):
        return self.browser.find_element(By.CSS_SELECTOR, '.summary_total_label').text
