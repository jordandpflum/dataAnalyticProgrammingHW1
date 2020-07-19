import random

class rpsGame:
    """
    Class object Rock Paper Scissors Game.
    """
    def __init__(self):
        """
        Initialize rpsGame
            Set players, (Human and Computer)
            Set Choice Options (Rock, Paper, Scissors)
            Set games played and results
        """
        self._humanPlayer = self.Player(_type="Human")
        self._computerPlayer = self.Player(_type="Computer")

        # Set Possible Options
        self._choice_options = ["Rock", "Paper", "Scissors"]

        # Initialize Number of Games Played
        self._gamesPlayed = 0

        # Initialize Results of game (Human perspective)
        self._results = (0, 0, 0)

    def __rules__(self, player1_choice, player2_choice):
        """Set rules of game
            ie, Rock beats Scissors
                Scissors beats Paper
                Paper beats Rock

        Parameters
        ----------
        player1_choice = str, representing choice of player1
        player2_choice = str, representing choice of player2

        Returns
        -------
        winner :  str, representing result of game. If "Player 1", then
                  player1 won, "Player 2" - player2 won, "Tie" both players tie
        """
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
        """Evaluate game between computer and human
            - Update results for each player
            - Report round outcome to user
        """
        # Obtain Result of Round (dictated by __rules__)
        result = self.__rules__(player1_choice = self._humanPlayer._latestChoice, player2_choice = self._computerPlayer._latestChoice)

        # Interpret Outcome of Round in terms of computer and human
        if result == "Player 1":
            # Update Results for Computer and Human
            self._humanPlayer._results[0] += 1
            self._computerPlayer._results[1] += 1

            # Report Round Outcome to User
            print("Congratulations, you won this round!")

        elif result == "Player 2":
            # Update Results for Computer and Human
            self._humanPlayer._results[1] += 1
            self._computerPlayer._results[0] += 1

            # Report Round Outcome to User
            print("Sorry, the Computer won this round. Try Again!")

        else:
            # Update Results for Computer and Human
            self._humanPlayer._results[2] += 1
            self._computerPlayer._results[2] += 1

            # Report Round Outcome to User
            print("This round's a Tie!")

    def __quitGame__(self):
        """Quit rps Game
            - Report Human Score to User
        """
        print("You have chosen to quit the game.")
        self._humanPlayer.__seePlayerScore__()

    def __playTurn__(self, choice):
        """
        Play Turn of Round

        Parameters
        ----------
        choice = str, representing choice of player
        """
        # Ensure selected choice is an accepted option
        if choice in self._choice_options:
            # Play Computer Turn and report result
            self._computerPlayer.__playTurn__(opponent=self._humanPlayer)

            # Play Human Turn
            self._humanPlayer.__playTurn__(choice)

            # Report to User what computer played
            print("Computer Played: " + str(self._computerPlayer._latestChoice))

            # Evaluate Game
            self.__evaluateGame__()

            # Update Results of Game (Human Perspective)
            self._results = self._humanPlayer._results

            # Update Total rounds played of RPS
            self._gamesPlayed += 1
        else:
            # If not a valid choice, inform user
            print("Pick Valid Choice: Rock, Paper, or Scissors")

    def __seeResults__(self):
        """
        See Results of Round (Human Perspective)
        """
        self._humanPlayer.__seePlayerResults__()

    def __showScore__(self):
        """
        Show Score of Total Game (Human Perspective)
        """
        self._humanPlayer.__seePlayerScore__()

    def __seeGameHistory__(self):
        """
        Show Game History (What Human/Computer has played in the past)
        """
        self._computerPlayer.__seePlayerHistory__()
        self._humanPlayer.__seePlayerHistory__()

    class Player:
        """
        InnerClass object (player) of rpsGame.
        """
        def __init__(self, _type):
            """
            Initialize rpsGame
                Set player options, (Human and Computer)
                Set Choice Options (Rock, Paper, Scissors)
                Initialize class varaibles
            """
            # Set Possible Options
            self._player_options = ("Human", "Computer")

            # Set Possible Options
            self._choice_options = ["Rock", "Paper", "Scissors"]

            # Ensure type is correct
            if _type in self._player_options:
                self._type = _type
            else:
                print("Pick Valid Player Option: Human or Computer")

            # Initialize History of Player
            self._history = {"Rock": 0,
                             "Paper": 0,
                             "Scissors": 0}

            # Initialize Results of Player (W,L,T)
            self._results = [0, 0, 0]

            # Initialize Games Played of Player
            self._gamesPlayed = 0

            # Initialize Player's latest Choice
            self._latestChoice = None

        def __inputChoice__(self, choice):
            """
            Input Choice of Player

            Parameters
            ----------
            choice = str, representing choice of player
            """
            if choice in self._choice_options:
                self._history[choice] += 1
                self._latestChoice = choice
                self._gamesPlayed += 1
            else:
                print("Pick Valid Choice: Rock, Paper, or Scissors")

        def __seePlayerResults__(self):
            """
            Show choice of current round for player
            """
            print(self._type + " has chosen " + str(self._latestChoice))

        def __seePlayerScore__(self):
            """
            Show total score of player
            """
            print(self._type + " has played " + str(self._gamesPlayed) + " games. Their record is: " +
                  str(self._results[0]) + " Wins, " +
                  str(self._results[1]) + " Losses, " +
                  str(self._results[2]) + " Ties."
                  )

        def __seePlayerHistory__(self):
            """
            Show total history of choices of player
            """
            print(self._type + " has played " +
                  str(self._history["Rock"]) + " Rocks, " +
                  str(self._history["Paper"]) + " Papers, " +
                  str(self._history["Scissors"]) + " Scissors."
                  )

        def __playTurn__(self, choice=None, opponent=None):
            """
            Play Turn of Player

            Parameters
            ----------
            choice = str, representing choice of player
            opponent = dictionary of opponents (human) history of choices
            """
            if self._type == "Computer":
                self.__playComputerTurn__(opponent)
            else:
                self.__playHumanTurn__(choice)


        def __playHumanTurn__(self, choice):
            """
            Play Turn of Human Player

            Parameters
            ----------
            choice = str, representing choice of player
            """
            self.__inputChoice__(choice)

        def __playComputerTurn__(self, opponent):
            """
            Play Turn of Computer Player according to computer logic and
            humans previous play history

            Parameters
            ----------
            opponent = dictionary of opponents (human) history of choices
            """
            choice = self.computerLogic(opponent)
            self.__inputChoice__(choice)

        def computerLogic(self, opponent):
            """
            Computer Logic of Choice given opponent history of choices

            Parameters
            ----------
            opponent = dictionary of opponents (human) history of choices

            Returns
            -------
            choice :  str, representing choice of computer given his logic and
                      opponents history of choices
            """
            # Initialize Largest Value of most played choice
            largest_value = 0

            # Initialize Top Choices to choose from dictionary for computer
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










