import os
from time import sleep
from Board import Board

b = Board()

for i in range(40):
    os.system("cls")
    # os.system("clear")
    print(f"------- Tour {i}-------")
    b.afficher()
    b.effectuer_un_tour()
    sleep(0.5)
