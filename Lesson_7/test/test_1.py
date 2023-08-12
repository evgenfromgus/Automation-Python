import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from Lesson_7.constants import Test_form_URL
from Lesson_7.data.data import *

def test_assertion(chrome_browser):

        main_page = Main_page
        main_page.filling_in_the_fields()
        main_page.click_submit_button()
        assert "danger" in main_page.getting_class_zipcode()
        assert "success" in main_page.getting_class_firstname()
        assert "success" in main_page.getting_class_lastname()
        assert "success" in main_page.getting_class_adress()
        assert "success" in main_page.getting_class_email()
        assert "success" in main_page.getting_class_phone()
        assert "success" in main_page.getting_class_zipcode()
        assert "success" in main_page.getting_class_city()
        assert "success" in main_page.getting_class_country()
        assert "success" in main_page.getting_class_jobposition()
        assert "success" in main_page.getting_class_company()




