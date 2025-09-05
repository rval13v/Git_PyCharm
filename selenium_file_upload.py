import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

base_url = 'https://www.lambdatest.com/selenium-playground/upload-file-demo'
driver.get(base_url)
driver.set_window_size(1920, 1080)
time.sleep(5)

path_upload = "//Users//ravilvaliev//PycharmProjects//Git_PyCharm//file_upload//screen.png"
click_button = driver.find_element(By.XPATH, "//input[@id='file']")
click_button.send_keys(path_upload)

check_upload = driver.find_element(By.XPATH, "//input[@id='file']")
value_check_upload = check_upload.get_attribute("value")
assert value_check_upload.endswith("screen.png")
print("Файл загружен")

driver.quit()