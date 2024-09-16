build:
	docker-compose -f local.yml up --build -d --remove-orphans

up:
	docker-compose -f local.yml up -d 

down:
	docker-compose -f local.yml down

show-logs:
	docker-compose -f local.yml logs


makemigrations:
	docker-compose -f local.yml run --rm api python manage.py makemigrations

migrate:
	docker-compose -f local.yml run --rm api python manage.py migrate

collectstatic:
	docker-compose -f local.yml run --rm api python manage.py collectstatic --no-input --clear

superuser:
	docker-compose -f local.yml run --rm api python manage.py createsuperuser

down-v:
	docker-compose -f local.yml down -v

volume:
	docker volume inspect src_postgres_data
