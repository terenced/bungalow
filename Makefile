default:
	@echo "View Makefile for usage"

.PHONY: app.build
app.build:
	@echo "==> Building app\n"
	docker-compose build app
	@echo "\n"

.PHONY: db.remove
db.remove:
	rm .data/database/db.sqlite3

.PHONY: db.clear
db.clear:
	docker-compose run --entrypoint "python manage.py empty_db" app

.PHONY: db.migrate
db.migrate: db.clear
	docker-compose run --entrypoint "python manage.py migrate" app

.PHONY: db.seed
db.seed: db.migrate
	docker-compose run --entrypoint "python manage.py import_data .data/imports/sample" app

.PHONY: app.run-with-data
app.run-with-data: db.seed
	docker-compose up app

.PHONY: app.run
app.run: db.migrate
	docker-compose up app
