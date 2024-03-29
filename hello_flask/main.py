from flask import Flask
# import random

app = Flask(__name__)
# print(random.__name__)
# print(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align : center" > Hello World! </h1>'\
            '<p> this is a test page </p>'\
            '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWF1OWxicXk0cnpueXhhZGMxd3RiMHk5ZzY1dWl4c2I2bTE0NzFjdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1BXa2alBjrCXC/giphy.gif" width = 200>'

@app.route('/bye')
def bye():
    return 'Bye!'

@app.route('/username/<name>/<int:number>')
def greeting(name, number):
    return f"Hello there  {name}, you are {number} year old !"

if __name__ == '__main__':
    app.run(debug=True)
