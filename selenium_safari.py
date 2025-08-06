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

# Здесь происходит поиск элемента на веб-странице по его атрибуту id, который равен "user-name".
user_name = driver.find_element(By.ID, "user-name")

# В это поле (user_name) вводится текст "standard_user". Это логин для тестового аккаунта.
user_name.send_keys("standard_user")

#Аналогично, находится поле ввода пароля по id="password", и элемент сохраняется в переменную user_password.
user_password = driver.find_element(By.ID, "password")
user_password.send_keys("secret_sauce")

# Находим оп id кнопку Логин и кликаем ее.
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# time.sleep(5)
# driver.close()# Закрываем окно браузера
