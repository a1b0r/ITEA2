from flask import Flask, request
from flask import render_template

app = Flask(__name__)




students = {"Alex": "85", "Andrew": "96",
            "Julia": "90", "John": "70"}

@app.route("/<int:id>")
def hello_world(id):
    print(id)
    print(request.args)
    return render_template("form_example.html")

@app.route("/<string:id>")
def id(id):
    print(id)
    return "Hi"



@app.route("/index", methods=["GET", "POST"])
def index_page():

    return "Form approved"



@app.route("/new_route")
def students_list():
    title = "Students list with marks"
    return render_template("index.html",
                           students=students,
                           title=title,
                           a = A())


if __name__ == "__main__":
    app.run(debug=True)