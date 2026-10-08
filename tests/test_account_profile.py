from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import AuthLocators, HeaderLocators, ProfileLocators, MainPageLocators
from urls import Urls


class TestAccountProfile:

    def test_go_to_account_profile_by_click_account_button(self, driver, registered_user):
        # Авторизуемся
        driver.get(Urls.LOGIN_URL)
        driver.find_element(By.XPATH, AuthLocators.EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(By.XPATH, AuthLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(By.XPATH, AuthLocators.LOGIN_BUTTON).click()

        # Ждем загрузки главной страницы
        driver.find_element(By.XPATH, MainPageLocators.CREATE_ORDER_BUTTON)

        # Переход в Личный Кабинет
        driver.find_element(By.XPATH, HeaderLocators.ACCOUNT_BUTTON).click()

        # Проверяем, что отображается ссылка «Профиль» и URL соответствует личному кабинету
        profile_link = driver.find_element(By.XPATH, ProfileLocators.PROFILE_LINK)
        assert profile_link.text == "Профиль"
        assert driver.current_url == Urls.ACCOUNT_PROFILE_URL

    def test_go_from_account_to_constructor_by_click_constructor_button(self, driver, registered_user):
        # Авторизуемся и заходим в профиль
        driver.get(Urls.LOGIN_URL)
        driver.find_element(By.XPATH, AuthLocators.EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(By.XPATH, AuthLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(By.XPATH, AuthLocators.LOGIN_BUTTON).click()

        driver.find_element(By.XPATH, HeaderLocators.ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, ProfileLocators.PROFILE_LINK)

        # Клик по кнопке «Конструктор»
        driver.find_element(By.XPATH, HeaderLocators.CONSTRUCTOR_BUTTON).click()

        # Проверяем возврат в конструктор по отображению заголовка
        constructor_title = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, MainPageLocators.CONSTRUCTOR_TITLE)))
        assert constructor_title.is_displayed()
        assert driver.current_url == Urls.BASE_URL

    def test_go_from_account_to_constructor_by_click_logo(self, driver, registered_user):
        # Авторизуемся и заходим в профиль
        driver.get(Urls.LOGIN_URL)
        driver.find_element(By.XPATH, AuthLocators.EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(By.XPATH, AuthLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(By.XPATH, AuthLocators.LOGIN_BUTTON).click()

        driver.find_element(By.XPATH, HeaderLocators.ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, ProfileLocators.PROFILE_LINK)

        # Клик по логотипу
        driver.find_element(By.XPATH, HeaderLocators.LOGO).click()

        # Проверяем возврат в конструктор
        constructor_title = driver.find_element(By.XPATH, MainPageLocators.CONSTRUCTOR_TITLE)
        assert constructor_title.text == "Соберите бургер"
        assert driver.current_url == Urls.BASE_URL

    def test_logout_from_account(self, driver, registered_user):
        # Авторизуемся и заходим в профиль
        driver.get(Urls.LOGIN_URL)
        driver.find_element(By.XPATH, AuthLocators.EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(By.XPATH, AuthLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(By.XPATH, AuthLocators.LOGIN_BUTTON).click()

        driver.find_element(By.XPATH, HeaderLocators.ACCOUNT_BUTTON).click()

        # Клик по кнопке «Выход»
        driver.find_element(By.XPATH, ProfileLocators.LOGOUT_BUTTON).click()

        # Проверяем возврат на страницу логина
        login_button = driver.find_element(By.XPATH, AuthLocators.LOGIN_BUTTON)
        assert login_button.text == "Войти"
        assert driver.current_url == Urls.LOGIN_URL
