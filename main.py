class Element:
    def __init__(self, row: int, column: int, value: int):
        self.options = []
        if (value != 0) and (0 < int(value) < 10):
            self.value = int(value)
        else:
            self.value = 0
            self.options = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        self.row = row
        self.column = column
        self.square = (self.column // 3) + (3*(self.row//3))

    def updateValues(self, values):
        for value in values:
            # print(f"values = {values} options = {self.options}")
            if value in self.options:
                self.options.remove(value)
                if len(self.options) == 1:
                    self.setValue(self.options[0])

    def setValue(self, value):
        self.value = value
        self.options = []


class Game:
    def __init__(self, start):
        self.result = start
        self.rows = [[], [], [], [], [], [], [], [], []]
        self.columns = [[], [], [], [], [], [], [], [], []]
        self.squares = [[], [], [], [], [], [], [], [], []]
        for rowIndex, row in enumerate(start):
            for columnIndex, value in enumerate(row):
                element = Element(rowIndex, columnIndex, value)
                self.rows[rowIndex].append(element)
                self.columns[columnIndex].append(element)
                self.squares[(columnIndex // 3) + (3*(rowIndex//3))].append(element)

    def show(self):
        for row in self.rows:
            values = [element.value for element in row]
            print(values)

    def removeExisting(self, elementTable):
        for elementList in elementTable:
            values = [item.value for item in elementList if item.value]
            for element in elementList:
                if element.value == 0:
                    element.updateValues(values)
                    if element.value:
                        return 1
        return None

    def findUnique(self, elementTable):
        for elementList in elementTable:
            elementPending = [
                element for element in elementList if element.value == 0]
            for element in elementPending:
                for option in element.options:
                    existingList = [
                        element for element in elementPending if option in element.options]
                    if len(existingList) == 1:
                        element.setValue(option)
                        return 1
        return None

    def solve(self):
        if self.removeExisting(self.rows):
            return
        if self.removeExisting(self.columns):
            return
        if self.removeExisting(self.squares):
            return

        if self.findUnique(self.rows):
            return
        if self.findUnique(self.columns):
            return
        if self.findUnique(self.squares):
            return


if __name__ == "__main__":
    # {"board":[[7,5,0,3,9,0,0,0,0],[1,0,4,0,6,8,0,0,0],[6,0,9,0,5,7,0,0,0],[2,0,3,5,0,0,0,0,0],[4,0,0,7,0,9,0,3,1],[0,9,7,1,0,3,6,4,0],[0,0,1,0,0,0,0,0,0],[5,4,8,0,0,2,7,1,6],[0,7,0,0,0,4,0,0,0]]}
    init = [[7,5,0, 3,9,0, 0,0,0],
            [1,0,4, 0,6,8, 0,0,0],
            [6,0,9, 0,5,7, 0,0,0],

            [2,0,3, 5,0,0, 0,0,0],
            [4,0,0, 7,0,9, 0,3,1],
            [0,9,7, 1,0,3, 6,4,0],
            
            [0,0,1, 0,0,0, 0,0,0],
            [5,4,8, 0,0,2, 7,1,6],
            [0,7,0, 0,0,4, 0,0,0]]
    # init = [[0, 0, 0, 0, 5, 0, 6, 9, 0], [2, 0, 5, 6, 0, 0, 0, 0, 0], [6, 0, 0, 0, 0, 7, 0, 3, 0],
    #         [0, 0, 8, 0, 2, 0, 0, 4, 0], [4, 0, 0, 5, 0, 9, 0, 0, 8], [0, 5, 0, 0, 3, 0, 2, 0, 0],
    #         [0, 7, 0, 1, 0, 0, 0, 0, 4], [0, 0, 0, 0, 0, 5, 1, 0, 7], [0, 1, 2, 0, 7, 0, 0, 0, 0]]

    game = Game(init)
    print("\nInitialization")
    game.show()

    for x in range(91):
        game.solve()

    print("---------------------------")
    print("\nResults")
    game.show()
