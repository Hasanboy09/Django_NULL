mig:
	python manage.py makemigrations
	python manage.py migrate

user:
	python3 manage.py createsuperuser

app:
	python3 manage.py startapp apps