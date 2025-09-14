import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

        print("Start test")

    def login(self):
        user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='user-name']")))
        user_name.send_keys("standard_user")
        print("Input user name")

        user_password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='password']")))
        user_password.send_keys("secret_sauce")
        print("Input password")

        login_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='login-button']")))
        login_button.click()
        print("Click login button")

    def select_good(self):
        select_product = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")))
        select_product.click()
        print("Click select product")

    def enter_to_cart(self):
        enter_cart = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='shopping_cart_container']/a")))
        enter_cart.click()
        print('Enter in cart')

    def check_good_in_cart(self):
        check_cart = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
        value_check_cart = check_cart.text
        assert value_check_cart == 'Your Cart'
        print("test cart ok")

    def quit_driver(self):
        self.driver.quit()

# Создаем экземпляр класса
start_test = Test()
start_test.test_select_product()  # открываем страницу
start_test.login()
start_test.select_good()
start_test.enter_to_cart()
start_test.check_good_in_cart()
start_test.quit_driver()