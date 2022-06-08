from flask import Flask, request, render_template
import os
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///info.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(30), nullable=False)
    author = db.Column(db.String(30), nullable=False)

    def __str__(self):
        return f'Firstname:{self.firstname}; Lastname:{self.lastname}; Age:{self.age}; Book title:{self.title}; Author: {self.author}'
 
 
@app.route('/', methods=['GET', 'POST'])
def books():
    if request.method=='POST':
        f = request.form['firstname']
        l = request.form['lastname']
        g = request.form['age']
        t = request.form['title']
        a = request.form['author']
        b1 = Books(firstname=f, lastname=l, age=int(g), title=t, author=a)
        db.session.add(b1)
        db.session.commit()      
        return render_template('base.html')

    return render_template('index.html')



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5005, debug=True)