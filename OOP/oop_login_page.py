from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def autorization(self, login_name, login_password):
        user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='user-name']")))
        user_name.send_keys(login_name)
        print("Input user name")

        user_password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='password']")))
        user_password.send_keys(login_password)
        print("Input password")

        login_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='login-button']")))
        login_button.click()
        print("Click login button")