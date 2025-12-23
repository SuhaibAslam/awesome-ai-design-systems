PYTHON ?= python3

.PHONY: validate table all

validate:
	$(PYTHON) scripts/validate-data.py

table:
	$(PYTHON) scripts/generate-table.py

all: validate table
