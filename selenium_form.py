import time

from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
base_url = 'https://lambdatest.com/selenium-playground/simple-form-demo'
driver.get(base_url)
driver.set_window_size(1920, 1080)

# Локатор к поисковом полю
input_message = driver.find_element(By.XPATH, "//input[@id='user-message']")

# Создаем переменную
message = 'Hello World'

# Передаем переменную с помощью метода input
input_message.send_keys(message)

# Кликаем по кнопке отправить
click_button = driver.find_element(By.XPATH, "//button[@id='showInput']")
click_button.click()
# пауза
time.sleep(3)

# сохранили в переменную сообщение
your_message = driver.find_element(By.XPATH, "//p[@id='message']")
value_message = your_message.text
assert value_message == message
print('ok')

# Создаем переменные
first_value = 1001
second_value = 3323
sum_result = first_value + second_value

# Локатор для первого и второго значения
input_first_value = driver.find_element(By.XPATH, "//input[@id='sum1']")
input_first_value.send_keys(first_value)
input_first_value = driver.find_element(By.XPATH, "//input[@id='sum2']")
input_first_value.send_keys(second_value)

# Нажатие на кнопку
click_button2 = driver.find_element(By.XPATH, "//*[@id='gettotal']/button")
click_button2.click()
time.sleep(3)

#создаем переменную результата и проверяем
result = driver.find_element(By.XPATH, "//p[@id='addmessage']")
value_result = result.text
assert value_result == str(sum_result)
print('ok2')
