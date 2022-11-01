#!python3 -main.py - es una pequeña aplicaicon para llevar cuenta de la 
# iniciativa en un juego de rol

from re import I
from Iniciative import Iniciativa
from Iniciative import Creature

if __name__ == "__main__":
    incitive = Iniciativa()
    heroe = Creature(15, "heroe")
    villano = Creature(20,"Villano")
    mounstro = Creature(17,"mounstro")
    incitive.agregar(heroe)
    incitive.agregar(villano)
    incitive.agregar(mounstro)
    print(incitive.list)
    incitive.eliminar(heroe)
    print(incitive.list)
    incitive.show_turn()
    incitive.next()
