import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

base_url = 'https://demoqa.com/buttons'
driver.get(base_url)
driver.set_window_size(1920, 1080)

action = ActionChains(driver)
double_click_button = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
action.double_click(double_click_button).perform()
print('Двойной клик')

time.sleep(3)
right_click_button = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
action.context_click(right_click_button).perform()
print('Клик правой кнопкой')

test_double_click = driver.find_element(By.XPATH, "//*[@id = 'doubleClickMessage']")
value_test_double_click = test_double_click.text
assert value_test_double_click == 'You have done a double click'
print('Double click')

test_right_click = driver.find_element(By.XPATH, "//*[@id = 'rightClickMessage']")
value_test_right_click = test_right_click.text
assert value_test_right_click == 'You have done a right click'
print('Right click')