from flask import Flask, render_template

app = Flask(__name__)

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

