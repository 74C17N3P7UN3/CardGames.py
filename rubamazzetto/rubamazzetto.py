# ------------------------------------------- CardGames.py/rubamazzetto.py ------------------------------------------- #
__version__ = "v1.0.0"
__updated__ = "03/09/2022"

# Python Packages
from colorama import init, Style, Fore
import cursor
import math
import random
import sys


# ------------------------------------------- Custom Packages -> Functions ------------------------------------------- #
def clear():
    print("\033[2J", end="")


# If regex is not working correctly
# for you, uncomment the code below
"""
def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")
"""

init()  # Initialize colorama ANSI filter for Win32

color_list = [
    Fore.MAGENTA,
    Fore.RED,
    Fore.YELLOW,
    Fore.GREEN,
    Fore.CYAN,
    Fore.BLUE
]


class Colors:
    black = Fore.BLACK
    blue = Fore.BLUE
    cyan = Fore.CYAN
    green = Fore.GREEN
    lb = Fore.LIGHTBLUE_EX
    lc = Fore.LIGHTCYAN_EX
    magenta = Fore.MAGENTA
    red = Fore.RED
    white = Fore.WHITE
    yellow = Fore.YELLOW

    reset = Style.RESET_ALL


class Cursor:
    save = "\033[s"
    reset = "\033[u"


banner = f"""{Colors.lc}
  ██████╗ ██╗   ██╗██████╗  █████╗ ███╗   ███╗ █████╗ ███████╗███████╗███████╗████████╗████████╗ ██████╗ 
  ██╔══██╗██║   ██║██╔══██╗██╔══██╗████╗ ████║██╔══██╗╚══███╔╝╚══███╔╝██╔════╝╚══██╔══╝╚══██╔══╝██╔═══██╗ {Colors.lb}
  ██████╔╝██║   ██║██████╔╝███████║██╔████╔██║███████║  ███╔╝   ███╔╝ █████╗     ██║      ██║   ██║   ██║
  ██╔══██╗██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║██╔══██║ ███╔╝   ███╔╝  ██╔══╝     ██║      ██║   ██║   ██║ {Colors.blue}
  ██║  ██║╚██████╔╝██████╔╝██║  ██║██║ ╚═╝ ██║██║  ██║███████╗███████╗███████╗   ██║      ██║   ╚██████╔╝
  ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝      ╚═╝    ╚═════╝  {Colors.reset}
"""


# --------------------------------------------------- Player Class --------------------------------------------------- #
class Player:
    def __init__(self):
        self.name = ""
        self.deck = []
        self.pickups = 0


