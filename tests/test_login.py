from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import AuthLocators, HeaderLocators, MainPageLocators
from urls import Urls


class TestLogin:

    def test_login_from_main_page_button(self, driver, registered_user):
        driver.get(Urls.BASE_URL)

        # Клик по кнопке «Войти в аккаунт» на главной странице
        driver.find_element(By.XPATH, MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()

        # Ввод почты и пароля, клик по кнопке «Войти»
        driver.find_element(By.XPATH, AuthLocators.EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(By.XPATH, AuthLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(By.XPATH, AuthLocators.LOGIN_BUTTON).click()

        # Проверяем, что кнопка «Оформить заказ» отображается на странице
        order_button = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, MainPageLocators.CREATE_ORDER_BUTTON)))
        assert order_button.is_displayed()

    def test_login_from_header_account_button(self, driver, registered_user):
        driver.get(Urls.BASE_URL)

        # Клик по кнопке «Личный Кабинет» в шапке
        driver.find_element(By.XPATH, HeaderLocators.ACCOUNT_BUTTON).click()

        # Ввод данных и вход
        driver.find_element(By.XPATH, AuthLocators.EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(By.XPATH, AuthLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(By.XPATH, AuthLocators.LOGIN_BUTTON).click()

        # Проверяем успешный вход
        order_button = driver.find_element(By.XPATH, MainPageLocators.CREATE_ORDER_BUTTON)
        assert order_button.text == "Оформить заказ"

    def test_login_from_registration_page_link(self, driver, registered_user):
        driver.get(Urls.REGISTER_URL)

        # Клик по ссылке «Войти» на странице регистрации
        driver.find_element(By.XPATH, AuthLocators.LOGIN_LINK_ON_REGISTER_PAGE).click()

        # Ввод данных и вход
        driver.find_element(By.XPATH, AuthLocators.EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(By.XPATH, AuthLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(By.XPATH, AuthLocators.LOGIN_BUTTON).click()

        # Проверяем успешный вход
        order_button = driver.find_element(By.XPATH, MainPageLocators.CREATE_ORDER_BUTTON)
        assert order_button.text == "Оформить заказ"

    def test_login_from_forgot_password_page_link(self, driver, registered_user):
        driver.get(Urls.FORGOT_PASSWORD_URL)

        # Клик по ссылке «Войти» на странице восстановления пароля
        driver.find_element(By.XPATH, AuthLocators.LOGIN_LINK_ON_FORGOT_PASSWORD_PAGE).click()

        # Ввод данных и вход
        driver.find_element(By.XPATH, AuthLocators.EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(By.XPATH, AuthLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(By.XPATH, AuthLocators.LOGIN_BUTTON).click()

        # Проверяем успешный вход
        order_button = driver.find_element(By.XPATH, MainPageLocators.CREATE_ORDER_BUTTON)
        assert order_button.text == "Оформить заказ"
