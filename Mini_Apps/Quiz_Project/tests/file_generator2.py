
import os
from createfile import createfile
from tkinter import filedialog
from random import shuffle


start = """<!DOCTYPE html>
<html lang="en" prefix="og: http://ogp.me/ns#">
  <head>
    <meta charset="UTF-8">
    <title>Review Questions: Chapter 2 - Signals, Signs, and Pavement Markings | Pennsylvania Driver Tests</title>
    <meta name="title" content="Review Questions: Chapter 2 - Signals, Signs, and Pavement Markings | Pennsylvania Driver Tests">
    <meta name="twitter:title" content="Review Questions: Chapter 2 - Signals, Signs, and Pavement Markings | Pennsylvania Driver Tests">
    <meta property="og:title" content="Review Questions: Chapter 2 - Signals, Signs, and Pavement Markings | Pennsylvania Driver Tests">
    <meta name="description" content="This test reviews what you have learned in Chapter 2 (p.7-22) of the Pennsylvania Driver's Manual. Answer the questions as best as you can.">
    <meta property="og:description" content="This test reviews what you have learned in Chapter 2 (p.7-22) of the Pennsylvania Driver's Manual. Answer the questions as best as you can.">
    <link rel="shortcut icon" type="image/x-icon" href="../../../resources/images/padt.ico">

    <meta name="keywords" content="PennDOT, Driver Manual, Tests, Practice, Exercises" lang="en">
    <meta name="language" content="en">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <meta property="og:site_name" content="sethclydesdale.github.io">
    <meta property="og:url" content="https://sethclydesdale.github.io/pa-driver-tests/tests/chapter-2/review/">
    <meta property="og:type" content="website">
    <meta property="og:image" content="https://sethclydesdale.github.io/pa-driver-tests/resources/images/padt-thumb.png">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:creator" content="@SethC1995">

    <link rel="stylesheet" href="../../../resources/stylesheet.min.css">
    <script src="../../../resources/ga.js" async></script>
  </head>

  <body>
    
    <header>
      <h1><a href="../../../" id="home-link">Pennsylvania Driver Tests</a></h1>
      <a id="fork-me" href="https://github.com/SethClydesdale/pa-driver-tests">Fork Me</a>
    </header>
    
    <div id="content">
      <div id="exercise" class="content-block">
        <h2 id="exercise-title" class="center">Review Questions: Chapter 2 - Signals, Signs, and Pavement Markings</h2>
        <div id="quiz-result"></div>
        <div id="quiz-zone" class="clear"></div>
        <div id="quiz-timer" class="center"></div>
      </div>
    </div>
    
    <footer class="clear">
      <ul class="footer-left">
        <li><a href="../../../">Home</a></li>
        <li><a href="../../../privacy/">Privacy</a></li>
        <li><a href="../../../report/">Report a Bug</a></li>
      </ul>
      
      <ul class="footer-right">
        <li>Created by <a href="https://github.com/SethClydesdale">Seth Clydesdale</a> and the <a href="https://github.com/SethClydesdale/pa-driver-tests/graphs/contributors">Github Community</a></li>
      </ul>
    </footer>
    
    <script src="../../../resources/easytimer.min.js"></script>
    <script src="../../../resources/ezquiz.min.js"></script>
    <script src="../../../resources/javascript.min.js"></script>
    <script>EZQuiz.generate({
      info : 'This test reviews what you have learned in Chapter 2 (p.7-22) of the Pennsylvania Driver\\'s Manual.<br>Answer the questions as best as you can.',

      quiz : ["""

end = """
      ]
    });</script>
  </body>
</html>"""
questions = """        {
          question : 'When you see this sign, you must:',
          image : 'c2-q01.png',
          answers : [
            '+Stop completely, check for pedestrians, and cross traffic',
            'Slow down without coming to a complete stop',
            'Stop completely and wait for a green light',
            'Slow down and check for traffic'
          ]
        },"""

quest = []

def opentext():
    rep = filedialog.askopenfilenames(
        # parent=root,
        initialdir=os.getcwd() + "data",
        initialfile='tmp',
        filetypes=[
            ("TXT", "*.txt")])
    return rep


name = opentext()
with open(name[0]) as file:
    file = file.read()
    # store a question in each item of cont
    cont = [l for l in file.split("\n\n")]

testo = ""
for q in cont:
    q = q.split("\n")
    # first answer is right
    q[1] = "+" + q[1]
    answers = q[:]
    answers.pop(0)
    # shuffle answers and then add to q
    shuffle(answers)
    q = [q[0], *answers]
    print(q)
    testo += f"{{question:\'{q[0]}\', image: '', answers : [\'{q[1]}\',\'{q[2]}\',\'{q[3]}\',\'{q[4]}\']}},\n"
    quest.append(testo)


html = start + "".join(testo) + end
def createfile(name, html):
    with open("data/review/" + name, "w") as newfile:
        newfile.write(html)
    return html


createfile("02.html", html)
print(os.getcwd())
os.startfile("data\\review\\02.html")
