# Cook_book_service

## Установка и запуск

1. Клонирование репозитория на локальную машину:

```bash
git clone https://github.com/AlexMiller93/Cook_book_service.git
```

2.Создание виртуального окружения:

```bash
python -m venv venv
```

3.Активация виртуального окружения:

    - На Windows:

    ```bash
    venv\Scripts\activate
    ```

    - На macOS и Linux:

    ```bash
    source venv/bin/activate
    ```

4.Установка зависимостей:

```bash
pip install -r requirements.txt
```

5.Запуск миграции:

```bash
python manage.py migrate
```

6.Создание суперпользователя (по желанию):

```bash
python manage.py createsuperuser
```

7.Запуск сервера разработки:

```bash
python manage.py runserver
```

## Примеры запросов

```
GET /recipe/add_product_to_recipe/?recipe_id=1&product_id=2&weight=50
GET /recipe/cook_recipe/?recipe_id=1
GET /recipe/show_recipes_without_product/?product_id=3

```
