from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },
    {
    'id': 2,
    'title': 'Frontend Engineer',
    'location': 'Remote',
  },
    {
    'id': 3,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': 'Rs. $120,000'
  }
]


@app.route('/')
def hello():
  return render_template("home.html", jobs=JOBS, company_name="Wdesk")

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
