import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

# Настройки браузера
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Оставляем окно открытым после завершения
# options.add_argument("--headless")  # Для фонового запуска

# Запуск браузера
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920, 1080)

# Авторизация
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys("standard_user")
user_password = driver.find_element(By.XPATH, "//input[@id='password']")
user_password.send_keys("secret_sauce")
login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
login_button.click()

print("\nПриветствую тебя в нашем интернет-магазине!")

# Список товаров
products = {
    "1": {"desc": "Sauce Labs Backpack", "locator": (By.XPATH, "//*[@id='item_4_title_link']")},
    "2": {"desc": "Sauce Labs Bike Light", "locator": (By.XPATH, "//*[@id='item_0_title_link']")},
    "3": {"desc": "Sauce Labs Bolt T-Shirt", "locator": (By.XPATH, "//*[@id='item_1_title_link']")},
    "4": {"desc": "Sauce Labs Fleece Jacket", "locator": (By.XPATH, "//*[@id='item_5_title_link']")},
    "5": {"desc": "Sauce Labs Onesie", "locator": (By.XPATH, "//*[@id='item_2_title_link']")},
    "6": {"desc": "Test.allTheThings() T-Shirt (Red)", "locator": (By.XPATH, "//*[@id='item_3_title_link']")}
}

def main():
    while True:
        print("Товары:")
        for key, item in products.items():
            print(f"{key}. {item['desc']}")

        choice = input("\nВыберите номер товара (или 0 для выхода): ").strip()

        if choice == "0":
            print("Выход из программы.")
            return None
        elif choice in products:
            item = products[choice]
            print(f"Вы выбрали: {item['desc']}")
            confirm = input("Вы точно выбрали этот товар? (y/n): ").strip().lower()
            if confirm == "y":
                click_choice = driver.find_element(*item["locator"])
                click_choice.click()
                # Ждём появления цены
                wait = WebDriverWait(driver, 10)
                price_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_details_price")))
                price = price_element.text

                add_to_cart = input(f"Цена {price}. Добавить этот товар в корзину? (y/n): ").strip().lower()
                if add_to_cart == "y":
                    click_add_to_cart = driver.find_element(By.XPATH, "//button[text()='Add to cart']")
                    click_add_to_cart.click()
                    print("Товар добавлен в корзину.")
                return {"name": item['desc'], "price": price}
            else:
                print("Выберите другой товар.")
        else:
            print("Неверный выбор. Повторите ввод.")

selected_item = main()

if selected_item is not None:
    # Переход в корзину
    click_cart = driver.find_element(By.ID, "shopping_cart_container")
    click_cart.click()
    time.sleep(1)

    print("\nПроверяем корзину...")
    cart_name = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    value_cart_name = cart_name.text
    cart_price = driver.find_element(By.CLASS_NAME, "inventory_item_price")
    value_cart_price = cart_price.text

    assert value_cart_name == selected_item['name']
    assert value_cart_price == selected_item['price']
    print("Проверка пройдена: товар и цена совпадают!")

    # Кликаем кнопку Checkout
    checkout = driver.find_element(By.XPATH, "//*[@id='checkout']")
    checkout.click()
    print('Click checkout')

    # Заполняем поля имя, фамилия, индекс Faker
    # указываем язык
    fake = Faker("en_US")

    # генерирует случайное имя
    name = fake.first_name()
    first_name = driver.find_element(By.XPATH, "//*[@id='first-name']")
    first_name.send_keys(name)
    print('Input first name')
    # генерирует случайную фамилию
    surname = fake.last_name()
    second_name = driver.find_element(By.XPATH, "//*[@id='last-name']")
    second_name.send_keys(surname)
    print('Input second name')
    # генерирует случайный посткод
    zip_code = fake.postcode()
    post_code = driver.find_element(By.XPATH, "//*[@id='postal-code']")
    post_code.send_keys(zip_code)
    print('Input post code')

    # Жмем продолжить
    button_continue = driver.find_element(By.XPATH, "//*[@id='continue']").click()
    print('Click continue')

    # Финальная проверка товара и цены
    finish_product = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    value_finish_product = finish_product.text
    assert value_finish_product == selected_item['name']
    print('Info finish product is good')

    price_finish_product = driver.find_element(By.CLASS_NAME, "inventory_item_price")
    value_price_finish_product = price_finish_product.text
    assert value_price_finish_product == selected_item['price']
    print('Info finish price product is good')

    summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
    value_summary_price = summary_price.text
    total_price = float(value_price_finish_product.strip('$'))
    item_total = f"Item total: ${total_price:.2f}"
    print(item_total)
    assert value_summary_price == item_total
    print('Total summary price is OK')

    button_finish = driver.find_element(By.XPATH, "//*[@id='finish']").click()
    print('Click finish button')

    checkout_complete = driver.find_element(By.XPATH, "//*[contains(text(), 'Checkout: Complete!')]")
    value_checkout_complete = checkout_complete.text
    print(value_checkout_complete)
    assert value_checkout_complete == 'Checkout: Complete!'
    print('Checkout: Complete!')

    # Закрываем браузер
    # driver.quit()