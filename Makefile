install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	pylint stats_2.py

test:
	pytest test_stats_2.py

all: install lint test