from __init__ import *
from version import __version__, __updated__


class Master:
    # --------------------------------------------- Class Initialization --------------------------------------------- #
    def __init__(self):
        self.args = sys.argv[1:]
        self.games = [
            "rubamazzetto"
        ]
        self.current = 0
        self.total = len(self.games) - 1

        if len(self.args) > 0:
            self.handle_args()

    # ----------------------------------------------- Handle Arguments ----------------------------------------------- #
    def handle_args(self):
        # --------------------------------------------- Master Arguments --------------------------------------------- #
        if self.args[0] == "--help" or self.args[0] == "--h":
            print(f"{Colors.green}█ This is the launcher for the various games")
            print(f"\n█ Args available:")
            print(f"{Colors.lb}█  --help: shows this prompt")
            print(f"{Colors.lb}█  --list: shows the games list usable as argument")
            print(f"{Colors.lb}█  --version: shows the launcher's version")
            print(f"{Colors.green}█ Run without args to use the GUI and the default settings")
            print(f"\n{Colors.green}█ To play a game with modified settings, use the following syntax:")
            print(f"{Colors.red}█  python .\\master.py --[gameName] --[gameArgs]")
            print(f"\n{Colors.yellow}█ To get the games list, use '--list' instead of --[gameName]")
            print(f"{Colors.yellow}█ To get game-specific args, use '--help' after --[gameName]")
            print(f"\n{Colors.red}█ Example usage: .\\master.py --rubamazzetto --verbose")
            exit()
        elif self.args[0] == "--list":
            print(f"{Colors.green}█ This is the games list usable as argument:")
            for game in self.games:
                print(f"{Colors.lb}█  --{game}")
            print(f"\n{Colors.red}█ Usage: python .\\master.py --[gameName] --[gameArgs]")
            print(f"{Colors.yellow}█ To get game-specific args, use '--help' after --[gameName]")
            exit()
        elif self.args[0] == "--version" or self.args[0] == "--v":
            print(f"{Colors.green}█ Version: {__version__}")
            print(f"{Colors.green}█ Updated: {__updated__}")
            exit()

        # ---------------------------------------------- Game Arguments ---------------------------------------------- #
        if self.args[0][2:] in self.games:
            self.launch_game(self.games.index(self.args[0][2:]))
        else:
            print(f"{Colors.red}█ Provided invalid argument: '{self.args[0]}'")
            print(f"{Colors.lb}█ Try using '--help' or '--list' first")
            exit()

    # ------------------------------------------------- Main Program ------------------------------------------------- #
    def main(self):
        cursor.hide()
        try:
            self.update_selection()
            while not kb.is_pressed("enter"):
                self.select_game()
            input()  # To catch the exit key 'enter'

            self.launch_game(self.current)
        except KeyboardInterrupt:
            print(f"\n{Colors.red}Exit the hard way, I guess.{Colors.reset}")

        cursor.show()

    def launch_game(self, i: int):
        if self.games[i] == "rubamazzetto":
            Rubamazzetto().main()

    # ----------------------------------- Logic for Game Selection with Arrow Keys ----------------------------------- #
    def select_game(self):
        while True:
            if kb.is_pressed("up arrow"):
                self.current -= 1
                if self.current < 0:
                    self.current = self.total
                break
            elif kb.is_pressed("down arrow"):
                self.current += 1
                if self.current == len(self.games):
                    self.current = 0
                break
            elif kb.is_pressed("enter"):
                break

        self.update_selection()
        while kb.is_pressed("up arrow") or kb.is_pressed("down arrow"):
            continue

    def update_selection(self):
        clear()
        print(master_banner)
        print(f"{' ' * round((80 - 31) / 2)}╔═════════════════════════════╗")
        print(f"{' ' * round((80 - 31) / 2)}║        SELECT A GAME        ║")
        for i in range(len(self.games)):
            game = self.games[i].capitalize()
            if i == self.current:
                print(f"{' ' * round((80 - 31) / 2)}║ > {game}{' ' * (26 - len(game))}║")
            else:
                print(f"{' ' * round((80 - 31) / 2)}║   {game}{' ' * (26 - len(game))}║")
        print(f"{' ' * round((80 - 31) / 2)}╚═════════════════════════════╝")


# ------------------------------------------------ Main Entry Point -------------------------------------------------- #
if __name__ == '__main__':
    Master = Master()  # OS Object
    Master.main()  # Run Program
