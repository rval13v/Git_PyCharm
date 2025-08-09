import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920, 1080)
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys("standard_user")
print('Input Login')
user_password = driver.find_element(By.XPATH, "//input[@id='password']")
user_password.send_keys("secret_sauce")
print('Input password')
login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
login_button.click()
print('Click Login button')

# Клик по кнопкам добавления товаров
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']").click()
driver.find_element(By.XPATH, "//button[@id=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]").click()

# Переход в корзину
driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']").click()

# Наведение мыши на элемент
actions = ActionChains(driver)
element = driver.find_element(By.ID, 'item_3_title_link')
actions.move_to_element(element).perform()

