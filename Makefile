export PYTHONPATH := src

.PHONY: test replay validate
test:
	python -m unittest discover -s tests -v

replay:
	python -m andy replay --prompt "Identify yourself."

validate:
	python scripts/validate_tree.py
