from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_word():
    return f'''
    <html>
        <header>
            <title>title</title>
        </header>
        <body>
            <h1>h1</h1>
            <h2>h2</h2>
        </body>
    </html>
    '''


@app.route('/new_route')
def routing():
    return 'new route'


if __name__ == '__main__':
    app.run(debug=True)

