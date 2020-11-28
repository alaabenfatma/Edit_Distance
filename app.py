from flask import Flask, render_template, request, json,jsonify
import recursive
app = Flask(__name__)

from flask import render_template
app = Flask(__name__, template_folder='templates', static_folder='static')
app.debug = True
@app.route('/')
def index(name=None):
    return render_template('index.html', name=name)

@app.route('/calculate_ed')
def calculate_ed():
    s1 = request.args.get('s1')
    s2 = request.args.get('s2')
    results = recursive.compute(s1,s2)
    return jsonify(result= results)
