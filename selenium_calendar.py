import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.set_window_size(1920, 1080)

date_input = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
date_input.send_keys(Keys.COMMAND + 'a')
date_input.send_keys(Keys.DELETE)

time.sleep(4)
current_date = datetime.now().strftime("%08.%27.%2025")
date_input.send_keys(current_date)
