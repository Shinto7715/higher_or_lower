import random
import art
import game_data
import os
import time

def assign():
  return random.choice(game_data.data)

def comparison(option1, option2, user_choice):
  sum1 = option1["follower_count"]
  sum2 = option2["follower_count"]

  max = ""

  if sum1 > sum2:
    max = option1["name"]

  elif sum1 < sum2:
    max = option2["name"]

  if max == user_choice:
    return True
  
  else:
    return False
  
def play_higher_or_lower():
  playing_game = True

  while playing_game:
    score = 0

    still_guessing = True

    while still_guessing:
      os.system('cls')

      print(art.logo)

      person1 = assign()
      person2 = assign()

      if score > 0:
        person1 = person2
        person2 = assign()

        if person1 == person2:
          person2 = assign()

      elif score == 0:
        if person1 == person2:
          person2 = assign()

      print(f"Name: {person1["name"]}, Description: {person1["description"]}")
      print("vs")
      print(f"Name: {person2["name"]}, Description: {person2["description"]}")

      print("-------------------------------------------------------------")
      print(f"Current Score: {score}")
      print("-------------------------------------------------------------")

      guess = input("Enter the name of the person with a higher follower count: ")

      if comparison(person1, person2, guess):
        score += 1

      else:
        still_guessing = False

    play_again = input("Would you like to play again? (y/n): ").lower()

    if play_again == 'y':
      continue

    elif play_again == 'n':
      playing_game = False
      os.system('cls')
      print("Successfully Exited the game")

    else:
      playing_game = False
      print("Invalid Input. Taken as No.")

play_game = input("Do you want to play Higher or Lower? (y/n): ").lower()

if play_game == 'y':
  os.system('cls')
  print("Launching game please wait...")
  time.sleep(3)
  os.system('cls')
  play_higher_or_lower()

elif play_game == 'n':
  os.system('cls')
  print("Exit successful")
  time.sleep(3)
  os.system('cls')

else:
  os.system('cls')
  print("Invalid input, program exited")
  time.sleep(3)
  os.system('cls')