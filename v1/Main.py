from random import choice, randrange

grid = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


def add_random(grid):
    cell = get_random_zero(grid)
    if cell:
        grid[cell[0]][cell[1]] = 2 * randrange(1, 3)
    else:
        print("No more room.")


def get_random_cell(grid):
    row = randrange(len(grid))
    col = randrange(len(grid[row]))
    return row, col, grid[row][col]


def get_random_zero(grid):
    zeros = find_zeros(grid)
    if len(zeros) > 0:
        return choice(find_zeros(grid))
    else:
        return False


def find_zeros(grid):
    cells = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 0:
                cells.append((row, col))
    return cells


def clean(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])-1):
            if grid[row][col] == 0:
                for index in range(col+1, len(grid[row])):
                    if grid[row][index] != 0:
                        grid[row][col] = grid[row][index]
                        grid[row][index] = 0
                        break


def merge(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])-1):
            if grid[row][col+1] == grid[row][col]:
                grid[row][col] *= 2
                grid[row][col+1] = 0


def rotate_clockwise(grid, num_of_times=1):  # doesnt work atm
    if num_of_times < 1:
        return list(map(list, grid))
    else:
        return rotate_clockwise(list(zip(*grid[::-1])), num_of_times-1)


def render(grid):
    for row in grid:
        print(row)


if __name__ == "__main__":
    while True:
        add_random(grid)
        render(grid)
        move = input()
        if move in ("up"):
            grid = rotate_clockwise(grid, 3)
            clean(grid)
            merge(grid)
            clean(grid)
            grid = rotate_clockwise(grid, 1)
        elif move in ("right"):
            grid = rotate_clockwise(grid, 2)
            clean(grid)
            merge(grid)
            clean(grid)
            grid = rotate_clockwise(grid, 2)
        elif move in ("down"):
            grid = rotate_clockwise(grid, 1)
            clean(grid)
            merge(grid)
            clean(grid)
            grid = rotate_clockwise(grid, 3)
        elif move in ("left"):
            clean(grid)
            merge(grid)
            clean(grid)
        elif move in ("exit", "quit"):
            break
        # add game over
        # need to make it so it doesnt add_random when move does not change the board
