from tkinter import *
from models import Snake, Food, GAME_WIDTH, GAME_HEIGHT, SPEED, BACKGROUND_COLOR

score = 0
direction = 'down'


def next_turn(snake, food):
    x, y = snake.move(direction)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score:{}".format(score))
        canves.delete("food")
        food = Food(canves)
    else:
        snake.remove_tail()

    if snake.check_collisions():
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction


def game_over():
    canves.delete(ALL)
    canves.create_text(
        canves.winfo_width() / 2, canves.winfo_height() / 2,
        font=('console', 70), text="GAME OVER", fill="red", tag="gameover"
    )
    play_again_btn = Button(window, text="PLAY AGAIN", font=('consoles', 30),
                            bg="#00FF00", fg="#000000", command=restart)
    canves.create_window(canves.winfo_width() / 2, canves.winfo_height() / 2 + 100,
                         window=play_again_btn, tag="gameover")


def restart():
    global score, direction
    score = 0
    direction = 'down'
    label.config(text="Score:0")
    canves.delete(ALL)

    snake = Snake(canves)
    food = Food(canves)
    next_turn(snake, food)


window = Tk()
window.title("Snake game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consoles', 40))
label.pack()

canves = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canves.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake(canves)
food = Food(canves)

next_turn(snake, food)

window.mainloop()
