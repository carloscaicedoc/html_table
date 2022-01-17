from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {'first_name' : 'Jeff', 'last_name' : 'Lebowski'},
        {'first_name' : 'Ethan', 'last_name' : 'Edwards'},
        {'first_name' : 'Dorothy', 'last_name' : 'Gale'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Julianne', 'last_name' : 'Monroe'},
        {'first_name' : 'Elizabeth', 'last_name' : 'Kent'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("index.html",users=users)


if __name__=="__main__":
    app.run(debug=True)



