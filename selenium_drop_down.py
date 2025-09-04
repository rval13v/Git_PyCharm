import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
base_url = 'https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo'
driver.get(base_url)
driver.set_window_size(1920, 1080)

click_drop = driver.find_element(By.XPATH, "//span[@aria-labelledby='select2-country-container']")
click_drop.click()
time.sleep(1)
select_country = driver.find_element(By.XPATH, "(//li[@class='select2-results__option'])[1]")
select_country.click()



# input_country = driver.find_element(By.XPATH, "(//input[@class='select2-search__field'])[2]")
#input_country.send_keys('Australia')
# input_country.send_keys(Keys.RETURN)
