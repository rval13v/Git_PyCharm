import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Создаем общий класс
class Test(): #создаем метод и помещаем в него выызов д-ра, url и открытие страницы
    def __init__(self): # коструктор класса чтобы создать и сохранить экземпляр браузера сразу при создании объекта класса. все методы могцт использоывать один браузер
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.base_url = 'https://www.saucedemo.com/'

    def test_select_product(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(2)

    def login(self):
        user_name = self.driver.find_element(By.XPATH, "//input[@id='user-name']")
        user_name.send_keys("standard_user")
        user_password = self.driver.find_element(By.XPATH, "//input[@id='password']")
        user_password.send_keys("secret_sauce")
        login_button = self.driver.find_element(By.XPATH, "//input[@id='login-button']")
        login_button.click()

    def quit_driver(self):
        self.driver.quit()

# Создаем экземпляр класса
start_test = Test()
start_test.test_select_product()  # открываем страницу
start_test.login()
start_test.quit_driver()
