from berserk import Berserk
from lessson3.character import  Character

player1 = Berserk(name="Vasya", damage=10)
player2 = Character(name="Petya", damage=15)

print(player1, "\n")
print(player2, "\n")

while player1.is_alive() and player2.is_alive():
player1.attack(player2)
player2.attack(player1)

print(player1, "\n")
print(player2, "\n")