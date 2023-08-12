from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from Lesson_7.constants import Test_form_URL
from Lesson_7.data.data import *

class Main_page:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(Test_form_URL)
        self._first_name = (By.NAME, "first-name")
        self._last_name = (By.NAME, "last-name")
        self._address = (By.NAME, "address")
        self._email = (By.NAME, "e-mail")
        self._phone = (By.NAME, "phone")
        self._zip_code = (By.NAME, "zip-code")
        self._city = (By.NAME, "city")
        self._country = (By.NAME, "country")
        self._job_position = (By.NAME, "job-position")
        self._company = (By.NAME, "company")
        self._button = (By.TAG_NAME, "button")

    def filling_in_the_fields(self):
        self.browser.find_element(self._first_name).send_keys(first_name)
        self.browser.find_element(self._last_name).send_keys(last_name)
        self.browser.find_element(self._address).send_keys(address)
        self.browser.find_element(self._email).send_keys(email)
        self.browser.find_element(self._phone).send_keys(phone)
        self.browser.find_element(self._zip_code).send_keys(zip_code)
        self.browser.find_element(self._city).send_keys(city)
        self.browser.find_element(self._country).send_keys(country)
        self.browser.find_element(self._job_position).send_keys(job_position)
        self.browser.find_element(self._company).send_keys(company)

    def click_submit_button(self):
        WebDriverWait(self.browser, 40, 0.1).until(EC.element_to_be_clickable(self._button)).click()

    def getting_class_firstname(self):
        self.browser.find_element(self._first_name).get_attribute("class")

    def getting_class_lastname(self):
        self.browser.find_element(self._last_name).get_attribute("class")

    def getting_class_adress(self):
        self.browser.find_element(self._address).get_attribute("class")

    def getting_class_email(self):
        self.browser.find_element(self._email).get_attribute("class")

    def getting_class_phone(self):
        self.browser.find_element(self._phone).get_attribute("class")

    def getting_class_zipcode(self):
        self.browser.find_element(self._zip_code).get_attribute("class")

    def getting_class_city(self):
        self.browser.find_element(self._city).get_attribute("class")

    def getting_class_country(self):
        self.browser.find_element(self._country).get_attribute("class")

    def getting_class_jobposition(self):
        self.browser.find_element(self._job_position).get_attribute("class")

    def getting_class_company(self):
        self.browser.find_element(self._company).get_attribute("class")
