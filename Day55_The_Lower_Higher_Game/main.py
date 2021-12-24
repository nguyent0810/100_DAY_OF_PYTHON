from flask import Flask
import random

random_number = random.randint(0, 9)
app = Flask(__name__)

@app.route("/")
def guess_the_number():
    return "<div style='text-align:center'> <h1>Guess a number between 0 and 9<h1> \
        <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></img></div>" 
def make_bold(function):
    def wrapper():
    
        return f"<b><i>{function()}</i></b>"
    return wrapper

@app.route("/<int:number>")
def greet(number):
    if number == random_number:
        return f"<div style='text-align:center'><h1 style='color:green'>You got it right</h1>\
            <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'></img></div>"
    elif number < random_number: 
        return f"<div style='text-align:center'><h1 style='color:red'>It's too low</h1>\
            <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'></img></div>"
    else:
        return f"<div style='text-align:center'><h1 style='color:purple'>It's too high</h1>\
            <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'></img></div>"
if __name__ == "__main__":
    app.run(debug=True)