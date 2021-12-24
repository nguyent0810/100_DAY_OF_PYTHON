from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='text-align:center'>Hello, World!<h1> \
    <p>This is a paragraph</p> \
    <img src='https://interactive-examples.mdn.mozilla.net/media/cc0-images/grapefruit-slice-332-332.jpg'<b></img>" 
def make_bold(function):
    def wrapper():
    
        return f"<b><i>{function()}</i></b>"
    return wrapper
@app.route("/bye")
@make_bold
def Bye():
    return "Bye"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}. You're {number} year olds"
if __name__ == "__main__":
    app.run(debug=True)