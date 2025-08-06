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

# Находим поле ввода пароля по ID
user_password = driver.find_element(By.XPATH, "//input[@id='password']")
user_password.send_keys("secret_sauce")

# Находим кнопку логина по ID и нажимаем её
login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
login_button.click()

# Ждём немного, чтобы увидеть результат
time.sleep(5)
# Закрываем окно браузера
driver.close()
