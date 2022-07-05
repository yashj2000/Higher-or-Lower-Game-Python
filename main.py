from art import logo,vs
import random
score = 0
from replit import clear
from game_data import data
print(logo)
game_over = False
person_A = random.choice(data)
print(person_A["name"] + ", " + person_A["description"]+ ", " + person_A["country"])

while not game_over:
  print(vs)
  person_B = random.choice(data)
  print(person_B["name"] + ", " + person_B["description"]+ ", " + person_B["country"])
  ans = input("Press 'a' or 'b' : ")
  if ans == 'a' and int(person_A["follower_count"]) > int(person_B["follower_count"]):
    # win
    person_A = person_B
    print(f"You're right! Current Score: {score}")
    score += 1
    clear()
    print(person_A["name"] + ", " + person_A["description"]+ ", " + person_A["country"])
      
  elif ans == 'b' and int(person_B["follower_count"]) > int(person_A["follower_count"]):
    person_A = person_B
    print(f"You're right! Current Score: {score}")
    clear()
    score += 1
    print(person_A["name"] + ", " + person_A["description"]+ ", " + person_A["country"])
  else:
    #lose
    game_over = True
    clear()
    print(f"That's the wrong answer! Final Score: {score}")