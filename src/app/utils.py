import string
import random


def get_random_string(length: int = 20) -> str:
    """
    Генерирует случайную строку размером length
    """

    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for i in range(length))