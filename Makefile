test: 
	pytest

format:
	isort .
	black . 

types:
	mypy gif.py
	pyright gif.py

loc: 
	find . -name 'gif.py' | xargs wc -l | sort -nr
	find tests -name '*.py' | xargs wc -l | sort -nr