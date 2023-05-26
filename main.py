import turtle as t
import pandas

states_data = pandas.read_csv("50_states.csv")
states_list = states_data.state.tolist()

screen = t.Screen()
screen.title("U.S. Naming Game")
bg_img = "blank_states_img.gif"
screen.addshape(bg_img)
t.shape(bg_img)
screen.tracer(0)
states_already_found = []


def state_found(state):
    new_state = t.Turtle()
    new_state.up()
    new_state.goto(state.x.item(), state.y.item())
    new_state.write(state.state.item(), align="center", font=("Time New Roman", 8, "normal"))
    new_state.hideturtle()
    states_already_found.append(state.state.item())


game_is_active = True
while game_is_active:
    user_answer_input = screen.textinput(title=f"{len(states_already_found)}/50 States Correct",
                                         prompt="What's another state's name?").title()
    if user_answer_input == "Exit":
        break
    if user_answer_input in states_already_found:
        print(f"{user_answer_input} was already found")
    elif user_answer_input in states_list:
        print(f"{user_answer_input} found!")
        state_row = states_data[states_data.state == user_answer_input]
        state_found(state_row)
    else:
        print(f"{user_answer_input} is not found!")

    screen.update()

# Creates a file that prints the list of states that weren't guessed
with open("./states_to_learn.csv", mode="w") as out_file:
    out_file.write("Missed States:\n")
    for state in states_list:
        if state not in states_already_found:
            out_file.write(f"{state}\n")
