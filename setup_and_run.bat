@echo off
python -m venv dshelper_env
call dshelper_env\Scripts\activate
pip install -r requirements.txt
python main.py
