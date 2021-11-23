import turtle
import pandas

image = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)
timmy = turtle.Turtle()
timmy.penup()
timmy.hideturtle()

data = pandas.read_csv("50_states.csv")
# if (data[data.state == answer_state.title()]):
#     print("OK")
# else:
#     print("NOK")
correct_answer = 0
correct_guesses = []
total_states = data.state.count()
answer_state = (screen.textinput(title="Guess the State", prompt="What's another state's name?")).title() 

while len(correct_guesses) < 50:
    if answer_state == "Exit":
        missing_states = []
        for state in data.state.values:
            if state not in correct_guesses:
                missing_states.append(state)
        learn_data = {
            "State To Learn": missing_states
        }
        df = pandas.DataFrame(learn_data)
        df.to_csv("states_to_learn.csv")
        break
    if answer_state not in correct_guesses:    
        if (answer_state in data.state.values):
                x = int(data[data.state == answer_state.title()]["x"])
                y = int(data[data.state == answer_state.title()]["y"])
                timmy.goto(x, y)
                timmy.write(f"{answer_state}")
                correct_answer += 1
                correct_guesses.append(answer_state)

    answer_state = (screen.textinput(title=f"{correct_answer}/{total_states} States Correct", prompt="What's another state's name?")).title()
 


