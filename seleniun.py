import time
# Импортируем основной модуль webdriver из библиотеки Selenium — он позволяет управлять браузером (в данном случае, Chrome).
from selenium import webdriver

# Импортируем класс Service, который управляет запуском ChromeDriver. Здесь мы переименовываем его в ChromeService для читаемости.
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService

# Импортируем менеджер, который автоматически скачивает и устанавливает нужную версию chromedriver. Это избавляет от необходимости делать это вручную.
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions() # Создаем объект настроек для браузера Chrome. Через него можно задать дополнительные параметры запуска (например, открыть в фоновом режиме, отключить уведомления и т.д.).
options.add_experimental_option("detach", True) # Устанавливаем параметр detach=True. Это значит, что окно браузера останется открытым после завершения работы скрипта Python.
options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# Сохраняем URL
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
