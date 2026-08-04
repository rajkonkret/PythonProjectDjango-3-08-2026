Na gałęzi master nasz projekt<br>
Na gałęzi main projekt rozbudowany o Django Rest Framework i kilka drobnych poprawek<br>
Możliwość przetestowania czy DRF działa:<br>
http://127.0.0.1:8000/api/courses/

pip install whitenoise<br>
python manage.py collectstatic<br>
pip install djangorestframework<br>
python manage.py check<br>

produkcja:<br>
pip install gunicorn<br>
gunicorn config.wsgi:application<br>
<br>
-----# CourseHub - projekt szkoleniowy Django 6

Projekt towarzyszący szkoleniu **Aplikacje webowe z Django - praktyczne wzorce budowy aplikacji internetowych**.

## Wersje użyte w materiale

- Python 3.12+ (Django 6.0 obsługuje Python 3.12-3.14)
- Django 6.0.7
- Django REST Framework 3.17.1
- SQLite w ćwiczeniach

## Uruchomienie

```bash
python -m venv .venv
source .venv/bin/activate       # macOS/Linux
# .venv\Scripts\activate      # Windows PowerShell/cmd
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py createsuperuser
python manage.py runserver
```

Adresy:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/admin/
- http://127.0.0.1:8000/api/courses/

## Kontrola projektu

```bash
python manage.py check
python manage.py makemigrations --check
python manage.py test
```

## Ważne

`runserver` jest narzędziem developerskim. W produkcji konfiguruj właściwy serwer/platformę, `DEBUG=False`, `ALLOWED_HOSTS`, sekrety i static files.