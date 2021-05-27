import random #this is the imported ramdom libry to make the bot choice ramdom 
hands=["paper","scissors","rock"]
GAMEOVER=["well played","play again?","you are good at this","this code is awesome"]
user_score = 0 # this is so the user can quit after they lose 3 times 

#this print the title of game and who worte the code for it
print(" THIS GAME WAS MADE BY LEON FORD AND LIAM HOWDEN")
print("")
print("")
print("In this game you will need to type the hole word as i am to lazy right now sorry")
print("")

while user_score != 10: 
    user_input = input("Choose rock, paper, scissors:")
    bot_choice = random.choice(hands)
    
#this is if thge user choice is the same as the bots it prints try again 
    if user_input.lower() == bot_choice:
        print("")
        print("same choice please try again")
        print("") #this is the users inputs and the bots choices and all the print satments is to make spaces in between the lines 

       #this is the times when you lose, you lose a point 
    
    elif user_input == "scissors" and bot_choice == "rock":
       print("")
       print("Bot chose Rock Bot wins")
       print("")
       user_score -= 1
       print("this is your score", user_score)
       
    elif user_input == "rock" and bot_choice == "paper":
       print("")
       print("Bot chose paper Bot wins")
       print("")
       user_score -=1 
       print("this is your score", user_score)
        
    elif user_input == "paper" and bot_choice == "scissors":
       print("")
       print("Bot chose scissors Bot wins")
       print("")
       user_score -= 1 
       print("this is your score", user_score)

      #this is the times when you the user wins,you win two points so the game will not be a stale mate  
    elif user_input == "rock" and bot_choice == "scissors":
       print("")
       print("Bot chose scissors you chose Rock you win")
       print("")
       user_score +=2
       print("this is your score", user_score)
  
       
    elif user_input == "scissors" and bot_choice == "paper":
       print("")
       print("Bot chose paper you chose scissors you win")
       print("")
       user_score +=2
       print("this is your score", user_score)

    elif user_input == "paper" and bot_choice == "rock":
       print("")
       print("Bot chose rock you chose paper you win")
       print("")
       user_score +=2
       print("this is your score", user_score )
#it is so satifaing to win



#this code is to end the game
    
print("gameover")
#this statment is to make the bot say somthing nice after you win as you can not lose (yet?) 
bot_talk =print(random.choice(GAMEOVER))


