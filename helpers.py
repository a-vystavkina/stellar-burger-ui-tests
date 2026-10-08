import random
import string


def generate_login():
    """
    Генерирует уникальный email по формату Практикума:
    имя_фамилия_номер когорты_любые 3 цифры@домен
    Например: alexandra_vystavkina_58_123@yandex.ru
    """
    random_digits = "".join(random.choices(string.digits, k=3))
    return f"alexandra_vystavkina_58_{random_digits}@yandex.ru"


def generate_password(length=8):
    """
    Генерирует валидный пароль (по умолчанию длиной 8 символов).
    """
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))
