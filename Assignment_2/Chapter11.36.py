import turtle
import random

turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("white")
turtle.title("Self-Avoiding Random Walk")

GRID_SIZE = 16
CELL_SIZE = 20
def is_valid(x, y, visited):
    return 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE and not visited[y][x]
def self_avoiding_walk():
    visited = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
    x, y = GRID_SIZE // 2, GRID_SIZE // 2
    turtle.penup()
    turtle.goto(x * CELL_SIZE, y * CELL_SIZE)
    turtle.pendown()

    while True:
        visited[y][x] = True
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        random.shuffle(directions)

        valid_moves = [(dx, dy) for dx, dy in directions if is_valid(x + dx, y + dy, visited)]
        if not valid_moves:
            break

        dx, dy = random.choice(valid_moves)
        x += dx
        y += dy
        turtle.goto(x * CELL_SIZE, y * CELL_SIZE)

self_avoiding_walk()
turtle.done()
