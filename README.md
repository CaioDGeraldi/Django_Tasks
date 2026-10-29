# Django Tasks

An educational task-management application built with Django and MySQL. This is an early learning project, not a production service.

## Setup (Windows CMD)

1. Install Python, MySQL Server and the dependencies required for `mysqlclient`.
2. Create a local MySQL database named `tasksdb` and a dedicated local database account with access to it.
3. In CMD, run:

```bat
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
set DJANGO_SECRET_KEY=replace-with-a-unique-random-key
set MYSQL_DATABASE=tasksdb
set MYSQL_USER=your-local-mysql-user
set MYSQL_PASSWORD=your-local-mysql-password
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Generate a Django secret locally using:

```bat
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Use the generated value in your local environment. The example commands do not provide working shared credentials. All accounts should be created locally; the application does not ship with a default administrator.

## Security

- Never commit credentials, `.env` files or database files.
- A previously committed SQLite file was removed from the current branch. Older commits may still contain it.
- Previously documented demonstration credentials and any exposed database credentials must be revoked or changed wherever they are still used.
- This project requires explicit `DJANGO_SECRET_KEY`; it does not embed a shared secret in source code.
