import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

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

# Добавляем товары в корзину
product_1 = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
product_1.click()
product_2 = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
product_2.click()
print('Added product 1 and 2 in cart')
time.sleep(2)

# Переход в корзину
go_to_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
go_to_cart.click()
print('Enter in cart')
time.sleep(2)

driver.back()
print('go back')
time.sleep(1)

driver.forward()
print('go forward')
time.sleep(1)