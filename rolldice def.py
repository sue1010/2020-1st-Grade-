import random

def rollDice():
    face = random.randint(1,6)
    return face

i = 0
while i < 4:
    print("주사위의 값=", rollDice())
    i = i + 1
    
