import random

roll = random.randint(1, 6)
howManyRolls = int(input("How many times should I roll?"))
i = 0;

while (i < howManyRolls):
    roll = random.randint(1, 6)
    print(roll)
    i += 1

for i in range (len(rolls)):
    print(f"{i + 1}: {rolls[i]}/{numRolls} = {rolls[i]/numRolls*100}
