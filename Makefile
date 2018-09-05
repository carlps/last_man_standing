COMPOSE_FILE=local.yml

help:		## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

makemigrations:	## make django migrations
	sh -c "docker-compose -f $(COMPOSE_FILE) run --rm django python manage.py makemigrations"

migrate:	## run django migrations
	sh -c "docker-compose -f $(COMPOSE_FILE) run --rm django python manage.py migrate"

coverage:	## run coverage check and open report in chrome
	sh -c "docker-compose -f $(COMPOSE_FILE) run --rm django coverage run -m pytest"
	sh -c "docker-compose -f $(COMPOSE_FILE) run --rm django coverage html"
	sh -c "google-chrome htmlcov/index.html"

runtests:	## run pytest
	sh -c "docker-compose -f $(COMPOSE_FILE) run --rm django pytest"

djshell:	## open a django shell in docker
	sh -c "docker-compose -f $(COMPOSE_FILE) run --rm django python manage.py shell"
