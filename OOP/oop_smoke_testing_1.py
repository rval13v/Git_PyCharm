import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from oop_login import USER_NAME, PASSWORD, LOGIN_BUTTON


class Test: #создаем метод и помещаем в него выызов д-ра, url и открытие страницы
    def __init__(self): # коструктор класса чтобы создать и сохранить экземпляр браузера сразу при создании объекта класса. все методы могцт использоывать один браузер
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.base_url = 'https://www.saucedemo.com/'

    def open_browser(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(2)

        print("Start test")

    def login(self):
        user_name_field = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(USER_NAME))
        user_name_field.send_keys("standard_user")
        print("Input user name")

        user_password_field = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(PASSWORD))
        user_password_field.send_keys("secret_sauce")
        print("Input password")

        login_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(LOGIN_BUTTON))
        login_button.click()
        print("Click login button")

    def choice_product(self):
        select_product = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")))
        select_product.click()
        print("Click select product")

    def enter_to_cart(self):
        enter_cart = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='shopping_cart_container']/a")))
        enter_cart.click()
        print('Enter in cart')

    def check_cart(self):
        check_cart = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
        value_check_cart = check_cart.text
        assert value_check_cart == 'Your Cart'

    def quit_driver(self):
        self.driver.quit()

# Создаем экземпляр класса
start_test = Test()
start_test.open_browser()  # открываем страницу
start_test.login()
start_test.choice_product()
start_test.enter_to_cart()
start_test.check_cart()
start_test.quit_driver()