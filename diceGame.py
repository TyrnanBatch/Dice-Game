import random
import time

diceRollOne = random.randint(1, 6)
diceRollTwo = random.randint(1, 6)
diceRollThree = random.randint(1, 6)
diceRollFour = random.randint(1, 6)
diceRollFive = random.randint(1, 6)
diceRollSix = random.randint(1, 6)
diceRollSeven = random.randint(1, 6)
diceRollEight = random.randint(1, 6)
diceRollNine = random.randint(1, 6)
diceRollTen = random.randint(1, 6)
diceRollEleven = random.randint(1, 6)
diceRollTwelve = random.randint(1, 6)
diceRollThirteen = random.randint(1, 6)
diceRollFourteen = random.randint(1, 6)
diceRollFifteen = random.randint(1, 6)
diceRollSixteen = random.randint(1, 6)
diceRollSeventeen = random.randint(1, 6)
diceRollEighteen = random.randint(1, 6)
diceRollNineteen = random.randint(1, 6)
diceRollTwenty = random.randint(1, 6)

print("Player one  roll one: " + str(diceRollOne))
time.sleep(0.5)
print("Player one roll two: " + str(diceRollTwo))
time.sleep(0.5)
print("Player two roll one: " + str(diceRollThree))
time.sleep(0.5)
print("Player two roll two: " + str(diceRollFour))
time.sleep(0.5)
print("Player one roll three: " + str(diceRollFive))
time.sleep(0.5)
print("Player one roll four: " + str(diceRollSix))
time.sleep(0.5)
print("Player two roll three: " + str(diceRollSeven))
time.sleep(0.5)
print("Player two roll four: " + str(diceRollEight))
time.sleep(0.5)
print("Player one roll five: " + str(diceRollNine))
time.sleep(0.5)
print("Player one roll six: " + str(diceRollTen))
time.sleep(0.5)
print("Player two roll five: " + str(diceRollEleven))
time.sleep(0.5)
print("Player two roll six: " + str(diceRollTwelve))
time.sleep(0.5)
print("Player one roll seven: " + str(diceRollThirteen))
time.sleep(0.5)
print("Player one roll eight: " + str(diceRollFourteen))
time.sleep(0.5)
print("Player two roll seven: " + str(diceRollFifteen))
time.sleep(0.5)
print("Player two roll eight " + str(diceRollSixteen))
time.sleep(0.5)
print("Player one roll nine: " + str(diceRollSeventeen))
time.sleep(0.5)
print("Player one roll ten: " + str(diceRollEighteen))
time.sleep(0.5)
print("Player two roll nine: " + str(diceRollNineteen))
time.sleep(0.5)
print("Player two roll ten: " + str(diceRollTwenty))

playerOneScore = diceRollOne + diceRollThree + diceRollFive + diceRollSeven + diceRollNine + diceRollEleven + diceRollThirteen + diceRollFifteen + diceRollSeventeen + diceRollNineteen
playerTwoScore = diceRollTwo + diceRollFour + diceRollSix + diceRollEight + diceRollTen + diceRollTwelve + diceRollFourteen + diceRollSixteen + diceRollEighteen + diceRollTwenty

print("Scores before bonus points: Player one - " + str(playerOneScore) + " Player Two - " + str(playerTwoScore))

if playerOneScore % 2 == 0:
    playerOneScore += 10
else:
    playerOneScore -= 5

if playerTwoScore % 2 == 0:
    playerTwoScore += 10
else: playerTwoScore -= 5

print("Final scores: Player one - " + str(playerOneScore) + " Player two - " + str(playerTwoScore))

if playerOneScore > playerTwoScore:
    print("--- Player One Wins!!! ---")

if playerOneScore < playerTwoScore:
    print("--- Player Two Wins!!! ---")

