import glob
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# Указываем путь в папку для скачаивания
path_download = "//Users//ravilvaliev//PycharmProjects//Git_PyCharm//Files_download"

options = webdriver.ChromeOptions()
# Конструкция, чтобы файл скачавался по умолчанию в нашу папку
prefs = {'download.default_directory' : path_download}
options.add_experimental_option('prefs', prefs)
options.add_experimental_option("detach", True)
#options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

base_url = 'https://www.lambdatest.com/selenium-playground/download-file-demo'
driver.get(base_url)
driver.set_window_size(1920, 1080)
time.sleep(5)
# Кликаем по кнопке download
click_button1 = driver.find_element(By.XPATH, "//button[contains(text(), 'Download File')]")
click_button1.click()
time.sleep(6)

# Проверка, что файл скачался в нашу директорию
file_name = "LambdaTest.pdf"
file_path = os.path.join(path_download, file_name)
assert os.access(file_path, os.F_OK) == True
print("File in directory")

# С помощью цикла проверяем размер скачанного файла
files = glob.glob(os.path.join(path_download, "*.*"))
for file in files:
    a = os.path.getsize(file)
    if a > 10:
        print("File good")
    else:
        print("File empty")

# Удаляем файл из директории
files = glob.glob(os.path.join(path_download, "*.*"))
for file in  files:
    os.remove(file)
