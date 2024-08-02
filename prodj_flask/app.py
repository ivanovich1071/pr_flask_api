from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # URL API
    url = "https://api.quotable.io/random"

    try:
        # Выполняем GET-запрос
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Проверяем, произошла ли ошибка HTTP

        # Парсим JSON-ответ
        data = response.json()
        quote = {
            "content": data.get("content", "Не удалось получить цитату."),
            "author": data.get("author", "Неизвестный автор")
        }
    except (requests.exceptions.RequestException, ValueError) as e:
        # Обработка ошибок запроса
        print(f"Ошибка подключения или получения данных: {e}")
        quote = {
            "content": "Не удалось получить цитату. Попробуйте позже.",
            "author": ""
        }

    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)


