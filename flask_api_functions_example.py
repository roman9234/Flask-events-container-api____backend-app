from flask import Flask, request

app = Flask(__name__)


# Flask умеет складывать всю информацию оо запросе в контекст
# контект - request, в нём хранится информация
@app.route('/login/<username>', methods=['GET', 'POST'])
def login(username):
    # Проверка на метод запроса
    if request.method == 'POST':
        return f"Post method for user {username}"
    else:
        return f"GET method for user {username}"

# просто API
@app.route("/api/")
def hello_world():

    # Получение данных запроса
    data = request.get_data()

    return f"hello great API!!!!!\n {data}"


# динамическая переменная.
# Flask умеет различать динамические переменные
@app.route('/api/<username>')
def api_v1_user_by_name(username):
    # show the user profile for that user
    return f'Hello User {username}'


# динамическая переменная со слэшом
@app.route('/api/<username>/')
def api_v2_user_by_name(username):
    # show the user profile for that user
    return f'Hello User {username} with /'
