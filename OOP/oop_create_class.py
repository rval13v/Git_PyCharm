import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Создаем общий класс
class Test(): #создаем метод и помещаем в него выызов д-ра, url и открытие страницы
    def test_select_product(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(2)

        user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
        user_name.send_keys("standard_user")
        user_password = driver.find_element(By.XPATH, "//input[@id='password']")
        user_password.send_keys("secret_sauce")
        login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
        login_button.click()
        time.sleep(2)

        driver.quit()

# Создаем экземпляр класса
start_test = Test()
start_test.test_select_product()  # открываем страницу
