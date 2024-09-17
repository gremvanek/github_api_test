import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Переменные окружения
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
REPO_NAME = os.getenv("REPO_NAME")

# Базовый URL для GitHub API
BASE_URL = "https://api.github.com"

# Заголовки для авторизации
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def create_repo():
    """Создание нового публичного репозитория."""
    url = f"{BASE_URL}/user/repos"
    data = {
        "name": REPO_NAME,
        "private": False  # Открытый репозиторий
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"Репозиторий {REPO_NAME} успешно создан!")
    else:
        print(f"Ошибка при создании репозитория: {response.json()}")
    return response

def check_repo():
    """Проверка наличия репозитория в списке."""
    url = f"{BASE_URL}/users/{GITHUB_USERNAME}/repos"
    response = requests.get(url, headers=headers)
    repos = [repo['name'] for repo in response.json()]
    if REPO_NAME in repos:
        print(f"Репозиторий {REPO_NAME} найден!")
        return True
    else:
        print(f"Репозиторий {REPO_NAME} не найден!")
        return False

def delete_repo():
    """Удаление репозитория."""
    url = f"{BASE_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}"
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Репозиторий {REPO_NAME} успешно удален!")
    else:
        print(f"Ошибка при удалении репозитория: {response.status_code} {response.json()}")

if __name__ == "__main__":
    # Шаг 1: Создание репозитория
    create_repo()

    # Шаг 2: Проверка наличия репозитория
    if check_repo():
        # Шаг 3: Удаление репозитория
        delete_repo()
