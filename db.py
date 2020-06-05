from player import Player, maria
import pickle
import json
def get_score(player):
    player = player
    high_score = player.money

    try:
        high_score_file = open("high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        print("The high score is", high_score)
    except IOError:

        print("There is no high score yet.")
    except ValueError:

        print("I'm confused. Starting with no high score.")

    return high_score


def save_high_score(new_high_score):
    try:

        high_score_file = open("high_score.txt", "w")
        high_score_file.write(str(new_high_score))
        high_score_file.close()
    except IOError:
        # Hm, can't write it.
        print("Unable to save the high score.")


def show_score(player):
    """ Main program is here. """
    # Get the high score
    high_score = get_score(player)

    # Get the score from the current game
    current_score = player.money
    try:
        # Ask the user for his/her score

        print("Tour current score is {}".format(current_score))
    except ValueError:
        # Error, can't turn what they typed into a number
        print("I don't understand what you typed.")

    # See if we have a new high score
    if current_score > high_score:
        # We do! Save to disk
        print("Yea! New high score!")
        save_high_score(current_score)
    else:
        print("Better luck next time.")
def save(player):
    player = player
    data = {'player_name' : player.name,
        'player.money': player.money}
    with open('data.json', 'wb') as f:
        pickle.dump(data, f)
    with open('data.json', 'rb') as f:
        data_new = pickle.load(f)
        print(data_new)
        return data_new
