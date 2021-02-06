# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div 

app = Flask(__name__)

@app.route('/add')
def addition():
    "Add integers a and b"

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = add(a,b)
    return str(answer)

@app.route('/sub')
def subtraction():
    "Subtract integers a and b"

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = sub(a,b)
    return str(answer)

@app.route('/mult')
def multiplication():
    "Multiple integers a and b"
    
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = mult(a,b)
    return str(answer)

@app.route('/div')
def division():
    "Divide integers a and b"

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = div(a,b)
    return str(answer)


##Further Study

operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<operation>')
def operate(operation):
    "Complete the operation of the chosen path"

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = operations[operation](a,b)
    return str(answer)
