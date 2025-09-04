import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

base_url = 'https://the-internet.herokuapp.com/javascript_alerts'
driver.get(base_url)
driver.set_window_size(1920, 1080)
time.sleep(5)

#алерт с одногй кнопкой подтверждения
click_alert_button = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
click_alert_button.click()
print("click_alert_button")
time.sleep(3)
driver.switch_to.alert.accept()

# алерт где выбираем подтвердить либо отменить
time.sleep(4)
click_alert_button = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
click_alert_button.click()
print("click_alert_button")
time.sleep(3)
driver.switch_to.alert.dismiss()

# есть поле ввода текста и кнопки подтв или отмены
time.sleep(4)
click_alert_button = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
click_alert_button.click()
print("click_alert_button")
time.sleep(3)
driver.switch_to.alert.send_keys("Hello")
driver.switch_to.alert.accept()

