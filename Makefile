default: test

init:
	pipenv install
	pipenv shell

run:
	python src/directories.py

test:
	@echo "========================================   Black    ========================================"
	# Black formatter
	-black src/
	@echo ""
	@echo "========================================   Flake8   ========================================"
	# flake8 - style guide enforcement
	-flake8 src/
	@echo ""
	@echo "======================================== pydocstyle ========================================"
	# pydocstyle - docstring style checker
	-pydocstyle src/
	@echo ""
	@echo "========================================   Pylint   ========================================"
	# Pylint - code analysis
	-pylint src/
	@echo "========================================    Mypy    ========================================"
	# Mypy - static type checker
	-mypy src/
	@echo ""
	@echo "========================================   Bandit   ========================================"
	# Bandit - find common security issues
	-bandit --quiet --recursive src/

.PHONY: init run test
