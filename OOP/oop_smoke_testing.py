import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Создаем общий класс
class Test(): #создаем метод и помещаем в него выызов д-ра, url и открытие страницы
    def test_select_product(self):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()

        print("Start test")

        user_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='user-name']")))
        user_name.send_keys("standard_user")
        print("Input user name")

        user_password = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='password']")))
        user_password.send_keys("secret_sauce")
        print("Input password")

        login_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='login-button']")))
        login_button.click()
        print("Click login button")

        select_product = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")))
        select_product.click()
        print("Click select product")

        enter_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='shopping_cart_container']/a")))
        enter_cart.click()
        print('Enter in cart')

        check_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
        value_check_cart = check_cart.text
        assert value_check_cart == 'Your Cart'
        print("test cart ok")
        driver.quit()

# Создаем экземпляр класса
start_test = Test()
start_test.test_select_product()  # открываем страницу
