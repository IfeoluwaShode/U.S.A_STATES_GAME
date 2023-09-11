from turtle import Turtle, Screen
import pandas

# Create Turtle and Screen objects
turtle = Turtle()
screen = Screen()
screen.title("U.S STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load state data
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

# Initialize variables
guess_count = 0
guess_list = []
missing_state = []


while len(guess_list) < 50:
    user_guess = screen.textinput(title=f"{guess_count}/50 correct", prompt="What's another state name").title()

    if user_guess == "Exit":
        break

    if user_guess in states and user_guess not in guess_list:
        guess_count += 1
        guess_list.append(user_guess)

        # Get state coordinates
        state_data = data[data.state == user_guess]
        x_cor = int(state_data.x)
        y_cor = int(state_data.y)

        # Create Turtle for the guessed state
        state_turtle = Turtle()
        state_turtle.penup()
        state_turtle.hideturtle()
        state_turtle.goto(x_cor, y_cor)
        state_turtle.write(arg=f"{user_guess}", align="center", font=("Arial", 8, "normal"))

# Find missing states
for i in states:
    if i not in guess_list:
        missing_state.append(i)

# Save missing states to a CSV file
data_2 = pandas.DataFrame(missing_state, columns=["Missing States"])
data_2.to_csv("states_to_learn.csv", index=False)

# Close the window when done
screen.exitonclick()
