import random


class rpsGame:
    def __init__(self):
        self._humanPlayer = self.Player(_type="Human")
        self._computerPlayer = self.Player(_type="Computer")

        # Set Possible Options
        self._choice_options = ["Rock", "Paper", "Sicors"]

    def __playTurn__(self, choice):
        if choice in self._choice_options:
            self._humanPlayer.__playTurn__(choice)
            self._computerPlayer.__playTurn__(opponent = self._humanPlayer)

    def __seeGameHistory__(self):
        self._humanPlayer.__seePlayerHistory__()
        self._computerPlayer.__seePlayerHistory__()

    class Player:
        def __init__(self, _type):
            # Set Possible Options
            self._player_options = ("Human", "Computer")

            # Set Possible Options
            self._choice_options = ["Rock", "Paper", "Sicors"]

            if _type in self._player_options:
                self._type = _type
            else:
                print("Pick Valid Player Option: Human or Computer")

            self._history = {"Rock": 0,
                             "Paper": 0,
                             "Sicors": 0}

        def __inputChoice__(self, choice):
            # if self._type == "Computer":
            #     print("You cannot play for the computer.")
            # else:
            if choice in self._choice_options:
                #if self._type == "Computer"
                self._history[choice] += 1
            else:
                print("Pick Valid Choice: Rock, Paper, or Scissors")

        def __seePlayerHistory__(self):
            print(self._type + " has played " +
                  str(self._history["Rock"]) + " Rocks, " +
                  str(self._history["Paper"]) + " Papers, " +
                  str(self._history["Sicors"]) + " Sicors, "
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
game.__playTurn__("Rock")
game.__seeGameHistory__()
game.__playTurn__("Rock")
game.__seeGameHistory__()
game.__playTurn__("Paper")
game.__seeGameHistory__()
game.__playTurn__("Paper")
game.__seeGameHistory__()
game.__playTurn__("Paper")
game.__seeGameHistory__()
game.__playTurn__("Sicors")
game.__seeGameHistory__()
game.__playTurn__("Sicors")
game.__seeGameHistory__()
game.__playTurn__("Sicors")
game.__seeGameHistory__()
game.__playTurn__("Sicors")
game.__seeGameHistory__()




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










