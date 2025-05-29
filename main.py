#made by Quartzdude12 aka CAA or Betrayed_
import time
import math
import random
import os

def main():
  if os.name == 'nt':
    os.system('cls')
    # For Linux/Mac
  else:
      os.system('clear')
  sides = int(input("Sides: "))
  amount = int(input("How many times?: "))
  for i in range(amount):
    print(random.randint(1, sides))
  time.sleep(4)

main()