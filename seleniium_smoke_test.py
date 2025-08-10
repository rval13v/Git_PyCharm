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

# Создаем переменную первого товара
product_1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

# Создаем переменную второго товара
product_2 = driver.find_element(By.XPATH, "//*[@id='item_1_title_link']/div")
value_product_2 = product_2.text
print(value_product_2)

price_product_2 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div")
value_price_product_2 = price_product_2.text
print(value_price_product_2)
time.sleep(1)

# Добавляем в корзину оба товара
select_product_1 = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']").click()
print('Add product_1 to cart')

select_product_2 = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
print('Add product_2 to cart')

# Переходим в корзину
cart = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()
print('Enter in cart')

# Проверяем в корзине товары и цены
cart_product_1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']")
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print('Info cart product 1 is good')

cart_product_2 = driver.find_element(By.XPATH, "//*[@id='item_1_title_link']/div")
value_cart_product_2 = cart_product_2.text
print(value_cart_product_2)
assert value_product_2 == value_cart_product_2
print('Info cart product 2 is good')

price_cart_product_1 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_cart_product_1 = price_cart_product_1.text
print(value_price_cart_product_1)
assert value_price_cart_product_1 == value_price_product_1
print('Info product_1 price in cart is good')

price_cart_product_2 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_price_cart_product_2 = price_cart_product_2.text
print(value_price_cart_product_2)
assert value_price_cart_product_2 == value_price_product_2
print('Info product_2 price in cart is good')

# Кликаем кнопку Checkout
checkout = driver.find_element(By.XPATH, "//*[@id='checkout']").click()
print('Click checkout')

# Заполняем поля имя, фамилия, индекс
first_name = driver.find_element(By.XPATH, "//*[@id='first-name']")
first_name.send_keys('Duke')
print('Input first name')

second_name = driver.find_element(By.XPATH, "//*[@id='last-name']")
second_name.send_keys('Dundee')
print('Input second name')

post_code= driver.find_element(By.XPATH, "//*[@id='postal-code']")
post_code.send_keys('123232')
print('Input post code')

# Жмем продолжить
button_continue = driver.find_element(By.XPATH, "//*[@id='continue']").click()
print('Click continue')

time.sleep(2)
finish_product_1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div")
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_finish_product_1 == value_product_1
print('Info finish product_1 is good')

finish_product_2 = driver.find_element(By.XPATH, "//*[@id='item_1_title_link']/div")
value_finish_product_2 = finish_product_2.text
print(value_finish_product_2)
assert value_finish_product_2 == value_product_2
print('Info finish product_2 is good')

price_finish_product_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_finish_product_1 = price_finish_product_1.text
print(value_price_finish_product_1)
assert value_price_finish_product_1 == value_price_product_1
print('Finish price product_1 is OK')

price_finish_product_2 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_price_finish_product_2 = price_finish_product_2.text
print(value_price_finish_product_2)
assert value_price_finish_product_2 == value_price_product_2
print('Finish price product_2 is OK')

summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
value_summary_price = summary_price.text
print(value_summary_price)
total_price = float(value_price_finish_product_1.strip('$')) + float(value_price_finish_product_2.strip('$'))
item_total = f"Item total: ${total_price:.2f}"
print(item_total)
assert value_summary_price == item_total
print('Total summary price is OK')

button_finish = driver.find_element(By.XPATH, "//*[@id='finish']").click()
print('Click finish button')

checkout_complete = driver.find_element(By.XPATH, "//*[contains(text(), 'Checkout: Complete!')]")
value_checkout_complete = checkout_complete.text
print(value_checkout_complete)
assert value_checkout_complete == 'Checkout: Complete!'
print('Checkout: Complete!')
