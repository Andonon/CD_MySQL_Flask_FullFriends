from flask import Flask, render_template, redirect, request
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'fullfriends')

@app.route('/')
def index():
    query = "select id,name,age,concat(Month(created_at),'/',Day(created_at)) as Date,year(created_at) as Year from friends"
    friends = mysql.query_db(query)
    print friends
    return render_template('fullfriends.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    print request.form
    print request.form['name']
    print request.form['age']
    query = "INSERT INTO friends (name, age, created_at, updated_at) VALUES (:name, :age, NOW(), NOW())"
    data = {
            'name': request.form['name'],
            'age': request.form['age']
        }
    mysql.query_db(query, data)
    # Run query, wi
    # add a friend to the database!
    return redirect('/')

app.run(debug=True)