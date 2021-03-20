class Element:
    def __init__(self, row : int, column :int, value : int):
        
        self.options = []
        if (value != None) and (0 < int(value) < 10):
            self.value = int(value)
        else:
            self.value = None
            self.options = [1,2,3,4,5,6,7,8,9]

        self.row = row
        self.column = column
        self.square = (self.column // 3) + (3*(self.row//3))

    def updateValues(self, values):
        for value in values:
            #print(f"values = {values} options = {self.options}")
            if value in self.options:
                self.options.remove(value)
                if len(self.options) == 1:
                    self.value = self.options[0]
                    self.options = []
        


class Game:
    def __init__(self, table : []):
        self.result = init
        self.rows = [[],[], [], [], [], [], [], [], []]
        self.columns = [[],[], [], [], [], [], [], [], []]
        self.squares = [[],[], [], [], [], [], [], [], []]
        for rowIndex, row in enumerate(init):
            for columnIndex, value in enumerate(row):
                element = Element(rowIndex, columnIndex, value)
                self.rows[rowIndex].append(element)
                self.columns[columnIndex].append(element)
                self.squares[(columnIndex // 3) + (3*(rowIndex//3))].append(element)

    def solve(self):
        for row in self.rows:
            rowValues = [item.value for item in row if item.value != None]
            for element in row:
                if element.value == None:
                    element.updateValues(rowValues)
        for column in self.columns:
            columnValues = [item.value for item in column if item.value != None]
            for element in column:
                if element.value == None:
                    element.updateValues(columnValues)

        for square in self.squares:
            squareValues = [item.value for item in square if item.value != None]
            for element in square:
                if element.value == None:
                    element.updateValues(squareValues)






if __name__ == "__main__":
    init = []
    init.append([2,None,None,       None,3,None,        4,5,None])
    init.append([None,6,None,       9,1,None,           8,None,None])
    init.append([None,None,None,    None,None,4,        None,None,None])

    init.append([None,4,3,          None,None,None,     5,None,7])
    init.append([1,None,None,       None,None,None,     None,None,6])
    init.append([7,None,6,          None,None,None,     1,8,None])
    
    init.append([None,None,None,    8,None,None,        None,None,None])
    init.append([None,None,9,       None,2,5,           None,6,None])
    init.append([None,8,5,          None,7,None,        None,None,3])

    game = Game(init)
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()
    game.solve()

    print("\nInitialization")
    for row in init:
        print(row)

    print("---------------------------")
    print("\nResults")
    for row in game.rows:
        values = [value.value for value in row]
        print(values)
        


