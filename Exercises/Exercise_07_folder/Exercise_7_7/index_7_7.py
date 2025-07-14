from flask import Flask, render_template

with open('./data/decompressedimage.txt', 'r') as f:
    reader = f.readlines()
    reader = [c.strip() for c in reader]

valList = [[] for i in range(9)]

colorDict = {
    '000': 'red',
    '001': 'white',
    '010': 'yellow',
    '011': 'blue',
    '100': 'black',
    '110': 'green'
}

for i, c in enumerate(reader):
    valList[i // 9] += [colorDict[c]]

app = Flask(__name__)

@app.route('/')
def generateImage():
    return render_template('index_7_7.html', valList = valList)

if __name__ == '__main__':
    app.run(debug=True)