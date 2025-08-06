from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Создаем драйвер Safari
driver = webdriver.Safari()

# Сохраняем URL-адрес сайта в переменную base_url.
base_url = 'https://www.saucedemo.com/'

# Открываем страницу
driver.get(base_url)

# Устанавливаем размер окна браузера
driver.set_window_size(1920, 1080)

# Находим поле ввода имени пользователя по XPath
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys("standard_user")
print('Input Login')

# Находим поле ввода пароля по ID
user_password = driver.find_element(By.XPATH, "//input[@id='password']")
user_password.send_keys("secret_sauce")
print('Input password')

# Находим кнопку логина по ID и нажимаем её
login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
login_button.click()
print('Click Login button')
print(driver.current_url)
get_url = driver.current_url
url = 'https://www.saucedemo.com/inventory.html'
assert url == get_url
print("Url корректен")

text_products = driver.find_element(By.XPATH, "//span[@class='title']")
print(text_products.text)
value_text_products = text_products.text
assert value_text_products == 'Products'
print('Заголовок корректен')

# Ждём немного, чтобы увидеть результат
time.sleep(5)
# Закрываем окно браузера
driver.close()
