import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# Функция проверяет название и цену товара
def check_product(driver, name_xpath, expected_name, price_xpath, expected_price, context=""):
    actual_name = driver.find_element(By.XPATH, name_xpath).text
    print(actual_name)
    assert actual_name == expected_name
    print(f"{context} product name is OK")

    actual_price = driver.find_element(By.XPATH, price_xpath).text
    print(actual_price)
    assert actual_price == expected_price
    print(f"{context} product price is OK")

# Убираем знак $
def get_price_value(price_text):
    return float(price_text.strip('$'))

# Открываем браузер
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920, 1080)

# Логин и пароль
driver.find_element(By.ID, "user-name").send_keys("standard_user")
print('Input Login')
driver.find_element(By.ID, "password").send_keys("secret_sauce")
print('Input password')
driver.find_element(By.ID, "login-button").click()
print('Click Login button')

# Создаем переменную первого и второго товара
product_1_name = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']").text
print(product_1_name)
product_1_price = driver.find_element(By.XPATH, "(//*[@class='inventory_item_price'])[1]").text
print(product_1_price)
product_2_name = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']").text
print(product_2_name)
product_2_price = driver.find_element(By.XPATH, "(//*[@class='inventory_item_price'])[2]").text
print(product_2_price)
time.sleep(2)

# Добавляем товары в корзину
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
print('Added product 1 and 2 in cart')
time.sleep(2)

# Переход в корзину
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
print('Enter in cart')
time.sleep(2)

# Проверка товаров в корзине
check_product(driver,
              "//*[@id='item_4_title_link']", product_1_name,
              "//*[@id='cart_contents_container']//div[3]/div[2]/div[2]/div", product_1_price,
              context="Cart Product 1")
check_product(driver,
              "//*[@id='item_0_title_link']", product_2_name,
              "//*[@id='cart_contents_container']//div[4]/div[2]/div[2]/div", product_2_price,
              context="Cart Product 2")

# Заполняем поля имя, фамилия, индекс
driver.find_element(By.ID, "checkout").click()
driver.find_element(By.ID, "first-name").send_keys("John")
driver.find_element(By.ID, "last-name").send_keys("Doe")
driver.find_element(By.ID, "postal-code").send_keys("12345")
driver.find_element(By.ID, "continue").click()
print('Input: Name, Surname and post code')
print('Click Continue')

# Проверка товаров на финальной странице
check_product(driver,
              "//*[@id='item_4_title_link']", product_1_name,
              "//*[@id='checkout_summary_container']//div[3]/div[2]/div[2]/div", product_1_price,
              context="Finish Product 1")

check_product(driver,
              "//*[@id='item_0_title_link']", product_2_name,
              "//*[@id='checkout_summary_container']//div[4]/div[2]/div[2]/div", product_2_price,
              context="Finish Product 2")

# Проверка итоговой суммы
summary_price_text = driver.find_element(By.XPATH,
    "//*[@id='checkout_summary_container']/div/div[2]/div[6]").text

total_price = get_price_value(product_1_price) + get_price_value(product_2_price)
expected_item_total = f"Item total: ${total_price}"

print(summary_price_text)
print(expected_item_total)
assert summary_price_text == expected_item_total
print("Total summary price is OK")

time.sleep(2)
driver.quit()
