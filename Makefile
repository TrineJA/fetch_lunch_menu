PY_ENV_EXEC ?= PYTHONPATH=src poetry run
PIPENV ?= PYTHONPATH=src pipenv run

# Cleaning
.PHONY: poetry-clean
poetry-clean:
	rm -rf $(poetry env info --path)

# Shorthands for editors
.PHONY: jupyter-notebook
jupyter-notebook: export PYTHONPATH=src/
jupyter-notebook:
	$(PY_ENV_EXEC) jupyter notebook

.PHONY: code
code:
	PYTHONPATH=src code .

print_menu:
	$(PY_ENV_EXEC) python src/get_menu.py

streamlit-local:
	$(PY_ENV_EXEC) streamlit run app/VTx_lunch_menu_wizard.py

heroku-local:
	$(PIPENV) heroku local web