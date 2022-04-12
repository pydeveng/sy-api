
.PHONY: celery-beat celery-worker django migrate docker
.DEFAULT_GOAL := empty

empty: ; @echo $@

celery-beat:
	celery -A app beat -l DEBUG --scheduler django_celery_beat.schedulers:DatabaseScheduler

celery-worker:
	celery -A app worker -l DEBUG -B

django:
	python3 manage.py runserver 0.0.0.0:8000

migrate:
	python3 manage.py migrate

docker:
	docker-compose up --build