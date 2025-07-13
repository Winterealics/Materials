from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def displaydata():

    with open('data/people.txt', 'r') as f:
        reader = list(csv.reader(f))

    for c in reader:
        screen_name = ''.join([i for i in c[0] if i != ' '])
        screen_name += c[1][5:7] + c[1][-2:]
        c[1] = screen_name

    return render_template('index_7_4.html', data=reader)

if __name__ == "__main__":
    app.run(debug=True)
