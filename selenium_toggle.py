import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
base_url = ' https://html5css.ru/howto/howto_js_rangeslider.php'
driver.get(base_url)
driver.set_window_size(1920, 1080)

actions = ActionChains(driver)
slider = driver.find_element(By.XPATH, "//input[@class='slider-color']")

time.sleep(5)

actions.click_and_hold(slider).move_by_offset(-500, 0).release().perform()

# Проверяем input
check_slider = driver.find_element(By.ID, "f")
value_check_slider = check_slider.text
assert value_check_slider == '11'
print("slider is moved")
