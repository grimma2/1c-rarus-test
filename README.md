# 1c-rarus-test


# FastAPI ToDo API

## Описание

Это API для управления задачами ToDo, реализованное с использованием FastAPI и SQLAlchemy. API позволяет создавать, обновлять, удалять и получать задачи.

## Установка и запуск

### Запуск с помощью Docker Compose

1. Убедитесь, что у вас установлен Docker и Docker Compose.
2. Создайте файл `.env` и скопируйте в него содержание файла `.env.example` (если есть).
3. Запустите проект с помощью Docker Compose:

    ```bash
    docker-compose up -d
    ```

### Локальный запуск

1. Клонируйте репозиторий:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Создайте и активируйте виртуальное окружение:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Запустите приложение:
    ```bash
    uvicorn main:app --reload
    ```

    Замените `main:app` на путь к вашему приложению, если он отличается.

## Эндпоинты

### Получение задачи по ID

- **URL**: `/api/tasks/{task_id}`
- **Метод**: `GET`
- **Параметры**:
  - `task_id` (path) - ID задачи
- **Ответ**:
  - **Код ответа**: `200 OK`
  - **Тело ответа**: `ToDoTaskOutput`

### Создание новой задачи

- **URL**: `/api/tasks/create`
- **Метод**: `POST`
- **Тело запроса**:
  - **Формат**: JSON
  - **Схема**: `ToDoTaskInput`
- **Ответ**:
  - **Код ответа**: `201 Created`
  - **Тело ответа**: `ToDoTaskOutput`

### Обновление задачи по ID

- **URL**: `/api/tasks/{task_id}`
- **Метод**: `PUT`
- **Параметры**:
  - `task_id` (path) - ID задачи
- **Тело запроса**:
  - **Формат**: JSON
  - **Схема**: `ToDoTaskUpdate`
- **Ответ**:
  - **Код ответа**: `200 OK`
  - **Тело ответа**: `ToDoTaskOutput`

### Удаление задачи по ID

- **URL**: `/api/tasks/{task_id}`
- **Метод**: `DELETE`
- **Параметры**:
  - `task_id` (path) - ID задачи
- **Ответ**:
  - **Код ответа**: `200 OK`
  - **Тело ответа**: `{"message": "Task deleted successfully"}`

### Получение списка всех задач

- **URL**: `/api/tasks/`
- **Метод**: `GET`
- **Параметры** (опционально):
  - `priority` (query) - Фильтр по приоритету задачи (min_length=3, max_length=6)
- **Ответ**:
  - **Код ответа**: `200 OK`
  - **Тело ответа**: Список объектов `ToDoTaskOutput`
