# Python Packages
import cursor
import random
import sys
# Custom Packages
from .graphics import banner
from utils import *
from .version import __version__, __updated__


class Rubamazzetto:
    def __init__(self):
        # Arguments
        self.args = sys.argv[2:]
        self.verbose = False

        # Technical variables
        # TODO: Remove in case

        # Generation of deck
        numbers = ["1", "2", "3", "4", "5", "6", "7", "F", "C", "R"]
        seeds = ["♥", "♦", "♣", "♠"]
        self.cards = []
        for seed in seeds:
            for number in numbers:
                self.cards.append(f"{number + seed}")
        self.table = []

        # Player related variables
        self.p1 = Player()
        self.p2 = Player()
        self.winner = ""
        self.loser = ""

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
            if arg == "--verbose":
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
            while True:
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
                self.set_winner(self.p1.name)
                self.dialog("Console", f"It's even! {self.winner} won!", Colors.magenta)
            else:
                self.set_winner(self.p2.name)
                self.dialog("Console", f"It's odd! {self.winner} won!", Colors.magenta)

            self.prompt("Shuffling", f"{self.loser}, press 'enter' to shuffle.", Colors.green)
            for i in range(random.randint(1, 4)):
                random.shuffle(self.cards)
            self.dialog("Console", f"Cards have been shuffled.", Colors.magenta)

            # ----------------------------------------------- Cutting ------------------------------------------------ #
            while True:
                cut = self.prompt("Cutting", f"{self.winner}, choose how many cards to cut (Max 39)", Colors.green)
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
            self.dialog("Console", f"Cards have been cut.", Colors.magenta)

            # --------------------------------------------- Distributing --------------------------------------------- #
            self.prompt("Distributing", f"{self.loser}, press 'enter' to distribute.", Colors.green)
        except KeyboardInterrupt:
            print(f"\n\n{Colors.red}Exit the hard way, I guess.{Colors.reset}")

        cursor.show()
        exit()

    def set_winner(self, player: str):
        self.winner = player
        if player == self.p1.name:
            self.loser = self.p2.name
        else:
            self.loser = self.p1.name

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


class Player:
    def __init__(self):
        self.name = ""
        self.deck = []
