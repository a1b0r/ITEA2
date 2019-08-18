from flask import Flask
from flask import render_template

app = Flask(__name__)

name = 'Alex'

@app.route('/')
def hello_word():
    return f'''
    <html>
        <header>
            <title>title</title>
        </header>
        <body>
            <h1>h1</h1>
            <h2>{name}</h2>
        </body>
    </html>
    '''


@app.route('/new_route')
def routing():
    students = {'Alex': '85', 'Andrew': '90'}
    title = 'students list with marks'

    Flask.render_template('índex.html', students=students,title=title)

    return 'new route'


if __name__ == '__main__':
    app.run(debug=True)

