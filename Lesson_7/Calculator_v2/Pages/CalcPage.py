from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Lesson_7.constants import Calculatot_URL


class CalcPage:
    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get(Calculatot_URL)

    def set_delay(self, delay):
        delay_field = self.browser.find_element(By.CSS_SELECTOR, '#delay')
        delay_field.clear()
        delay_field.send_keys(delay)

    def input_text(self, keys_calculator):
        for val in keys_calculator:
            self.browser.find_element(By.XPATH, f'//span[text()="{val}"]').click()

    def wait_result(self, delay, result):
        waiter = WebDriverWait(self.browser, delay + 1)
        waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), str(result)))

    def result_text(self):
        result = self.browser.find_element(By.CSS_SELECTOR, '.screen')
        return result.text
