from selenium.webdriver.common.by import By
from configuration import *

def test_shop_form(chrome_browser):
    chrome_browser.get(URL_3)
    name = chrome_browser.find_element(By.ID, "user-name").send_keys("standard_user")
    pas = chrome_browser.find_element(By.ID, "password").send_keys("secret_sauce")
    login_button = chrome_browser.find_element(By.ID, "login-button").click()
    first_add = chrome_browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    second_add = chrome_browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    third_add = chrome_browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    container = chrome_browser.find_element(By.ID, "shopping_cart_container").click()
    checkout = chrome_browser.find_element(By.ID, "checkout").click()
    first_name = chrome_browser.find_element(By.ID, "first-name").send_keys("Evgen")
    last_name = chrome_browser.find_element(By.ID, "last-name").send_keys("Voronov")
    postal_code = chrome_browser.find_element(By.ID, "postal-code").send_keys("601500")
    continue_button= chrome_browser.find_element(By.ID, "continue").click()
    total_price = chrome_browser.find_element(By.CLASS_NAME, 'summary_total_label')
    total = total_price.text.strip().replace("Total: $", "")

    expected_total = "58.29"
    assert total == expected_total  # Проверяем, что итоговая сумма равна $58.29
    print("Итоговая сумма равна $58.29") # Выводим сообщение в случае успешного выполнения
