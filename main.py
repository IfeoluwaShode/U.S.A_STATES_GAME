from turtle import Turtle, Screen
import pandas
turtle = Turtle()
screen = Screen()
screen.title("U.S STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guess_count = 0
guess_list = []
missing_state = []

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
while len(guess_list) < 50:
    user_guess = screen.textinput(title=f"{guess_count}/50 correct", prompt="What's another state name").title()
    state_data = data[data.state == user_guess]
    x_cor = int(state_data.x)
    y_cor = int(state_data.y)
    if user_guess == "Exit":
        break

    if user_guess in states and user_guess not in guess_list:
        guess_count += 1
        guess_list.append(user_guess)

        state_turtle = Turtle()
        state_turtle.penup()
        state_turtle.hideturtle()
        state_turtle.goto(x_cor, y_cor)
        state_turtle.write(arg=f"{user_guess}", align="center", font=("arial", 8, "normal"))


    for i in states:
        if i not in guess_list:
            missing_state.append(i)


    data_2 = pandas.DataFrame(missing_state)
    data_2.to_csv("states_to_learn.csv")
