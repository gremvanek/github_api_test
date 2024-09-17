# GitHub API Test

Этот проект представляет собой автоматический тест для работы с GitHub API на Python. Он выполняет создание, проверку и удаление репозитория на GitHub.

## Установка и настройка

1. Склонируйте репозиторий:
    ```bash
    git clone https://github.com/gremvanek/github_api_test.git
    cd github_api_test
    ```

2. Создайте виртуальное окружение и активируйте его:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # для Linux/Mac
    .\venv\Scripts\activate    # для Windows
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Создайте файл `.env` в корне проекта с вашим GitHub токеном, именем пользователя и названием репозитория:
    ```env
    GITHUB_TOKEN=your_github_token_here
    GITHUB_USERNAME=your_github_username_here
    REPO_NAME=test-repo
    ```

## Запуск теста

1. Запустите тест:
    ```bash
    python test_api.py
    ```

Тест создаст новый публичный репозиторий, проверит его наличие и удалит его после завершения проверки.
