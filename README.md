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
gunicorn config.wsgi:application
