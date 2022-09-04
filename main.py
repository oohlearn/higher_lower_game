import art
from game_data import data
print(art.logo)
import random
import replit
# score = 0

questions = []
def start():
  score = 0
  questions.append(random.choice(data))
  questions.append(random.choice(data))
  while questions[0] == questions[1]:
    questions[1] = random.choice(data)

  a = questions[0]
  b = questions[1]
  print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']} , {a['follower_count']}")

  print(art.vs)
  
  print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}, {b['follower_count']}")

  guess = input("Who has more followers? Type 'A' or 'B': ")
  answer = compare(a, b, guess)
  score = result(answer, score)
  while answer == True:
    replit.clear()
    print(art.logo)
    if a["follower_count"] > b["follower_count"]:
      b = random.choice(data)
    else:
      a = b
      b = random.choice(data)
    answer = next_round(answer, a, b, score)
    score = result(answer, score)
  
def compare(a, b, guess):
  if guess == "A":
    if a["follower_count"] < b["follower_count"]:
      return False
    else: return True
  else: 
    if a["follower_count"] > b["follower_count"]:
      return  False
    else: return True
  # print(answer)
    

def result(answer, score):
  if answer == True:
    score += 1
    return score
  else:
    replit.clear()
    print(art.logo)
    print(f"Sorry, that's wrong. Final score:{score}")
    return score


def next_round(answer, a, b, score):
  print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}, {a['follower_count']}")

  print(art.vs)
  print(f"You 're right! Current score:{score}")
  
  print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}, {b['follower_count']}")
  guess = input("Who has more followers? Type 'A' or 'B': ")
  answer = compare(a, b, guess)  
  return answer
    

start()
