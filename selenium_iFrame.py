import time
from selenium.webdriver import ActionChains, Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
base_url = 'https://www.lambdatest.com/selenium-playground/iframe-demo/'
driver.get(base_url)
driver.set_window_size(1920, 1080)

iframe = driver.find_element(By.XPATH, "//iframe[@id='iFrame1']")
driver.switch_to.frame(iframe)

input_pole = driver.find_element(By.XPATH, "//*[@id='__next']/div/div[2]")

# Выделеяем, удаляем старое значение в поле и пишем новое
input_pole.send_keys(Keys.COMMAND, 'a')
input_pole.send_keys(Keys.DELETE)
time.sleep(2)
input_pole.send_keys("Green tree")
value_pole = input_pole.text
print(value_pole)

time.sleep(2)
# Выделяем новый текст и жмем на кнопку курсив и перечеркивания
input_pole.send_keys(Keys.COMMAND, 'a')
click_editing_panel_italic = driver.find_element(By.XPATH, "//button[@title= 'Italic']")
click_editing_panel_italic.click()
print('Click italic button')
click_editing_panel_strike = driver.find_element(By.XPATH, "//button[@title= 'Strike through']")
click_editing_panel_strike.click()
print('Click strike button')

time.sleep(2)
# Проверка
new_input_pole = driver.find_element(By.XPATH, "//*[@id='__next']/div/div[2]/i")
value_input_pole = new_input_pole.text
print(value_input_pole)
assert value_pole == value_input_pole
print('ok')





