init:
	pipenv install
	pipenv shell

run:
	python src/directories.py

test:
	# Black formatter
	-black src/
	@echo ""
	# flake8 style guide enforcement
	-flake8 src/
	@echo ""
	# Pylint code analysis
	-pylint src/
	# Mypy static type checker
	-mypy src/

.PHONY: init run test
