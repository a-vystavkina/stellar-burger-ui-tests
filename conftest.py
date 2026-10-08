import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from helpers import generate_login, generate_password
from locators import AuthLocators
from urls import Urls


@pytest.fixture
def driver():
    # Инициализация браузера Google Chrome
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    browser = webdriver.Chrome(service=service, options=options)

    # Неявное ожидание для поиска элементов
    browser.implicitly_wait(10)

    yield browser

    # Закрытие браузера после каждого теста
    browser.quit()


@pytest.fixture
def registered_user(driver):
    """
    Фикстура для создания нового пользователя перед тестом.
    Возвращает словарь с именем, email и паролем.
    """
    user_name = "Александра"
    user_email = generate_login()
    user_password = generate_password()

    driver.get(Urls.REGISTER_URL)
    driver.find_element(By.XPATH, AuthLocators.NAME_INPUT).send_keys(user_name)
    driver.find_element(By.XPATH, AuthLocators.EMAIL_INPUT).send_keys(user_email)
    driver.find_element(By.XPATH, AuthLocators.PASSWORD_INPUT).send_keys(user_password)
    driver.find_element(By.XPATH, AuthLocators.REGISTER_BUTTON).click()

    # Ждём перехода на страницу логина
    driver.find_element(By.XPATH, AuthLocators.LOGIN_BUTTON)

    return {
        "name": user_name,
        "email": user_email,
        "password": user_password
    }
