import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

base_url = 'https://demoqa.com/browser-windows'
driver.get(base_url)
driver.set_window_size(1920, 1080)
time.sleep(5)

new_tab = driver.find_element(By.XPATH, "//button[@id='tabButton']")
new_tab.click()
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])


time.sleep(4)
# создали переменную
new_window= driver.find_element(By.XPATH, "//button[@id='windowButton']")
new_window.click()
# Переключене между окнами
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])

