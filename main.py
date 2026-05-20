import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

def print_author():
    # Считываем значение переменной AUTHOR
    author = os.getenv("AUTHOR")
    
    print(f"Автор проекта: {author}")

# Вызов функции для проверки работы
if __name__ == "__main__":
    print_author()
