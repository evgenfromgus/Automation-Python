import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

driver.get("https://dzen.ru")
time.sleep(3)
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# options = webdriver.ChromeOptions()
# options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
# options.add_experimental_option('useAutomationExtension', False)
#
# s = Service(executable_path = 'C:\Projects Selenium\First\chromedriver.exe')
#
# driver = webdriver.Chrome(service=s, options=options)
# driver.maximize_window()
#
# driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
#     'source': '''''
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Object;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Proxy;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
#     '''''
# })
# # options.add_argument('--headless')
# # options.add_argument('--disable-notifications')
# # options.add_argument('--disable-popup-blocking')
# # options.add_argument('--disable-infobars')
# # options.add_argument('--disable-blink-features')
# try:
#     #element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "html")))
#
#     driver.get("https://www.ozon.ru/")
#     time.sleep(2)
#     pole = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/header/div[1]/div[3]/div/div/form/div[1]/div[2]/input[1]")))
#     #time.sleep(2)
#     pole.send_keys('royal canin fibre response 2 кг')
#     button_poisk = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/header/div[1]/div[3]/div/div[2]/form/div[2]/button/span"))).click()
#     #time.sleep(2)
#     kupit_button1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#paginatorContent div:nth-child(6) button'))).click()
#     #time.sleep(2)
#     kupit_button2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#paginatorContent div:nth-child(9) button'))).click()
#     # time.sleep(2)
#     korzina = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/header/div[1]/div[4]/a[2]'))).click()
#     #time.sleep(2)
#     udalit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[2]/div[4]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/button/span/span'))).click()
#     podtverdit_udalit = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div/section/div[3]/div/button/span/span').click()
#     #time.sleep(2)
#     driver.refresh()
#     oformlrnie_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div[2]/div[4]/div[2]/div/section/div[1]/div[1]/div[1]/button/span/span'))).click()
#     #time.sleep(2)
#
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()
