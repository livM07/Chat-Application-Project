import sqlite3
from flask import Flask, request, jsonify
app = Flask(__name__)

connection = sqlite3.connect('database.db')
cur = connection.cursor()
table_schema = '''CREATE TABLE IF NOT EXISTS users (
email TEXT PRIMARY KEY,
password TEXT NOT NULL
);'''


cur.execute(table_schema)
connection.commit()
connection.close()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/create', methods = ['POST'])
def create():
    data = request.json
    # print(data["email"])
    # print(data["password"])
    # TO DO --> check if email already in DB, if true reject
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()
    rows = cur.execute("select * from users where email = ?", [data['email']]).fetchall() 
    
    for row in rows:
        print(row[0])
        print("email already exists, reject")
        connection.commit()
        connection.close()
        return jsonify({
            "message": "email already exists"
        })


    # TO DO --> check if email meets validation critera, if false reject
    rows = cur.execute("select * from users where email = ?", [data['email']]).fetchall()
    for row in rows:
        if row[0] == data['email']:
            print("email meets criteria")
        else:
            print("email does not meet criteria")
        connection.commit()
        connection.close()
        return jsonify({
            "message": "email meets criteria"
        })

    # TO DO --> check if password meet validation critera, if false reject
    rows = cur.execute("select * from users where password = ?", [data['password']]).fetchall()
    for row in rows:
        if row[0] == data['password']:
            print("password meets criteria")
        else:
            print("password does not meet criteria")
        connection.commit()
        connection.close()
        return jsonify({
            "message": "password meets criteria"
        })


    # store new account in DB, return success
    cur.execute("INSERT INTO users (email, password) VALUES (?, ?)",
            (data['email'], data["password"])
            )
    connection.commit()
    connection.close()

    return jsonify({
        "message": "success"
    })
