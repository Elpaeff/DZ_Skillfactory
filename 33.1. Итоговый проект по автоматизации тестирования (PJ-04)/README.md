33.1. Итоговый проект по автоматизации тестирования (PJ-04)

Тестирование WEB интерфейса страницы авторизации "Ростелеком" https://b2c.passport.rt.ru/
при тестировании страницы регистрации используется 2 технитки тест дизайна:
 - "Пограничные значения" -  тесткейсы PJ04_13, PJ04_15
 - "Эквивалентные значения" - тесткейсы  PJ04_14, PJ04_15, PJ04_17
  данные техники применены чтобы проверить требования тех задания для элементов ввода фамилии и имени,где указано, 
     что Необходимо заполнить поле кириллицей. От 2 до 30 символов."

Остальные тесткейсы прверяют элементы управления (кнопки, ссылки)

тест кейсы - https://docs.google.com/spreadsheets/d/1Y1AFrI68JjzaVRHEVKh01LeMtvYDyycm83t_iBls-VY/edit?usp=sharing
баг репорты - https://docs.google.com/spreadsheets/d/1yyabyJ4ZktLF1OBZ2f53qDd0kPzFf-aD2_VpZ2PAI3c/edit?usp=sharing


Автотесты разбиты на 2 файла 

test_auth_page.py - тестирует элементы интерфейса на странице "Авторизации"
test_reg_page.py - тестирует элементы интерфейса на странице "Регистрации"

для коректной работы автотестов должен быть установлены фрейворки:
pytest
selenium 


Автотесты составлены методом ООП, используется патерн PageObject

Запуск Автотестов на странице "Авторизации"
python -m pytest -v --driver Chrome --driver-path M:/chromedriver/chromedriver.exe  tests/test_auth_page.py 
(M:/chromedriver/chromedriver.exe - путь к хром драйверу. при запуске на другой машине  заменить на актуальный WEBdriver)
8 автотестов


Запуск Автотестов на странице "Регистрации"
python -m pytest -v --driver Chrome --driver-path M:/chromedriver/chromedriver.exe  tests/test_reg_page.py
(M:/chromedriver/chromedriver.exe - путь к хром драйверу. при запуске на другой машине  заменить на актуальный WEBdriver)
4 автотеста

