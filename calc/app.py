# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_both():
  args = request.args
  a = int(args.get('a'))
  b = int(args.get('b'))
  result = add(a, b)
  return f'<h1>{str(result)}</h1>'


@app.route('/sub')
def sub_both():
  args = request.args
  a = int(args.get('a'))
  b = int(args.get('b'))
  result = sub(a, b)
  return f'<h1>{str(result)}</h1>'


@app.route('/mult')
def mult_both():
  args = request.args
  a = int(args.get('a'))
  b = int(args.get('b'))
  result = mult(a, b)
  return f'<h1>{str(result)}</h1>'


@app.route('/div')
def div_both():
  args = request.args
  a = int(args.get('a'))
  b = int(args.get('b'))
  result = div(a, b)
  return f'<h1>{str(result)}</h1>'


operations = {
  'add': add,
  'sub': sub,
  'mult': mult,
  'div': div
}

#Single route to rule them all
@app.route('/math/<op>')
def do_math(op):
  args = request.args
  a = int(args.get('a'))
  b = int(args.get('b'))
  result = operations[op](a,b)
  return f'<h1>{str(result)}</h1>'