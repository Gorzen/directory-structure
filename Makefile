init:
	pipenv install

test:
	# Black formatter
	-black src/
	@echo ""

	# Pylint code analysis
	-pylint src/

	# Mypy static type checker
	-mypy src/

.PHONY: init test
