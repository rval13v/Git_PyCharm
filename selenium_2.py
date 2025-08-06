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
user_name.send_keys("standad_user")
print('Input Login')

user_password = driver.find_element(By.XPATH, "//input[@id='password']")
user_password.send_keys("secret_sauc")
print('Input password')

login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
login_button.click()
print('Click Login button')

time.sleep(5)
driver.refresh()
