import json
import re
import random
from rps import Rps
from ttt import TicTacToe


class Regina:

  def __init__(self):
    print("Regina: Welcome to my cafe!")

  def load_json(file):
    with open(file) as bot_responses:
      #print(f"Loaded '{file}' successfully!")
      return json.load(bot_responses)

  response_data = load_json("src/bot.json")

  def read(self, str):
    if str == "exit":
      print("Regina: oki doki artichokie see u later")
      return False
      print("test1")

    split_message = re.split(r'\s+|[,;?!.-]\s*', str.lower())
    score_list = []

    # Check all the responses
    for response in self.response_data:
      response_score = 0
      required_score = 0
      required_words = response["required_words"]

      # Check if there are any required words
      if required_words:
        for word in split_message:
          if word in required_words:
            required_score += 1

      # Amount of required words should match the required score
      if required_score == len(required_words):
        # print(required_score == len(required_words))
        # Check each word the user has typed
        for word in split_message:
          # If the word is in the response, add to the score
          if word in response["user_input"]:
            response_score += 1

      # Add score to list
      score_list.append(response_score)
      # Debugging: Find the best phrase
      # print(response_score, response["user_input"])

    # Find the best response and return it if they're not all 0
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    # Check if input is empty
    if str == "":
      return "Please type something so we can chat :("

    elif best_response != 0:
      print(self.response_data[response_index]["bot_response"])

    elif str == "rps":
      Rps.playrps(self)
      print("Regina: Good game!")

    elif str == "ttt":
      TicTacToe.playttt(self)
      print("Regina: Good game!")

    # If there is no good response, return a random one.
    elif str != "rock" or "paper" or "scissors":
      print(
        random.choice([
          "Please try writing something more descriptive.",
          "Oh! It appears you wrote something I don't understand yet",
          "Do you mind trying to rephrase that?",
          "I'm terribly sorry, I didn't quite catch that.",
          "I can't answer that yet, please try asking something else."
        ]))
