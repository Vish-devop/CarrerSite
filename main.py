
from flask import Flask, render_template, jsonify

app=Flask(__name__)


JOBS=[
    {
        'id':1,
        'title':'Data Analyst',
        'location': 'Bengaluru, India',
         
    },
    {
        'id':2,
        'title':' Backend Engineer',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 20lpa'
    },
    {
        'id':3,
        'title':'Full-stack Engineer',
        'location': 'Noida, India',
        'salary': 'Rs. 40lpa'
    },
]

@app.route('/')
def jobs():
    return render_template('index.html',jobs=JOBS, company_name="ASC" )

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)


app.run(debug=True)