from selenium import webdriver #Импортируем основной модуль webdriver из библиотеки Selenium — он позволяет управлять браузером (в данном случае, Chrome).
from selenium.webdriver.chrome.service import Service as ChromeService #Импортируем класс Service, который управляет запуском ChromeDriver. Здесь мы переименовываем его в ChromeService для читаемости.
from webdriver_manager.chrome import ChromeDriverManager # Импортируем менеджер, который автоматически скачивает и устанавливает нужную версию chromedriver. Это избавляет от необходимости делать это вручную.

options = webdriver.ChromeOptions() #Создаем объект настроек для браузера Chrome. Через него можно задать дополнительные параметры запуска (например, открыть в фоновом режиме, отключить уведомления и т.д.).
options.add_experimental_option("detach", True) #Устанавливаем параметр detach=True. Это значит, что окно браузера останется открытым после завершения работы скрипта Python.

#Создаем экземпляр браузера Chrome: options=options — применяем заданные настройки,ervice=... — указываем, как запускать chromedriver (с использованием автоматически установленного драйвера через ChromeDriverManager).
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = 'https://www.saucedemo.com/' #Сохраняем URL-адрес сайта в переменную base_url.
driver.get(base_url) #Открываем браузер и переходим по адресу, указанному в base_url.
driver.set_window_size(1920, 1080) #Устанавливаем размер окна браузера вручную, можно применить макс разр. driver.maximize_window()
