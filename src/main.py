from flask import Flask, render_template, request
from tinydb import TinyDB

app = Flask(__name__)

db = TinyDB('db.json')


@app.route("/")
def add_user():
    # return render_template("add_user.html", title=" Add User", form= form)

    return render_template('base.html')


@app.route('/user', methods=['POST'])
def signUp():
    # read the posted values from the UI
    subscribe = request.form['action'] == 'Register'
    first_name = request.form['firstName']
    print(first_name)
    last_name = request.form['lastName']
    print(last_name)
    _email = request.form['inputEmail']
    print(_email)
    _tele = request.form['telenummer']
    print(_tele)
    db.insert({'firstName': first_name, 'lastName': last_name,
               "inputEmail": _email})
    return render_template('base.html')


if __name__ == "__main__":
    app.run(debug=True)
