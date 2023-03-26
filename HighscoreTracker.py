import random
import time
import os

def game():
    return random.randint(0,1000)

replay=None
delay=0.3
location = "highscore.txt"

while replay !="q":
    os.system("cls")
    print("***HIGH SCORE TRACKER***\n")
    time.sleep(delay)
    
    with open (location,"r") as f:
        latest_score = game()
        high_score = int(f.read())
        play = input("\nPress Enter to play")
        time.sleep(delay)

        print ("\n")
        print ("-"*50)
        print (f"Current Score: {latest_score}")
        time.sleep(delay)

        print (f"\nHigh Score: {high_score}")
        print ("-"*50)
        time.sleep(delay)

        if latest_score > high_score:
            with open (location,"w") as f:
                f.write(str(latest_score))
            print("\nCongratulations!!")
            time.sleep(delay)
            print("New High Score Updated...")
            time.sleep(delay)
        else:
            print ("\nYou could not beat the High Score!!")
        
        replay = input("\nPlay Again?\nPress 'Enter' to continue,\nPress 'q' to quit\nPress 'r' to reset High Score\n").lower()

        if replay == "r":
            with open (location,"w") as f:
                f.write('0')          



