from resource.start import start, end
import os
from createfile import createfile
from tkinter import filedialog

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
