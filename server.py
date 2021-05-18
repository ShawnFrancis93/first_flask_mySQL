from flask import Flask, render_template, redirect, request
from mysqlconn import connectToMySQL
app = Flask(__name__)





@app.route("/")
def index():
    mysql = connectToMySQL("'first_flask'")	        # call the function, passing in the name of our db
    friends = mysql.query_db('SELECT * FROM friends;')  # call the query_db function, pass in the query as a string
    print(friends)
    return render_template("index.html", all_friends = friends)


@app.route("/createfriend", methods =["POST"])
def add_friend_to_db(): 
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at) VALUES (%(fn)s, %(ln)s, %(occ)s, NOW());"
    data = {
        'fn': request.form['fname'],
        'ln': request.form['lname'],
        'occ': request.form['occ']
    }
    mysql = connectToMySQL("'first_flask'")
    mysql.query_db(query, data)
    return render_template("add.html"), redirect("/")


















if __name__ == "__main__":
    app.run(debug=True)