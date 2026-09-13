from flask import Flask, jsonify

app = Flask(__name__)
@app.route("/")
def hpme() :
    return "главная страница приложения"


@app.route('/info')
def info():
    fio = 'иванов иван иванович'
    group = 'ддр40'
    discipline = 'информатика'

    return f"Студент: {fio}<br>Группа: {group}<br> Дисциплина: {discipline}"

@app.route('/hello/<name>')
def hello(name):
    return f"Здравствуйте, {name}!"

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    result = a * b
    return jsonify({
    "number_1": a, 
    "number_2": b, 
    "operation": "multiplication", 
    "result": result
    })

@app.route('/check/<int:number>')
def check_even_odd(number):
    if number % 2 == 0:
        status = "even"
        description = "четное"
    else:
        status = "odd"
        description = "нечетное"

    return jsonify({
    "number": number, 
    "status": status, 
    "description": description
    })

    
if __name__=="__main__" : 
    app.run(host="0.0.0.0", port=5001)
