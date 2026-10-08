class AuthLocators:
    # Поле ввода имени (страница регистрации)
    NAME_INPUT = "//label[text()='Имя']/following-sibling::input"

    # Поле ввода email
    EMAIL_INPUT = "//label[text()='Email']/following-sibling::input"

    # Поле ввода пароля
    PASSWORD_INPUT = "//label[text()='Пароль']/following-sibling::input"

    # Кнопка «Зарегистрироваться»
    REGISTER_BUTTON = "//button[text()='Зарегистрироваться']"

    # Сообщение об ошибке некорректного пароля («Некорректный пароль»)
    PASSWORD_ERROR = "//p[contains(@class, 'input__error') and text()='Некорректный пароль']"

    # Кнопка «Войти» на форме авторизации
    LOGIN_BUTTON = "//button[text()='Войти']"

    # Ссылка «Войти» на странице регистрации
    LOGIN_LINK_ON_REGISTER_PAGE = "//a[contains(@class, 'Auth_link') and text()='Войти' and @href='/login']"

    # Ссылка «Войти» на странице восстановления пароля
    LOGIN_LINK_ON_FORGOT_PASSWORD_PAGE = "//a[contains(@class, 'Auth_link') and text()='Войти' and @href='/login']"


class HeaderLocators:
    # Кнопка / ссылка «Конструктор» в шапке
    CONSTRUCTOR_BUTTON = "//p[text()='Конструктор']/ancestor::a"

    # Логотип «Stellar Burgers» в шапке
    LOGO = "//header//a[@href='/']"

    # Кнопка «Личный Кабинет» в шапке
    ACCOUNT_BUTTON = "//p[text()='Личный Кабинет']/ancestor::a"


class MainPageLocators:
    # Кнопка «Войти в аккаунт» на главной странице
    LOGIN_ACCOUNT_BUTTON = "//button[text()='Войти в аккаунт']"

    # Кнопка «Оформить заказ» (появляется после успешного входа)
    CREATE_ORDER_BUTTON = "//button[text()='Оформить заказ']"

    # Заголовок «Соберите бургер»
    CONSTRUCTOR_TITLE = "//h1[text()='Соберите бургер']"

    # Вкладка «Булки»
    BUNS_TAB = "//span[text()='Булки']/ancestor::div[contains(@class, 'tab_tab')]"

    # Вкладка «Соусы»
    SAUCES_TAB = "//span[text()='Соусы']/ancestor::div[contains(@class, 'tab_tab')]"

    # Вкладка «Начинки»
    FILLINGS_TAB = "//span[text()='Начинки']/ancestor::div[contains(@class, 'tab_tab')]"


class ProfileLocators:
    # Ссылка «Профиль» в личном кабинете
    PROFILE_LINK = "//a[contains(@class, 'Account_link') and text()='Профиль']"

    # Кнопка «Выход» в личном кабинете
    LOGOUT_BUTTON = "//button[text()='Выход']"
