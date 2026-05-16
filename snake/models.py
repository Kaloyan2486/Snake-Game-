import random

GAME_WIDTH = 1700
GAME_HEIGHT = 1000
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
HEAD_COLOR = "#0C7936"
SNAKE_COLOR = "#692929"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Snake:

    def __init__(self, canvas):
        self.canvas = canvas
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = self.canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                fill=SNAKE_COLOR, tag="snake"
            )
            self.squares.append(square)

    def move(self, direction):
        x, y = self.coordinates[0]

        if direction == "up":
            y -= SPACE_SIZE
        elif direction == "down":
            y += SPACE_SIZE
        elif direction == "left":
            x -= SPACE_SIZE
        elif direction == "right":
            x += SPACE_SIZE

        self.coordinates.insert(0, (x, y))

        square = self.canvas.create_rectangle(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=HEAD_COLOR
        )
        self.squares.insert(0, square)

        if len(self.squares) > 1:
            self.canvas.itemconfig(self.squares[1], fill=SNAKE_COLOR)

        return x, y

    def remove_tail(self):
        del self.coordinates[-1]
        self.canvas.delete(self.squares[-1])
        del self.squares[-1]

    def check_collisions(self):
        x, y = self.coordinates[0]

        if x < 0 or x >= GAME_WIDTH:
            return True
        elif y < 0 or y >= GAME_HEIGHT:
            return True

        for body_part in self.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True

        return False


class Food:

    def __init__(self, canvas):
        self.canvas = canvas

        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        self.canvas.create_oval(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE,
            fill=FOOD_COLOR, tag="food"
        )
