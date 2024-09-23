install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	ruff check *.py

test:
	pytest *.py

all: install lint test