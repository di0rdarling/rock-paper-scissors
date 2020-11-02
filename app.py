import random


def start_game():
    play_options = ['rock', 'paper', 'scissors']
    computer_points = 0
    player_points = 0

    # Game is best of three. The Player with more than 2 points automatically wins.
    while (computer_points < 2 and player_points < 2):

        # Computer randomly selects a play option.
        computer_selected_option = play_options[random.randint(
            0, len(play_options)-1)]
        player_selected_option = input('Rock, paper, scissors? \n')
        print('Computer: ' + computer_selected_option)
        print('You: ' + player_selected_option)

        if(player_selected_option.lower() == computer_selected_option):
            print('You both picked ' +
                  computer_selected_option + '. Try again \n')
        elif(player_selected_option in play_options):
            if(player_selected_option.lower() == 'rock'):
                if(computer_selected_option == 'paper'):
                    computer_points += 1
                    print('Computer wins!')
                elif(computer_selected_option == 'scissors'):
                    player_points += 1
                    print('You win!')
            elif(player_selected_option.lower() == 'scissors'):
                if(computer_selected_option == 'rock'):
                    computer_points += 1
                    print('Computer wins!')
                elif(computer_selected_option == 'paper'):
                    player_points += 1
                    print('You win!')
            elif(player_selected_option.lower() == 'paper'):
                if(computer_selected_option == 'scissors'):
                    computer_points += 1
                    print('Computer wins!')
                elif(computer_selected_option == 'rock'):
                    player_points += 1
                    print('You win!')
            print('Computer: ' + str(computer_points) +
                  ' | Player: ' + str(player_points) + '\n')
        else:
            print('Your input was incorrect. Please check your spelling. \n')

    if player_points == 2:
        print('Well done. You won!')
    else:
        print('Sorry. You lost')


start_game()
