from flask import Flask, url_for, render_template, request, redirect, session, jsonify
import psycopg2
import os
app = Flask(__name__)

# Connect to SQL Server
conn = psycopg2.connect(database="For_Proj_Test",
                        host="localhost",
                        user="postgres",
                        password="admin",
                        port="5432")

@app.route('/', methods=['GET'])
def hello_world():
    # Query the database
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Persons')
    rows = cursor.fetchall()

    return jsonify(rows)

if __name__ == '__main__':
    app.run()

# cursor.execute("INSERT INTO Persons (personid, lastname, firstname, address, city) VALUES (8787, 'Yu', 'Champ', 'ABC', 'Taipei')")