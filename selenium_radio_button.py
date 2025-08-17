import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)
driver.set_window_size(1920, 1080)

radio_button = driver.find_element(By.XPATH, "(//label[@class='custom-control-label'])[2]")
radio_button.click()

# Проверяем input
radio_input = driver.find_element(By.ID, "impressiveRadio")
assert radio_input.is_selected()
print("Radio button is selected")

test = driver.find_element(By.XPATH, "//span[@class='text-success']")
value_text = test.text
assert value_text == 'Impressive'
print('radio-button is activity!!!')




