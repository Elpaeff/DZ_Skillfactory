from tkinter.font import names

import pytest
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')

    yield driver

    driver.quit()


def test_show_all_pets(driver):


    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('vasya@mail.com')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('12345')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

     # ожидаем нужный элемент


    # Проверяем на наличие имен, возраста и картинок
    driver.implicitly_wait(20)
    images = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')



    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0
def test_my_pets(driver):
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('vasya@mail.com')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('12345')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@class="card"][3]')))

    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    driver.find_element(By.XPATH,'// span[ @class ="navbar-toggler-icon"]').click()
    driver.find_element(By.XPATH,'//a[contains(text(), "Мои питомцы")]').click()

    names_pets = driver.find_elements(By.XPATH, '//tr/td[1]')
    breed_pets = driver.find_elements(By.XPATH, '//tr/td[2]')
    age_pets = driver.find_elements(By.XPATH, '//tr/td[3]')
    str_foto_pets = driver.find_elements(By.XPATH, '//tr//img')
    no_foto_pets = driver.find_elements(By.XPATH, '//tr//img[@src=""]')
    number_of_pets = driver.find_element(By.XPATH, '//div[contains(@class, "col-sm-4 left")]').text
    split_namber_of_pets = int(re.split(": |\n", number_of_pets)[2])
    #по name проверяем чт околичество строк равно количеству питомцев указанного на странице под именем
    assert split_namber_of_pets ==  len(names_pets)
    # проверяем, что количество картачек с фото больше либо равно 50%
    assert int(split_namber_of_pets) >= ((len(str_foto_pets)) - (len(no_foto_pets)))/2
    for i in range(split_namber_of_pets):
        for j in range(split_namber_of_pets):
            pets_i =[names_pets[i].text, breed_pets[i].text, age_pets[i].text]
            pets_j =[names_pets[j].text, breed_pets[j].text, age_pets[j].text]
            if j != i:
                assert pets_i != pets_j













