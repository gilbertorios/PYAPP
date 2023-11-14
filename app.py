from flask import Flask, render_template, request 
#import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#setup app to use sqlalchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample.db'
db = SQLAlchemy(app)


#setup a simple table for database
class Visitor(db.Model):
    username = db.Column(db.String(100), primary_key = True)
    numVisits = db.Column(db.Integer, default=1)

    def __repr__(self):
        return f"{self.username} - {self.numVisits}"
    

#create tables in database
with app.app_context():
    db.create_all()



#Make a homepage
@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/hello/<name>')
def hello(name):
    listOfNames = [name, "Gil", "Ruben", "Jennifer"]
    return render_template('name.html', name = name, nameList = listOfNames)
#Add the option to run this file directly

if __name__ == "__main__":
    app.run(debug=True)


@app.route('/form', methods=['GET', 'POST'])
def formDemo():
    if request.method == 'POST':
        if request.form['name']:
         name=request.form['name']
         #check if user is in the database
         visitor = Visitor.query.get(name)
         if visitor == None:
            #add visitor to the database
            visitor = Visitor(username=name)
            db.session.add(visitor)
        else:
            visitor.numVisits +=1

    db.session.commit()
    return render_template('form.html', name=name)

@app.route('/visitors')
def visitors():
        #query the database to find all visitors
        people = Visitor.query.all()
        return render_template('visitors.html')

