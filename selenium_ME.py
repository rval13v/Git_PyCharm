import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Создаем экземпляр браузера Edge
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# Сохраняем URL-адрес сайта в переменную base_url.
base_url = 'https://www.saucedemo.com/'
driver.get(base_url) #  Открываем браузер и переходим по адресу, указанному в base_url.

# Устанавливаем размер окна браузера
driver.set_window_size(1920, 1080)
time.sleep(5)
driver.close() # Закрываем окно браузера
