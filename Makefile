# Makefile for TactIQ PoC

setup:
	conda env create -f environment.yml

notebook:
	conda activate tactiq && jupyter notebook notebooks/player_tracking_demo.ipynb

update:
	conda env update -f environment.yml --prune

detect:
	python src/tracking/detect_players.py

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
