class BasePage(object):
   # конструктор класса - специальный метод с ключевым словом __init__
   # Нам нужны объект веб-драйвера, адрес страницы и время ожидания элементов
   def __init__(self, driver, url, timeout=10):
       self.driver = driver
       self.url = url
       self.driver.implicitly_wait(timeout)

