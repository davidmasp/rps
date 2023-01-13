

# build env
.install.done: .env
	@echo "Building..."
	python -m venv ./venv
	. ./venv/bin/activate
	pip3 install -r requirements.txt
	touch $@

all: .install.done
	@echo "Running..."
	@python3 bot.py

