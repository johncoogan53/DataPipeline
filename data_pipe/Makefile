
#variables
PYSRC := python

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -v python/tests
	cargo test --quiet

format:	
	cargo fmt --quiet
	black python 
	

lint:
	cargo clippy --quiet
	ruff check $(PYSRC)

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	#deploy goes here

venv:
	python3 -m venv venv
		
all: install lint test format deploy
