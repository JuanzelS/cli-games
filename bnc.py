# cli-games/bnc.py

input = input("Greetings, what is your name? > ")
print("Greetings", input)
(cli-games) python3 bnc.py
# cli-games/bnc.py

player = input("Bear, Ninja, or Cowboy? > ")
print(player)
# Import the random method from the randint module
from random import randint

# Define roles
roles = ["Bear", "Ninja", "Cowboy"]

# Generate a random role using an array
computer = roles[randint(0,2)]

print(computer)
# cli-games/bnc.py

from random import randint

# Define roles
roles = ["Bear", "Ninja", "Cowboy"]

# Generate a random role using an array
computer = roles[randint(0,2)]

# Get player input
player = input("Bear, Ninja, or Cowboy? > ")

# Compare computer and player role

print(computer, player)
# cli-games/bnc.py
...
# Replace the print(computer, player) line with the following:
if computer == player:
  print("DRAW!")
else:
  print(computer, player)
   
   # cli-games/bnc.py
...

if computer == player:
  print("DRAW!")
elif computer == "Cowboy":
  if player == "Bear":
    print("You lose!", player, "is shot by", computer)
  else: # computer is cowboy, player is ninja
    print("You win!", player, "defeats", computer)
elif computer == "Bear":
  if player == "Cowboy":
    print("You win!", player, "shoots", computer)
  else: # computer is bear, player is ninja
    print("You lose!", player, "is eaten by", computer)
elif computer == "Ninja":
  if player == "Cowboy":
    print("You lose!", player, "is defeated by", computer)
  else: # computer is ninja, player is bear
    print("You win!", player, "eats", computer)
    # cli-games/bnc.py

...
if computer == player:
  print("DRAW!")
elif computer == "Cowboy":
  if player == "Bear":
    print("You lose!", player, "is shot by", computer)
  else: # computer is cowboy, player is ninja
    print("You win!", player, "defeats", computer)
elif computer == "Bear":
  if player == "Cowboy":
    print("You win!", player, "shoots", computer)
  else: # computer is bear, player is ninja
    print("You lose!", player, "is eaten by", computer)
elif computer == "Ninja":
  if player == "Cowboy":
    print("You lose!", player, "is defeated by", computer)
  else: # computer is ninja, player is bear
    print("You win!", player, "eats", computer)
    # cli-games/bnc.py

...

player = False

while player == False:
    # Get player input
    player = input("Bear, Ninja, or Cowboy? > ")

    # Compare computer and player role

    if computer == player:
      print("DRAW!")
    elif computer == "Cowboy":
      if player == "Bear":
        print("You lose!", computer, "shoots", player)
      else: # computer is cowboy, player is ninja
        print("You win!", player, "defeats", computer)
    elif computer == "Bear":
      if player == "Cowboy":
        print("You win!", player, "shoots", computer)
      else: # computer is bear, player is ninja
        print("You lose!", computer, "eats", player)
    elif computer == "Ninja":
      if player == "Cowboy":
        print("You lose!", computer, "defeats", player)
      else: # computer is ninja, player is bear
        print("You win!", player, "eats", computer)

    player = False
    computer = roles[randint(0,2)]
    # cli-games/bnc.py

...

    # after checking who won, put the following code

    play_again = input("Would you like to play again? (yes/no) > ")
    if play_again == 'yes':
      player = False
      computer = roles[randint(0,2)]
    else:
      break
