import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

base_url = 'https://demoqa.com/checkbox'
driver.get(base_url)
driver.set_window_size(1920, 1080)

checkbox = driver.find_element(By.XPATH, "//label[@for='tree-node-home']")
checkbox.click()

# Проверяем input
checkbox_input = driver.find_element(By.ID, "tree-node-home")
assert checkbox_input.is_selected()
print("Checkbox is selected")