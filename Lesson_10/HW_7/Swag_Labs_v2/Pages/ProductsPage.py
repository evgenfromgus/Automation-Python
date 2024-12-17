from selenium.webdriver.common.by import By
import allure


class ProductsPage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step("Добавляем необходимый товар в корзину")
    def add_to_cart(self):
        self.browser.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self.browser.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self.browser.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    @allure.step("Переходим в корзину")
    def go_to_cart(self):
        self.browser.find_element(
            By.CSS_SELECTOR, '.shopping_cart_link').click()

    @allure.step("Делаем checkout - переход к оформлению заказа")
    def checkout_click(self):
        self.browser.find_element(By.CSS_SELECTOR, '#checkout').click()
