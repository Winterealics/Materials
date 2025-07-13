from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def navigation():
    return render_template('index_7_5.html')

@app.route('/round<n>')
def roundscores(n):
    with open('./data/Ex_7_4_competitor.csv', 'r') as f:
            reader1 = list(csv.reader(f))[1:]

    with open('./data/Ex_7_4_scores.csv', 'r') as f:
        reader2 = list(csv.reader(f))[1:]

    idDict = {}
    for c in reader1:
        idDict[c[0]] = c[1]

    scoreList = []
    for c in reader2:
        if c[1] == n:
            scoreList += [[idDict[c[0]], c[2]]]

    scoreList.sort(key = lambda x: int(x[1]), reverse = True)

    return render_template('roundscores.html', scoreList = scoreList, n=n)

@app.route('/meanscores')
def meanscore():

    with open('./data/Ex_7_4_competitor.csv', 'r') as f:
            reader1 = list(csv.reader(f))[1:]

    with open('./data/Ex_7_4_scores.csv', 'r') as f:
        reader2 = list(csv.reader(f))[1:]

    meanList = []
    for c in reader1:
        scoreList = [x for x in reader2 if x[0] == c[0]]
        mean = round(sum([int(m[2]) for m in scoreList]) / len(scoreList), 2)
        meanList += [[c[1], str(mean)]]

    meanList.sort(key = lambda x:x[0])

    return render_template('meanscores.html', meanList = meanList)

@app.route('/qualifiers')
def qualifiers():

    with open('./data/Ex_7_4_competitor.csv', 'r') as f:
            reader1 = list(csv.reader(f))[1:]

    with open('./data/Ex_7_4_scores.csv', 'r') as f:
        reader2 = list(csv.reader(f))[1:]
     
    qualifiedList = []
    for c in reader1:
        scoreList = [x for x in reader2 if x[0] == c[0]]
        total = sum([int(m[2]) for m in scoreList])
        
        if total >= 250:
            qualifiedList += [[c[1], total, 'Qualified']]
        else:
            qualifiedList += [[c[1], total, 'Not qualified']]

    qualifiedList.sort(key = lambda x:x[0])

    return render_template('qualifers.html', qualifiedList = qualifiedList)

@app.route('/query', methods=['GET', 'POST'])
def query():
    
    def generateInfo(id):
        with open('./data/Ex_7_4_competitor.csv', 'r') as f:
            reader1 = list(csv.reader(f))[1:]

        with open('./data/Ex_7_4_scores.csv', 'r') as f:
            reader2 = list(csv.reader(f))[1:]

        queryList = []
        queryList += [c[1] for c in reader1 if c[0] == id]
        scoreList = [int(c[2]) for c in reader2 if c[0] == id]
        queryList += [scoreList]
        queryList += [sum(scoreList)]

        if sum(scoreList) >= 250:
            queryList += ['Qualified']
        else:
            queryList += ['Not qualified']

        return queryList
    
    id=request.form.get('id')
    
    return render_template('query.html', id=id, queryList=generateInfo(id))

if __name__ == '__main__':
    app.run(debug=True)