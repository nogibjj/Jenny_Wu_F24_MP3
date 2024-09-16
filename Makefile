install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	pylint main.py

test:
	pytest test_main.py

all: install lint test