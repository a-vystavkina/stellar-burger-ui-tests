# Проект автотестов UI для сервиса Stellar Burgers (Sprint 5)

Финальный проект спринта: автоматизация UI-тестирования веб-приложения Stellar Burgers с использованием Python, Selenium WebDriver и Pytest.

## Ссылка на сервис
[Stellar Burgers](https://stellarburgers.education-services.ru/)

## Структура проекта
```
Sprint_5/
├── tests/
│   ├── test_registration.py       # Тесты регистрации (успешная регистрация, ошибка короткого пароля)
│   ├── test_login.py              # Тесты входа (с главной, через Личный кабинет, из формы регистрации, из формы восстановления пароля)
│   ├── test_account_profile.py    # Тесты личного кабинета (переход в ЛК, переход в конструктор по клику на Конструктор и логотип, выход)
│   └── test_constructor.py        # Тесты перехода по разделам конструктора (Булки, Соусы, Начинки)
├── conftest.py                    # Фикстуры pytest (инициализация и закрытие драйвера, создание тестового пользователя)
├── locators.py                    # Локаторы всех элементов страниц с комментариями
├── urls.py                        # URL страниц сервиса
├── helpers.py                     # Вспомогательные функции генерации логина (email) и пароля
├── requirements.txt               # Зависимости проекта
├── .gitignore                     # Исключения для Git
└── README.md                      # Описание проекта
```


## Запуск тестов
Запуск всех тестов в Google Chrome:
```bash
pytest -v
```

Запуск конкретного файла тестов:
```bash
pytest -v tests/test_registration.py
pytest -v tests/test_login.py
pytest -v tests/test_account_profile.py
pytest -v tests/test_constructor.py
```
