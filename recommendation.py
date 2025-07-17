"""
def main():
    difficulty = input("Choose between easy and difficult ")
    player = input("choose between a single and multiple ")

    if difficulty == "difficult":
        if player == "single":
            recommend("Poker")  #recommending for difficult with single player
        elif player == "multiple":
            recommend("klondike") #recommending for difficult with multiple player
        else:
            print("Enter valid player")
    elif difficulty == "easy":
        if player == "multiple":
            recommend("Hearts")  #recommending for easy with multiple player
        else:
            recommend("Clock")  #recommending for easy with single player
    else:
        print("Enter valid difficulty")


def recommend(game):
    print("You might like", game)


main()
"""


def main():
    difficulty = input("Choose between easy and difficult ")
    if not (difficulty == "difficult" or difficulty == "easy"):
        print("Enter valid difficulty")
        return


    player = input("choose between a single and multiple ")
    if not (player == "single" or player == "multiple"):
        print("Enter valid player")
        return

    if difficulty == "difficult" and player == "single":
        recommend("Poker")  #recommending for difficult with single player
    elif difficulty == "difficult" and player == "multiple":
        recommend("klondike") #recommending for difficult with multiple player
    elif difficulty == "easy" and player == "multiple":
        recommend("Hearts")  #recommending for easy with multiple player
    else:
        recommend("Clock")  #recommending for easy with single player

def recommend(game):
    print("You might like", game)


main()