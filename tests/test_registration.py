from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import AuthLocators
from urls import Urls
from helpers import generate_login, generate_password


class TestRegistration:

    def test_successful_registration(self, driver):
        name = "Александра"
        email = generate_login()
        password = generate_password()

        driver.get(Urls.REGISTER_URL)

        driver.find_element(By.XPATH, AuthLocators.NAME_INPUT).send_keys(name)
        driver.find_element(By.XPATH, AuthLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(By.XPATH, AuthLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(By.XPATH, AuthLocators.REGISTER_BUTTON).click()

        # Маркер успешной регистрации: редирект на страницу /login
        is_redirected_to_login = WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Urls.LOGIN_URL))
        assert is_redirected_to_login
        assert driver.current_url == Urls.LOGIN_URL

    def test_registration_with_short_password_shows_error(self, driver):
        name = "Александра"
        email = generate_login()
        invalid_password = "123"

        driver.get(Urls.REGISTER_URL)

        driver.find_element(By.XPATH, AuthLocators.NAME_INPUT).send_keys(name)
        driver.find_element(By.XPATH, AuthLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(By.XPATH, AuthLocators.PASSWORD_INPUT).send_keys(invalid_password)
        driver.find_element(By.XPATH, AuthLocators.REGISTER_BUTTON).click()

        # На странице появляется текст ошибки «Некорректный пароль»
        error_element = driver.find_element(By.XPATH, AuthLocators.PASSWORD_ERROR)
        assert error_element.text == "Некорректный пароль"
