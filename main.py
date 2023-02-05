import sys

sys.path.append('src/')

from src.regina import Regina

def main():
  
  print("*you enter the cafe*")
  myBot = Regina()
  while True:
    if myBot.read(input("You: ")) == False:
      break
    #Print("Regina: ", Regina.read())


main()