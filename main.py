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
                    self.setValue(self.options[0])

    def setValue(self, value):
        self.value = value
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

    def show(self):
        for row in self.rows:
            values = [element.value for element in row]
            print(values)



    def removeExisting(self, elementTable):
        for elementList in elementTable:
            values = [item.value for item in elementList if item.value != None]
            for element in elementList:
                if element.value == None:
                    element.updateValues(values)
                    if element.value != None:
                        return 1
        return None

    def findUnique(self, elementTable):
        for elementList in elementTable:
            elementPending = [element for element in elementList if element.value == None]
            for element in elementPending:
                for option in element.options:
                    existingList = [element for element in elementPending if option in element.options]
                    if len(existingList) == 1:
                        element.setValue(option)
                        return 1
        return None


    def solve(self):
        if self.removeExisting(self.rows) != None:
            return
        if self.removeExisting(self.columns) != None:
            return
        if self.removeExisting(self.squares) != None:
            return
        
        if self.findUnique(self.rows) != None:
            return
        if self.findUnique(self.columns) != None:
            return
        if self.findUnique(self.squares) != None:
            return
        
        

if __name__ == "__main__":
    init = []
    init.append([None,None,None,    None,5,None,        6,9,None])
    init.append([2,None,5,          6,None,None,        None,None,None])
    init.append([6,None,None,       None,None,7,        None,3,None])

    init.append([None,None,8,       None,2,None,        None,4,None])
    init.append([4,None,None,       5,None,9,           None,None,8])
    init.append([None,5,None,       None,3,None,        2,None,None])
    
    init.append([None,7,None,       1,None,None,        None,None,4])
    init.append([None,None,None,    None,None,5,        1,None,7])
    init.append([None,1,2,          None,7,None,        None,None,None])

    game = Game(init)
    print("\nInitialization")
    game.show()

    for x in range(91):
        game.solve()


    print("---------------------------")
    print("\nResults")
    game.show()
        


