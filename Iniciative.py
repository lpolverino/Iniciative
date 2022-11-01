class Creature:
    def __init__(self,number, name):
        self.number = number
        self.name = name
    def __repr__(self):
        return f"<{self.number}, {self.name}>"
    def __str__(self):
        return f"<{self.number}, {self.name}>"

class Iniciativa:
    def __init__(self):
        self.list = []
        self.traker = 0
        print("TIRA INICIATIVA")
    
    def agregar(self, creature):
        if len(self.list) != 0:
            current_turn = self.list[self.traker]
        else:
            current_turn = creature

        self.list.insert(0,creature)
        for idx,turn in enumerate(self.list):
            if (turn.number < creature.number) and (idx!= 0):
                self.list[idx -1] = self.list[idx]
                self.list[idx] = creature
        self.traker = self.list.index(current_turn)

    def eliminar(self,creature):
        idx = self.list.index(creature)
        if creature.number < self.list[self.traker].number:
            self.traker -= 1
        if idx != len(self.list) -1:
            self.list =  self.list[:idx] + self.list[idx+1:]
        elif idx == len(self.list) -1:
            self.list = self.list[:idx]
        else:
            print(f"{creature.name} was not found")
    
    def show_turn(self):
        print(f"{self.list[self.traker]}")
    
    def next(self):
        self.traker += 1
        self.show_turn()
