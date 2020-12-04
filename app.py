from flask import render_template
from flask import Flask, render_template, request, json, jsonify
import greedy
import recursive
import dynamic
import branch_and_bound
import k_stripes_dynamic_programming
app = Flask(__name__)

app = Flask(__name__, template_folder='templates', static_folder='static')
app.debug = True


@app.route('/')
def index(name=None):
    return render_template('index.html', name=name)


@app.route('/calculate_ed')
def calculate_ed():
    s1 = request.args.get('s1')
    s2 = request.args.get('s2')
    algo = request.args.get('algo')
    results = None
    # the ed algo must return (distance,alignment (string))
    if(algo == algo == 'Recursive algorithm'):
        results = recursive.compute(s1, s2)
    elif(algo == 'Dynamic programming'):
        results = dynamic.compute(s1, s2)
    elif(algo == 'K-stripe approach'):
        results = k_stripes_dynamic_programming.compute(s1, s2)
    elif('Greedy approach' in algo):
        results = greedy.compute(s1, s2)
    elif('Branch and bound algorithm' in algo):
        results = branch_and_bound.compute(s1,s2)
    elif('Divide and conquer algorithm' in algo):
        pass
    print(results)
    return jsonify(result=results)
