# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/add')
def f_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)
    return f'{result}'


@app.route('/sub')
def f_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)
    return f'{result}'


@app.route('/mult')
def f_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)
    return f'{result}'


@app.route('/div')
def f_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)
    return f'{result}'


operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}


@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)
