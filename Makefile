SHELL := /bin/bash

.PHONY: activate install create-env check format build

install:
	python3 -m pip install -r requirements.txt

check:
	ruff check *.py

format:	
	ruff check --fix
	ruff format

build:
	python3 -m build