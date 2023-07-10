from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_options = webdriver.ChromeOptions()
wait = WebDriverWait(driver, 40, 0.1)

try:
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    name = driver.find_element(By.ID, "user-name").send_keys("standard_user")
    pas = driver.find_element(By.ID, "password").send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button").click()
    first_add = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    second_add = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    third_add = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    container = driver.find_element(By.ID, "shopping_cart_container").click()
    checkout = driver.find_element(By.ID, "checkout").click()
    first_name = driver.find_element(By.ID, "first-name").send_keys("Evgen")
    last_name = driver.find_element(By.ID, "last-name").send_keys("Voronov")
    postal_code = driver.find_element(By.ID, "postal-code").send_keys("601500")
    continue_button= driver.find_element(By.ID, "continue").click()
    total_price = driver.find_element(By.CLASS_NAME, 'summary_total_label')
    total = total_price.text.strip().replace("Total: $", "")

    expected_total = "58.29"
    assert total == expected_total  # Проверяем, что итоговая сумма равна $58.29
    print("Итоговая сумма равна $58.29") # Выводим сообщение в случае успешного выполнения

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()



