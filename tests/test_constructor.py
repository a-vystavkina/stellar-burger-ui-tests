from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainPageLocators
from urls import Urls

class TestConstructor:

    def test_switch_to_sauces_tab(self, driver):
        driver.get(Urls.BASE_URL)

        # Клик по вкладке «Соусы»
        driver.find_element(By.XPATH, MainPageLocators.SAUCES_TAB).click()

        # Явное ожидание: проверяем, что в атрибуте class вкладки появился класс активной вкладки
        is_active = WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element_attribute((By.XPATH, MainPageLocators.SAUCES_TAB), "class", "tab_tab_type_current"))
        assert is_active

    def test_switch_to_fillings_tab(self, driver):
        driver.get(Urls.BASE_URL)

        # Клик по вкладке «Начинки»
        driver.find_element(By.XPATH, MainPageLocators.FILLINGS_TAB).click()

        # Явное ожидание: проверяем, что в атрибуте class вкладки появился класс активной вкладки
        is_active = WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element_attribute((By.XPATH, MainPageLocators.FILLINGS_TAB), "class", "tab_tab_type_current"))
        assert is_active

    def test_switch_to_buns_tab(self, driver):
        driver.get(Urls.BASE_URL)

        # Сначала переключаемся на «Соусы», чтобы активной стала другая вкладка
        driver.find_element(By.XPATH, MainPageLocators.SAUCES_TAB).click()
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element_attribute((By.XPATH, MainPageLocators.SAUCES_TAB), "class", "tab_tab_type_current"))

        # Кликаем обратно на «Булки»
        driver.find_element(By.XPATH, MainPageLocators.BUNS_TAB).click()

        # Явное ожидание: проверяем, что в атрибуте class вкладки «Булки» снова появился класс активной вкладки
        is_active = WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element_attribute((By.XPATH, MainPageLocators.BUNS_TAB), "class", "tab_tab_type_current"))
        assert is_active