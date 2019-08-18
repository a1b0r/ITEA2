from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_word():
    a = ""
    for i in range(100):
        a += str(i)
    return 'hello word'


@app.route('/new_route')
def routing():
    return 'new route'


if __name__ == '__main__':
    app.run(debug=True)

