import random


class rpsGame:
    def __init__(self):
        self._humanPlayer = self.Player(_type="Human")
        self._computerPlayer = self.Player(_type="Computer")

        # Set Possible Options
        self._choice_options = ["Rock", "Paper", "Scissors"]

        self._gamesPlayed = 0

        self._results = (0, 0, 0)

    def __rules__(self, player1_choice, player2_choice):
        if player1_choice == "Rock":
            if player2_choice == "Rock":
                winner = "Tie"
            elif player2_choice == "Paper":
                winner = "Player 2"
            elif player2_choice == "Scissors":
                winner = "Player 1"
        elif player1_choice == "Paper":
            if player2_choice == "Rock":
                winner = "Player 1"
            elif player2_choice == "Paper":
                winner = "Tie"
            elif player2_choice == "Scissors":
                winner = "Player 2"
        elif player1_choice == "Scissors":
            if player2_choice == "Rock":
                winner = "Player 2"
            elif player2_choice == "Paper":
                winner = "Player 1"
            elif player2_choice == "Scissors":
                winner = "Tie"

        return winner

    def __evaluateGame__(self):
        result = self.__rules__(player1_choice = self._humanPlayer._latestChoice, player2_choice = self._computerPlayer._latestChoice)
        if result == "Player 1":
            self._humanPlayer._results[0] += 1
            self._computerPlayer._results[1] += 1
            print("Congratulations, you won this round!")
        elif result == "Player 2":
            self._humanPlayer._results[1] += 1
            self._computerPlayer._results[0] += 1
            print("Sorry, the Computer won this round. Try Again!")
        else:
            self._humanPlayer._results[2] += 1
            self._computerPlayer._results[2] += 1
            print("This round's a Tie!")

    def __quitGame__(self):
        print("You have chosen to quit the game.")
        self._humanPlayer.__seePlayerScore__()


    def __playTurn__(self, choice):
        if choice in self._choice_options:
            self._computerPlayer.__playTurn__(opponent=self._humanPlayer)
            print("Computer Played: " + str(self._computerPlayer._latestChoice))
            self._humanPlayer.__playTurn__(choice)

            self.__evaluateGame__()

            #self.__seeResults__()

            self._results = self._humanPlayer._results

            self._gamesPlayed += 1

    def __seeResults__(self):
        self._humanPlayer.__seePlayerResults__()

    def __showScore__(self):
        self._humanPlayer.__seePlayerScore__()

    def __seeGameHistory__(self):
        self._computerPlayer.__seePlayerHistory__()
        self._humanPlayer.__seePlayerHistory__()

    class Player:
        def __init__(self, _type):
            # Set Possible Options
            self._player_options = ("Human", "Computer")

            # Set Possible Options
            self._choice_options = ["Rock", "Paper", "Scissors"]

            if _type in self._player_options:
                self._type = _type
            else:
                print("Pick Valid Player Option: Human or Computer")

            self._history = {"Rock": 0,
                             "Paper": 0,
                             "Scissors": 0}

            self._results = [0, 0, 0]

            self._gamesPlayed = 0

            self._latestChoice = None

        def __inputChoice__(self, choice):
            # if self._type == "Computer":
            #     print("You cannot play for the computer.")
            # else:
            if choice in self._choice_options:
                #if self._type == "Computer"
                self._history[choice] += 1
                self._latestChoice = choice
                self._gamesPlayed += 1
            else:
                print("Pick Valid Choice: Rock, Paper, or Scissors")

        def __seePlayerResults__(self):
            print(self._type + " has chosen " + str(self._latestChoice))

        def __seePlayerScore__(self):
            print(self._type + " has played " + str(self._gamesPlayed) + " games. Their record is: " +
                  str(self._results[0]) + " Wins, " +
                  str(self._results[1]) + " Losses, " +
                  str(self._results[2]) + " Ties."
                  )

        def __seePlayerHistory__(self):
            print(self._type + " has played " +
                  str(self._history["Rock"]) + " Rocks, " +
                  str(self._history["Paper"]) + " Papers, " +
                  str(self._history["Scissors"]) + " Scissors."
                  )

        def __playTurn__(self, choice=None, opponent = None):
            if self._type == "Computer":
                self.__playComputerTurn__(opponent)
            else:
                self.__playHumanTurn__(choice)


        def __playHumanTurn__(self, choice):
            self.__inputChoice__(choice)

        def __playComputerTurn__(self, opponent):
            choice = self.computerLogic(opponent)
            self.__inputChoice__(choice)

        def computerLogic(self, opponent):
            largest_value = 0
            topChoice = {}

            for choice, numChoicePlayed in opponent._history.items():
                if numChoicePlayed > largest_value:
                    # Create new topChoice dict
                    topChoice = {choice : numChoicePlayed}

                    # Update Largest Value Choice
                    largest_value = numChoicePlayed

                elif numChoicePlayed == largest_value:
                    topChoice[choice] = numChoicePlayed


            # NOTE: Can probaly take this if out and just keep else. Check later.
            if len(topChoice) == 1:
                choice = list(topChoice.keys())[0]
            else:
                choice = random.choice(list(topChoice.keys()))
            return choice

# Testing
game = rpsGame()
print("Round 1")
game.__playTurn__("Rock")
#game.__seeResults__()
#game.__seeGameHistory__()

print("Round 2")
game.__playTurn__("Rock")
#game.__seeResults__()
#game.__seeGameHistory__()

print("Round 3")
game.__playTurn__("Paper")
#game.__seeResults__()
#game.__seeGameHistory__()

print("Round 4")
game.__playTurn__("Paper")
#game.__seeResults__()
#game.__seeGameHistory__()

print("Round 5")
game.__playTurn__("Paper")
#game.__seeResults__()
#game.__seeGameHistory__()

print("Round 6")
game.__playTurn__("Scissors")
#game.__seeResults__()
#game.__seeGameHistory__()

print("Round 7")
game.__playTurn__("Scissors")
#game.__seeResults__()
#game.__seeGameHistory__()

print("Round 8")
game.__playTurn__("Scissors")
#game.__seeResults__()
#game.__seeGameHistory__()

print("Round 9")
game.__playTurn__("Scissors")
#game.__seeResults__()
#game.__seeGameHistory__()

game.__quitGame__()







# Testing
game = rpsGame()
game.__playTurn__("Rock")
game.__seeResults__()
game.__seeGameHistory__()

game.__playTurn__("Rock")
game.__seeResults__()
game.__seeGameHistory__()

game.__playTurn__("Rock")
game.__seeResults__()
game.__seeGameHistory__()

game.__playTurn__("Rock")
game.__seeResults__()
game.__seeGameHistory__()

game.__playTurn__("Rock")
game.__seeResults__()
game.__seeGameHistory__()

game.__playTurn__("Rock")
game.__seeResults__()
game.__seeGameHistory__()

game.__playTurn__("Rock")
game.__seeResults__()
game.__seeGameHistory__()

game.__playTurn__("Rock")
game.__seeResults__()
game.__seeGameHistory__()

game.__playTurn__("Rock")
game.__seeResults__()
game.__seeGameHistory__()

game.__quitGame__()





#rpsGame().__seeGameHistory__()


'''
# Create Players
player1 = Player(_type="Human")
player2 = Player(_type="Computer")


player1.__playTurn__("Rock")
player1.__seePlayerHistory__()

player2.__playTurn__("Rock")
player2.__seePlayerHistory__()
'''










