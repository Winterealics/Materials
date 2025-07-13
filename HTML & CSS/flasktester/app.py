from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('welcome.html')

@app.route("/name/<user>")
def welcome(user):
    return render_template("welcome.html", name = user)

@app.route('/form', methods=['GET','POST'])
def form():
    return render_template('form.html', name=request.form.get('input'))

@app.route('/list')
def list():
    return render_template('list.html', ulist=['a', 'b', 'c', 'd'], olist=[1, 2, 3, 4])

@app.route('/table')
def table():
    return render_template('table.html', header=['A', 'B', 'C', 'D'], value=[1, 2, 3, 4])

if __name__ == "__main__":
    app.run(debug=True)