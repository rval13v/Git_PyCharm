import glob
import os
import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
driver.set_window_size(1920, 1080)

# неявное ожидание - применяется при динамически загружаемых элементах на странице (временная задержка для поиска элемента)т
# driver.implicitly_wait(10)
#
# print('Start test')
# visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
# visible_button.click()
# print('Test finish')

# Явное ожид  позволяет дождаться элемента (определенного условия перед продолжением работы)
print('Start test')
visible_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='visibleAfter']")))
visible_button.click()
print('Test finish')

driver.quit()