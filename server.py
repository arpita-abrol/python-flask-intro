from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/about')
def about():
    return 'This site was developed by Arpita'

@app.route('/hello/<uname>')
def say_hello(uname):
    return 'Hello ' + uname

# Read from a CSV
@app.route('/users')
def return_users():
    with open('data/users.csv') as file:
        data = csv.reader(file, delimiter=',')
        first_line = True
        users = []
        for row in data:
            if not first_line:
                users.append({
                "fname": row[0],
                "lname": row[1],
                "city": row[2]
                })
            else:
                first_line = False
    return render_template("index.html", users=users)
