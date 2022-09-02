# Python Packages
import cursor
import random
import sys
# Custom Packages
from .graphics import banner
from utils import *
from .version import __version__, __updated__


class Player:
    def __init__(self):
        self.name = ""
        self.deck = []
        self.pickups = 0


class Game:
    def __init__(self):
        # Arguments
        self.args = sys.argv[2:]
        self.autopilot = False
        self.verbose = False

        # Technical variables
        self.table = []
        self.valuables = ["A", "2", "3"]
        self.last_discard = ""
        self.objective = ""
        self.objective_discarded = 0

        # Statistics
        self.total_moves = 0
        self.total_pickups = 0

        # Generation of deck
        numbers = ["A", "2", "3", "4", "5", "6", "7", "F", "C", "R"]
        seeds = ["♥", "♦", "♣", "♠"]
        self.cards = []
        for seed in seeds:
            for number in numbers:
                self.cards.append(f"{number + seed}")

        # Player related variables
        self.p1 = Player()
        self.p2 = Player()
        self.playing = self.p1

        # Handle arguments
        if len(self.args) > 0:
            self.handle_args()

    # ----------------------------------------------- Handle Arguments ----------------------------------------------- #
    def handle_args(self):
        # --------------------------------------------- Master Arguments --------------------------------------------- #
        if self.args[0] == "--help" or self.args[0] == "--h":
            print(f"{Colors.green}█ Help for 'Rubamazzetto'")
            print(f"\n█ Args available:")
            print(f"{Colors.lc}█  --help: shows this prompt")
            print(f"{Colors.lc}█  --version: shows the game's version")
            print(f"{Colors.lb}█  --verbose: prints out every move")
            print(f"\n{Colors.green}█ Run without args to play with default settings")
            print(f"{Colors.green}█ To play with modified settings, use the following syntax:")
            print(f"{Colors.red}█ python .\\master.py --rubamazzetto [--args]")
            print(f"\n{Colors.red}█ Example usage: .\\master.py --rubamazzetto --verbose")
            exit()
        elif self.args[0] == "--version" or self.args[0] == "--v":
            print(f"{Colors.red}█ Version: {__version__}")
            print(f"{Colors.green}█ Updated: {__updated__}")
            exit()

        # ---------------------------------------------- Game Arguments ---------------------------------------------- #
        for arg in self.args:
            if arg == "--autopilot":
                self.autopilot = True
            elif arg == "--verbose":
                self.verbose = True
            else:
                print(f"{Colors.red}█ Provided invalid argument: '{arg}'")
                print(f"{Colors.lb}█ Try using '--help' first")
                exit()

    def main(self):
        try:
            clear()
            print(banner)
            # ------------------------------------------------ Naming ------------------------------------------------ #
            self.p1.name = self.prompt("Naming", "Insert Player1's name:", Colors.lb).capitalize()
            self.p2.name = self.prompt("Naming", "Insert Player2's name:", Colors.lb).capitalize()
            # ---------------------------------------------- Shuffling ----------------------------------------------- #
            while True:  # Choose who starts
                even_odd = self.prompt("Shuffling", f"{self.p1.name}, choose 'even' or 'odd':", Colors.green)
                if even_odd == "even" or even_odd == "e":
                    even_odd = 0
                elif even_odd == "odd" or even_odd == "o":
                    even_odd = 1
                else:
                    self.dialog("Error", "Insert a valid option!", Colors.red)
                    continue
                break
            if random.randint(0, 1) == even_odd:
                self.dialog("Console", f"It's even. {self.playing.name} won!", Colors.magenta)
            else:
                self.switch_player()
                self.dialog("Console", f"It's odd. {self.playing.name} won!", Colors.magenta)

            self.switch_player()  # The loser shuffles the cards
            if not self.autopilot:
                self.prompt("Shuffling", f"{self.playing.name}, press 'enter' to shuffle.", Colors.green)
            for i in range(random.randint(1, 4)):
                random.shuffle(self.cards)
            self.dialog("Console", f"{self.playing.name} shuffled the cards.", Colors.magenta)
            self.switch_player()
            # ----------------------------------------------- Cutting ------------------------------------------------ #
            while True:  # The winner cuts the cards
                cut = f"{self.playing.name}, choose how many cards to cut (Max 39):"
                cut = self.prompt("Cutting", cut, Colors.green)
                try:
                    if 0 <= int(cut) < 40:
                        cut = int(cut)
                        break
                except ValueError:
                    pass
                self.dialog("Error", "Insert a valid option!", Colors.red)
                continue

            for i in range(cut):
                self.cards.append(self.cards.pop(0))
            self.dialog("Console", f"{self.playing.name} cut the cards.", Colors.magenta)
            self.switch_player()
            # --------------------------------------------- Distributing --------------------------------------------- #
            if not self.autopilot:
                self.prompt("Distributing", f"{self.playing.name}, press 'enter' to distribute.", Colors.green)
            for card in self.cards:  # The loser distributes the cards
                self.switch_player()
                self.playing.deck.append(card)
            self.dialog("Console", f"{self.playing.name} distributed the cards.", Colors.magenta)
            self.switch_player()
            # ------------------------------------------------ Match ------------------------------------------------- #
            self.prompt("Console", f"The match is ready! Press 'enter' to start.", Colors.magenta, nl=True)
            while len(self.p1.deck) > 0 and len(self.p2.deck) > 0:  # Until a player has no cards left
                if not self.autopilot:
                    self.prompt("Playing", f"{self.playing.name}, press 'enter' to discard.", Colors.yellow)
                self.discard()  # The current player discards a card
                if self.last_discard in self.valuables:  # If he responds with a valuable:
                    self.switch_player()  # Switch player,
                    self.objective = self.last_discard  # Set the new objective and continue
                elif self.objective == "":  # If he responds with a non-valuable and there is no objective:
                    self.switch_player()  # Just switch player
                else:  # If he responds with a non-valuable but there is an objective:
                    self.check_objective()  # Check the game's logic
            # -------------------------------------------- Ending Screen --------------------------------------------- #
            if len(self.table) > 0:
                self.switch_player()
                self.take_table()
            self.dialog("Console", f"{self.playing.name} wins.", Colors.magenta)
            # TODO: Cool finish screen
        except KeyboardInterrupt:
            print(f"\n\n{Colors.red}Exit the hard way, I guess.{Colors.reset}")

        cursor.show()
        exit()

    # -------------------------------------------------- Functions --------------------------------------------------- #
    def check_objective(self):  # The game's logic
        self.objective_discarded += 1  # Keeps track of the amount of cards discarded
        if self.objective == "A":
            if self.last_discard not in self.valuables:  # If the discarded card is not valuable
                self.take_table()  # The opponent takes the table
            else:
                self.change_objective()  # Otherwise we change the objective and continue discarding
        elif self.objective == "2":
            if self.last_discard not in self.valuables:  # If the discarded card is not valuable
                if self.objective_discarded == 2:  # And it's the last opportunity to respond
                    self.take_table()  # The opponent takes the table
                # Otherwise the current player tries to respond again
            else:
                self.change_objective()  # Otherwise we change the objective and continue discarding
        elif self.objective == "3":
            if self.last_discard not in self.valuables:  # If the discarded card is not valuable
                if self.objective_discarded == 3:  # And it's the last opportunity to respond
                    self.take_table()  # The opponent takes the table
                # Otherwise the current player tries to respond again
            else:
                self.change_objective()  # Otherwise we change the objective and continue discarding

    def change_objective(self):
        self.objective = self.last_discard
        self.objective_discarded = 0
        self.switch_player()

    def reset_objective(self):
        self.objective = ""
        self.objective_discarded = 0

    def discard(self):
        self.total_pickups += 1  # For ending screen statistics
        self.last_discard = self.playing.deck.pop(0)
        self.table.append(self.last_discard)
        if self.verbose:
            self.dialog("Console", f"{self.playing.name} discarded '{self.last_discard}'.", Colors.magenta)
        self.last_discard = self.last_discard[0]  # Since we don't care about the seed, we only consider the value

    def switch_player(self):
        if self.playing == self.p1:
            self.playing = self.p2
        else:
            self.playing = self.p1

    # TODO: Cool bar indicating decks len
    def take_table(self):
        self.reset_objective()
        self.switch_player()
        self.playing.pickups += 1
        self.dialog("Console", f"{self.playing.name} picked up {len(self.table)} cards.", Colors.lb)
        self.playing.deck.extend(self.table)
        self.table = []

    @staticmethod
    def dialog(action: str,
               text: str,
               color_b: str = Colors.white,
               color_a: str = Colors.white,
               nl: bool = False,
               called: bool = False) -> str:

        if nl:
            print()
        if not called:
            print(f"{color_b}█ {Colors.white}[{color_b + action + Colors.white}]{color_b} {text}{color_a} ")
        else:
            return f"{color_b}█ {Colors.white}[{color_b + action + Colors.white}]{color_b} {text}{color_a} "

    def prompt(self,
               action: str,
               text: str,
               color_before: str = Colors.white,
               color_after: str = Colors.white,
               nl: bool = False) -> str:

        return input(self.dialog(action, text, color_before, color_after, nl, True)).lower()
