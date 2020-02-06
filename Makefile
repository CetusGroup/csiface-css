.PHONY: init tests requirements vendor

PROJECT_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
VIRTUAL_ENV = $(PROJECT_DIR).venv
PYTHON = python3.6
#include .env


dependencies:
	$(PYTHON) -m pip install virtualenvwrapper


venv: dependencies
	#$(PYTHON) -m virtualenv $(VIRTUAL_ENV)
	virtualenv -p `which $(PYTHON)` $(VIRTUAL_ENV)


requirements:
	$(PYTHON) -m pip install -r $(PROJECT_DIR)requirements.txt


build:
	docker-compose build


rebuild: init
	docker-compose build --no-cache


up:
	docker-compose up -d


logs:
	docker-compose logs -f


down:
	docker-compose down


clean:
	docker-compose down --rmi all


pycache_clean:
	find . -regex '.*\(__pycache__\|\.py[co]\)' -delete


tox-clean:
	rm -r .tox


tests: up
	tox -e tests


coala: up
	tox -e coala


