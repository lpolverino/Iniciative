class Creature:
    def __init__(self, name):
        #self.number = number
        self.name = name
        self.conditions={}

    def agCondition(self, name, time):
        self.conditions.update({name:time})

    def __repr__(self):
        return f"<{self.name}, {self.conditions}>"
    
    def __str__(self):
        return f"<{self.name}, {self.conditions}>"

class Iniciativa:
    def __init__(self):
        self.list = []
        self.traker = 0
        print("TIRA INICIATIVA")
    
    def agregar(self, roll, creature):
        creature = (roll, Creature(creature))
        if len(self.list) != 0:
            current_turn = self.list[self.traker]
        else:
            current_turn = creature
        self.list.insert(0,creature)
        for idx,turn in enumerate(self.list):
            if (turn[0] < creature[0]) and (idx!= 0):
                self.list[idx -1] = self.list[idx]
                self.list[idx] = creature
        self.traker = self.list.index(current_turn)

    def eliminar(self,creature):
        try:
            idx = [tup[1].name for tup in self.list].index(creature) #habra forma mas facil?
            creature = self.list[idx]
            if creature[0]< self.list[self.traker][0]:
                self.traker -= 1
            if idx != len(self.list) -1:
                self.list =  self.list[:idx] + self.list[idx+1:]
            elif idx == len(self.list) -1:
                self.list = self.list[:idx]
            else:
                print(f"{creature.name} was not found")
        except:
            print(f"No se puede sacar a {creature}")

    def insertCondition(self, creature_name, condition, time):
        try:
            idx = [tup[1].name for tup in self.list].index(creature_name)
            creature = self.list[idx][1]
            creature.agCondition(condition, time)
        except:
            print(f"no se puede modificar a {creature_name}")
    
    def show_turn(self):
        print(f"{self.list[self.traker]}")
    
    def next(self):
        self.traker += 1
        creature = self.list[self.traker]
        poped = []
        for condition, time in creature[1].conditions.items():
            if time == 1:
                poped.append(condition)
            else: 
                creature[1].conditions.update({condition:time-1})
        for condition in poped:
            creature[1].conditions.pop(condition)
        self.show_turn()
