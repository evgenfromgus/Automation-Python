from selenium.webdriver.common.by import By

# class DataFild:
#     def __init__(self, browser):
#         self.browser = browser

#     # Находим необходимые поля для заполнения 
#     def find_fields(self):
#         self.class_first_name = (By.ID, "first-name")
#         self.class_last_name = (By.ID, "last-name")
#         self.class_address = (By.ID, "address")
#         self.class_email = (By.ID, "e-mail")
#         self.class_phone = (By.ID, "phone")
#         self.class_zip_code = (By.ID, "zip-code")
#         self.class_city = (By.ID, "city")
#         self.class_country = (By.ID, "job-position")
#         self.class_job_position = (By.ID, "country")
#         self.class_company = (By.ID, "company")
    
#     # Получаем значение классов полей
#     def get_class_first_name(self):
#         return self.browser.find_element(*self.class_first_name).get_attribute("class")

#     def get_class_last_name(self):
#         return self.browser.find_element(*self.class_last_name).get_attribute("class")

#     def get_class_address(self):
#         return self.browser.find_element(*self.class_address).get_attribute("class")

#     def get_class_email(self):
#         return self.browser.find_element(*self.class_email).get_attribute("class")

#     def get_class_phone(self):
#         return self.browser.find_element(*self.class_phone).get_attribute("class")

#     def get_class_zipcode(self):
#         return self.browser.find_element(*self.class_zip_code).get_attribute("class")

#     def get_class_city(self):
#         return self.browser.find_element(*self.class_city).get_attribute("class")

#     def get_class_country(self):
#         return self.browser.find_element(*self.class_country).get_attribute("class")

#     def get_class_jobposition(self):
#         return self.browser.find_element(*self.class_job_position).get_attribute("class")

#     def get_class_company(self):
#         return self.browser.find_element(*self.class_company).get_attribute("class")


# оптимизированный способ
#В этом подходе:
#Создаётся словарь fields, где ключи — это имена полей, а значения — соответствующие локаторы.
#Метод get_class принимает имя поля (ключ словаря), извлекает соответствующий локатор, находит элемент и возвращает значение его атрибута class.
class DataFild:
    def __init__(self, browser):
        self.browser = browser

    def find_fields(self):
        self.fields = {
            "first_name": (By.ID, "first-name"),
            "last_name": (By.ID, "last-name"),
            "address": (By.ID, "address"),
            "email": (By.ID, "e-mail"),
            "phone": (By.ID, "phone"),
            "zip_code": (By.ID, "zip-code"),
            "city": (By.ID, "city"),
            "country": (By.ID, "country"),
            "job_position": (By.ID, "job-position"),
            "company": (By.ID, "company")
        }

    def get_class(self, field_name):
        locator = self.fields[field_name]
        return self.browser.find_element(*locator).get_attribute("class")