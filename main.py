#!python3 -main.py - es una pequeña aplicaicon para llevar cuenta de la 
# iniciativa en un juego de rol

from re import I
from Iniciative import Iniciativa
from Iniciative import Creature

if __name__ == "__main__":
    incitive = Iniciativa()
    #heroe = Creature(15, "heroe")
    #villano = Creature(20,"Villano")
    #mounstro = Creature(17,"mounstro")
    #incitive.agregar(heroe)
    #incitive.agregar(villano)
    #incitive.agregar(mounstro)
    #print(incitive.list)
    #incitive.eliminar(heroe)
    #print(incitive.list)
    #incitive.show_turn()
    #incitive.next()
    #heroe = Creature("heroe")
    #villano = Creature("Villano")
    #mounstro = Creature("mounstro")
    incitive.agregar(15, "heroe")
    incitive.agregar(17, "villano")
    incitive.agregar(16,"mounstro")
    print(incitive.list)
    incitive.eliminar("heeroe")
    incitive.insertCondition("vVllano","paralizado",1)
    incitive.insertCondition("villano","encantado",10)
    print(incitive.list)
    incitive.show_turn()
    incitive.next()
    print(incitive.list)


