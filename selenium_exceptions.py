import glob
import os
import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
driver.set_window_size(1920, 1080)
time.sleep(1)
# button_visible = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
# button_visible.click()

# Отлавливаем ошибку, пока кнопка не появилась
try:
    button_visible = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
    button_visible.click()
except NoSuchElementException:
    print('Получили NoSuchElementException')
    time.sleep(5)
    driver.refresh()
    time.sleep(5)
    # Повторно пробуем найти элемент и кликнуть по нему
    button_visible = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
    button_visible.click()
    print('Click button visible')