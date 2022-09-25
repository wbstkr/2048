import random


class Grid:
    def __init__(self):
        self.board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.gameover = False

    def add(self):
        x, y = random.randint(0, 3), random.randint(0, 3)
        while self.board[x][y] != 0:
            x, y = random.randint(0, 3), random.randint(0, 3)
        self.board[x][y] = 2**random.randint(1, 2)

    def spawn(self):
        space = False
        for row in self.board:
            if row.count(0) > 0:
                space = True
                break
        if space:
            self.add()
        else:
            self.gameover = True

    def render(self):
        print()
        for row in self.board:
            for index in row:
                if index < 10:
                    print(" ", end="")
                print(index, end=" ")
            print()
            print()

    def slide(self):
        for row in self.board:
            for counter in range(1, 4):
                for index in range(counter, 4):
                    if row[index] != 0 and (row[index - 1] == 0 or row[index - 1] == row[index]):
                        row[index - 1] = row[index] + row[index - 1]
                        row[index] = 0

    def turn(self, n):
        for counter in range(n):
            temp = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
            for rowindex in range(4):
                for index in range(4):
                    temp[3 - index][rowindex] = self.board[rowindex][index]
            self.board = temp

    def move(self, d):
        if d == "left":
            self.slide()
        if d == "up":
            self.turn(1)
            self.slide()
            self.turn(3)
        if d == "right":
            self.turn(2)
            self.slide()
            self.turn(2)
        if d == "down":
            self.turn(3)
            self.slide()
            self.turn(1)

    def play(self):
        x = ""
        while not self.gameover:
            self.spawn()
            self.render()
            x = str(input("Direction>"))
            if x == "quit":
                break
            self.move(x)
        print("GAME OVER")


game = Grid()
game.play()
