import random
welcome_message = """
          Welcome to 'Pig', a dice game!
   
    In this game, a user and a computer opponent
    roll a 6-sided die each round. If the value of
    the die is a 1, the player that rolled the 1 loses
    all of their points. Otherwise, the player gets the
    value of the die added to their points. The first
    player to reach 30 points wins!
"""
def update_score(score,player_score):
    if player_score==1:
        return 1
    else:
        return score+player_score
def display_scoreboard2(player_score,computer_score):
    print("#"*20)
    print(f"Player Score:{player_score}")
    print(f"Computer Score:{computer_score}")
    print("#"*20)
def display_scoreboard3(player1_score,player2_score,player3_score):
    print("#"*20)
    print(f"{user_name} Score:{player1_score}")
    print(f"Player2 Score:{player2_score}")
    print(f"Player3 Score:{player3_score}")
    print("#"*20)
def display_scoreboard4(player1_score,player2_score,player3_score,player4_score):
    print("#"*20)
    print(f"{user_name} rolls a {player1_score}")
    print(f"Player2 Score:{player2_score}")
    print(f"Player3 Score:{player3_score}")
    print(f"Player4 Score:{player4_score}")
    print("#"*20)

print(welcome_message)
user_name=input("Enter your name: ")
player_score=0
player2_score=0
player3_score=0
player4_score=0
computer_score=0
no_of_players=int(input("Enter the number of players you want to play: "))
while True:
    if no_of_players==2:
        input(f"Press 'Enter' to roll the die {user_name}!\n")
        player_dice_value=random.randint(1,6)
        print(f"{user_name} rolls a {player_dice_value}")
        computer_dice_value=random.randint(1,6)
        print(f"Computer rolls a {computer_dice_value}")
        player_score=update_score(player_score,player_dice_value)
        computer_score=update_score(computer_score,computer_dice_value)
        display_scoreboard2(player_score,computer_score)
        if player_score>=30:
            if player_score>computer_score:
                print(f"{user_name} wins")
                break
        if computer_score>=30:
                if computer_score>player_score:
                    print(f"Computer Wins")
                    break
    if no_of_players==3:
        input(f"press 'Enter' to roll the dice {user_name}!\n")
        player1_dice_value=random.randint(1,6)
        print(f"{user_name} rolls a {player1_dice_value}")
        player2_dice_value=random.randint(1,6)
        print(f"Player2 rolls a {player2_dice_value}")
        player3_dice_value=random.randint(1,6)
        print(f"Player3 rolls a {player3_dice_value}")
        player_score=update_score(player_score,player1_dice_value)
        player2_score=update_score(player2_score,player2_dice_value)
        player3_score=update_score(player3_score,player3_dice_value)
        display_scoreboard3(player_score,player2_score,player3_score)

        if player_score>=30:
            if player_score>player2_score and player_score>player3_score:
                print(f"{user_name} wins!!!")
                break
        if player2_score>=30:
            if player2_score>player_score and player2_score>player3_score:
                print(f"Player2 wins!!!")
                break
        if player3_score>=30:
            if player3_score>player_score and player3_score>player2_score:
                print(f"Player3 wins!!!")
                break

    if no_of_players==4:
            input(f"press 'Enter' to roll the dice {user_name}!\n")
            player1_dice_value=random.randint(1,6)
            print(f"{user_name} rolls a {player1_dice_value}")
            player2_dice_value=random.randint(1,6)
            print(f"Player2 rolls a {player2_dice_value}")
            player3_dice_value=random.randint(1,6)
            print(f"Player3 rolls a {player3_dice_value}")
            player4_dice_value=random.randint(1,6)
            print(f"Player4 rolls a {player4_dice_value}")
            player_score=update_score(player_score,player1_dice_value)
            player2_score=update_score(player2_score,player2_dice_value)
            player3_score=update_score(player3_score,player3_dice_value)
            player4_score=update_score(player4_score,player4_dice_value)
            display_scoreboard4(player_score,player2_score,player3_score,player4_score)

            if player_score>=30:
                if player_score>player2_score and player_score>player3_score and player_score>player4_score:
                    print(f"{user_name} wins!!!")
                    break
            if player2_score>=30:
                if player2_score>player_score and player2_score>player3_score and player2_score>player4_score:
                    print(f"Player2 wins!!!")
                    break

            if player3_score>=30:
                if player3_score>player_score and player3_score>player2_score and player3_score>player4_score:
                    print(f"Player3 wins!!!")
                    break

            if player4_score>=30:
                if player4_score>player_score and player4_score>player2_score and player4_score>player3_score:
                    print(f"Player4 wins!!!")
                    break
            

            

            

            

            

            

            

            


        


