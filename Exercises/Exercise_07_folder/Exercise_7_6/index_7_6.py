from flask import Flask, render_template, request
import csv

with open('./data/BOOK.txt', 'r') as f:
    bookReader = list(csv.reader(f)) #book id, book name, genre

with open('./data/LOAN.txt', 'r') as f:
    loanReader = list(csv.reader(f)) #number, member id, book id, date, returned

with open('./data/MEMBER.txt', 'r') as f:
    memberReader = list(csv.reader(f)) #member id, member last name, member first name

def bookCheck(name):
    if name:
        name = name.split(' ')
        memberID = [c[0] for c in memberReader if c[1] == name[1] and c[2] == name[0]][0]
        recordList = []

        for c in loanReader:
            if c[1] == memberID:
                bookID = c[2]
                bookName = [x[1] for x in bookReader if x[0] == bookID][0]

                if c[4] == 'FALSE':
                    recordList += [[bookName, 'Not returned']]

                elif c[4] == 'TRUE':
                    recordList += [[bookName, 'Returned']]

        return recordList

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def searchRecords():
    name = request.form.get('name')

    return render_template('index_7_6.html', name=name, recordList=bookCheck(name))

if __name__ == '__main__':
    app.run(debug=True)