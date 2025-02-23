SHELL := /bin/bash

.PHONY: activate install create-env check format build test kernel

install:
	python3 -m pip install -r requirements.txt

check:
	ruff check *.py

format:	
	ruff check --fix
	ruff format

build:
	pip install -q build
	python3 -m build

test:
	python3 -m unittest

kernel:
	python -m ipykernel install --user --name tic --display-name "TicTacToe"