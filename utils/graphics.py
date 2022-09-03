# Python Packages
from colorama import init, Style, Fore

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


# bars = "▁▂▃▄▅▆▇█"
master_banner = f"""{Colors.lc}
   ██████╗ █████╗ ██████╗ ██████╗    ██████╗  █████╗ ███╗   ███╗███████╗███████╗
  ██╔════╝██╔══██╗██╔══██╗██╔══██╗  ██╔════╝ ██╔══██╗████╗ ████║██╔════╝██╔════╝ {Colors.lb}
  ██║     ███████║██████╔╝██║  ██║  ██║  ███╗███████║██╔████╔██║█████╗  ███████╗
  ██║     ██╔══██║██╔══██╗██║  ██║  ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ╚════██║ {Colors.blue}
  ╚██████╗██║  ██║██║  ██║██████╔╝  ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗███████║
   ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝ {Colors.reset}
"""
