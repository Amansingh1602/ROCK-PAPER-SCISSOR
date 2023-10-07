import pyttsx3
import random
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #changing index changes voices but ony 0 and 1 are working here
engine.say("ROCK PAPER SCISSORS  !")
player_choice=int(input("ROCK PAPER SCISSORS ? TYPE 0 FOR ROCK, TYPE 1 FOR PAPER AND TYPE 2 FOR SCISSORS.\n"))
comp_choice = random.randint(0,2)
print(f"Computer has chosen {comp_choice}")
if (player_choice >=3 or player_choice<0):
    print("invalid input")
    engine.setProperty('voice', voices[0].id)
    engine.say("invalid input!")
elif (comp_choice>player_choice ):
    print("you lost honey, better luck next time...")
    engine.setProperty('voice', voices[1].id)
    engine.say("you lost honey, better luck next time...")
elif(player_choice > comp_choice):
    print("Smart play , congratulations you have wonnn....")
    engine.setProperty('voice', voices[1].id)
    engine.say("Smart play , congratulations you have wonn .... !")
elif(comp_choice== player_choice):
    print("Think more and try again no result...")
    engine.setProperty('voice', voices[0].id)
    engine.say("Think more and try again no result.... !")

engine.runAndWait()