# ---------------------------------------------------- Main Class ---------------------------------------------------- #
class Game:
    def __init__(self):
        # Arguments
        self.args = sys.argv[1:]
        self.autopilot = False
        self.verbose = True

        # Technical variables
        self.table = []
        self.table_cards = 0
        self.valuables = ["A", "2", "3"]
        self.last_discard = ""
        self.objective = ""
        self.objective_discarded = 0

        # Statistics
        self.total_discards = 0
        self.total_pickups = 0

        # Deck generation
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
            print(f"{Colors.lb}█  --autopilot: the game discards for you (sick.)")
            print(f"{Colors.lb}█  --no-verbose: removes the printing of every move")
            print(f"\n{Colors.green}█ Run without args to play with default settings")
            print(f"{Colors.green}█ To play with modified settings, use the following syntax:")
            print(f"{Colors.red}█ python .\\rubamazzetto.py [--args]")
            print(f"\n{Colors.red}█ Example usage: .\\rubamazzetto.py --autopilot")
            exit()
        elif self.args[0] == "--version" or self.args[0] == "--v":
            print(f"{Colors.green}█ Version: {__version__}")
            print(f"{Colors.green}█ Updated: {__updated__}")
            exit()

        # ---------------------------------------------- Game Arguments ---------------------------------------------- #
        for arg in self.args:
            if arg == "--autopilot":
                self.autopilot = True
            elif arg == "--no-verbose":
                self.verbose = False
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
            if self.autopilot:
                even_odd = random.randint(0, 1)
                if even_odd == 0:
                    self.dialog("Shuffling", f"{self.playing.name} chose 'even'.", Colors.green)
                else:
                    self.dialog("Shuffling", f"{self.playing.name} chose 'odd'.", Colors.green)
            else:
                while True:  # Choose who starts
                    even_odd = self.prompt("Shuffling", f"{self.playing.name}, choose 'even' or 'odd':", Colors.green)
                    if even_odd == "even" or even_odd == "e":
                        even_odd = 0
                    elif even_odd == "odd" or even_odd == "o":
                        even_odd = 1
                    else:
                        self.dialog("Error", "Insert a valid option!", Colors.red)
                        continue
                    break
            if random.randint(0, 1) == 0:
                if even_odd == 1:
                    self.switch_player()
                self.dialog("Console", f"It's even. {self.playing.name} won!", Colors.magenta)
            else:
                if even_odd == 0:
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
            if self.autopilot:
                cut = random.randint(0, 39)
                self.dialog("Cutting", f"{self.playing.name} cut {cut} cards.", Colors.green)
            else:
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
                    self.change_objective()  # Set the new objective and continue
                elif self.objective == "":  # If he responds with a non-valuable and there is no objective:
                    self.switch_player()  # Just switch player
                else:  # If he responds with a non-valuable but there is an objective:
                    self.check_objective()  # Check the game's logic
            # -------------------------------------------- Ending Screen --------------------------------------------- #
            if len(self.table) > 0:
                if len(self.playing.deck) != 0:
                    self.switch_player()
                self.take_table()

            self.dialog("Console", f"Game Over!", Colors.lb, nl=True)
            self.dialog("Stats", f"Total discards: {self.total_discards}", Colors.yellow)
            self.dialog("Stats", f"Total pickups: {self.total_pickups}", Colors.yellow)
            self.dialog("Stats", f"{self.p1.name}'s pickups: {self.p1.pickups}", Colors.yellow)
            self.dialog("Stats", f"{self.p2.name}'s pickups: {self.p2.pickups}", Colors.yellow)

            self.print_winner()
            self.prompt("Exit", f"Press 'enter' to exit.", Colors.red)
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
        self.reset_objective()
        self.objective = self.last_discard

    def reset_objective(self):
        self.objective = ""
        self.objective_discarded = 0
        self.switch_player()

    def discard(self):
        self.total_discards += 1  # For ending screen statistics
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

    def take_table(self):
        self.reset_objective()
        self.total_pickups += 1  # For ending screen statistics
        self.playing.pickups += 1  # For ending screen statistics
        self.table_cards = len(self.table)
        self.playing.deck.extend(self.table)
        self.table = []
        cards_status = f"{self.calc_bars_spacing()}[{Colors.green}" \
                       f"{'|' * math.floor(len(self.p1.deck) / 2)}" \
                       f"{Colors.red}" \
                       f"{'|' * math.ceil(len(self.p2.deck) / 2)}" \
                       f"{Colors.lb}] " \
                       f"{len(self.p1.deck)}/{len(self.p2.deck)}"
        self.dialog("Console", f"{self.playing.name} picked up {self.table_cards} cards. {cards_status}", Colors.lb)

    # --------------------------------------------- Printing Functions ----------------------------------------------- #
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

    def calc_bars_spacing(self) -> str:
        longer = self.p1
        if len(self.p2.name) > len(self.p1.name):
            longer = self.p2

        difference = abs(len(self.p1.name) - len(self.p2.name))

        if self.playing == longer:
            if self.table_cards > 9:
                return ""
            return " "
        else:
            if self.table_cards > 9:
                return f"{' ' * difference}"
            return f" {' ' * difference}"

    def print_winner(self):
        text = f"\n{Colors.lb}█ {Colors.white}["
        to_colored_text = "Winner"
        for i in range(len(to_colored_text)):
            text += f"{color_list[i % len(color_list)]}{to_colored_text[i]}"
        text += f"{Colors.white}] "
        to_colored_text = self.playing.name + " takes the crown!"
        for i in range(len(to_colored_text)):
            text += f"{color_list[i % len(color_list)]}{to_colored_text[i]}"

        print(text)


# ----------------------------------------- Standalone Version Entry Point ------------------------------------------- #
if __name__ == '__main__':
    Game = Game()  # Game Object
    Game.main()  # Run Game
