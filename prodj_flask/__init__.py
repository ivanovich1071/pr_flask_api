from flask import Flask

app = Flask(__name__)

# Импортируем модули, которые могут зарегистрировать маршруты
from . import app  # импортируем из текущего пакета

