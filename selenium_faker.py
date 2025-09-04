import time
from faker import Faker
from selenium.webdriver import ActionChains, Keys
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

time.sleep(3)

# указываем язык
fake = Faker("en_US")

# генерирует случайное имя
name = fake.first_name()
# Заполняем сгенерированным именем поле user_name
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(name)
print("input login")
