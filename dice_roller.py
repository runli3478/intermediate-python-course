import random
dice_rolls = 2
dice_sum = 0

dice_size = int(input("How many dice would you want to roll?\n"))

for i in range(0,dice_rolls):
  roll = random.randint(1,dice_size)
  dice_sum += roll
  if roll == 1:
    print(f"You rolled a {roll}! Critical Fail")
  elif roll == dice_size:
    print(f'You rolled a {roll}! Critical Success!')
  else:
    print(f"You rolled a {roll}")
print(f'You have rolled a total of {dice_sum}')