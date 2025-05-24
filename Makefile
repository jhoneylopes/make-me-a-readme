.PHONY: help install clean

help:
	@echo "Available targets:"
	@echo "  install   Create virtualenv and install requirements"
	@echo "  clean     Remove virtualenv (reset environment)"

install:
	@if [ -d "venv" ]; then \
		echo "Virtualenv already exists. Skipping creation."; \
	else \
		python3 -m venv venv; \
		echo "Virtualenv created."; \
	fi
	@echo "Activating virtualenv and installing requirements..."
	. ./venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
	@echo "Setup complete! To activate: source venv/bin/activate"

clean:
	rm -rf venv
	@echo "Virtualenv removed."

run:
	source ./venv/bin/activate && python -m app.readme_generator