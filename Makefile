ps:
	@docker ps

cps:
	@docker compose ps

logs:
	@echo "docker compose logs -f"
	@docker compose logs -f

down:
	@echo "docker compose down"
	@echo "Stopping all services..."
	@docker compose down

build-compose:
	@echo "docker compose build"
	@echo "Building Docker markovic..."
	@docker compose build

build:
	@echo "Building Docker markovic..."
	@docker compose up --build -d

bp:
	@docker build -t anower77/crossc1-backend:latest .
	@docker push anower77/crossc1-backend:latest

cache:
	@echo "docker compose build --no-cache"
	@echo "Clearing Docker build cache..."
	@docker compose build --no-cache

up:
	@echo "docker compose up -d"
	@echo "Starting all services..."
	@docker compose up -d

restart:
	@docker restart crossc1_web_server

bash:
	@docker exec -it crossc1_web_server bash

images:
	@docker images

pull:
	@docker pull anower77/crossc1-backend:latest

push:
	@docker push anower77/crossc1-backend:latest

mm:
	@docker exec -it crossc1_web_server python manage.py makemigrations

m:
	@docker exec -it crossc1_web_server python manage.py migrate

mig:
	@docker exec crossc1_web_server python manage.py makemigrations subscription
	@docker exec crossc1_web_server python manage.py migrate

sm:
	@docker exec -it crossc1_web_server python manage.py showmigrations

net:
	@netstat -ano | findstr :9000

all: down build up logs

# Install dependencies
setup:
	poetry install

# Run tests
test:
	poetry run pytest

# Run linting
lint:
	poetry run ruff check .

# Format code
format:
	poetry run ruff format .

# Clean cache/build files
clean:
	rm -rf .pytest_cache .ruff_cache dist build

# Git helpers
cm ?= Update code

git:
	git add .
	git status
	git commit -m "$(cm)"
	git log -1 --graph --oneline
	git push origin main

	
