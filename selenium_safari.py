from selenium import webdriver
import time

# Создаем драйвер Safari
driver = webdriver.Safari()

# Сохраняем URL-адрес сайта в переменную base_url.
base_url = 'https://www.saucedemo.com/'

# Открываем страницу
driver.get(base_url)

# Устанавливаем размер окна браузера
driver.set_window_size(1920, 1080)
time.sleep(5)
driver.close()# Закрываем окно браузера
