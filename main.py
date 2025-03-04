from flask import Flask, request
import os
app = Flask(__name__)


@app.route('/greet', methods=['GET'])
def greet():
    # Извлечение параметров из GET-запроса с установкой значений по умолчанию
    name = request.args.get('name', 'Recruto')  # Значение по умолчанию 'Recruto'
    message = request.args.get('message', 'Давай дружить!')  # Значение по умолчанию 'Давай дружить!'

    # Формирование ответа
    response = f"Hello {name}! {message}"
    return response


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Используйте PORT из окружения
    app.run(host='0.0.0.0', port=port)

