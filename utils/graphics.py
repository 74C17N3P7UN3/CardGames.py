# Python Packages
from colorama import init, Style, Fore

# Initialize colorama ANSI filter for Win32
init()


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


bars = "▁▂▃▄▅▆▇█"
master_banner = f"""{Colors.lc}
   ██████╗ █████╗ ██████╗ ██████╗    ██████╗  █████╗ ███╗   ███╗███████╗███████╗
  ██╔════╝██╔══██╗██╔══██╗██╔══██╗  ██╔════╝ ██╔══██╗████╗ ████║██╔════╝██╔════╝ {Colors.lb}
  ██║     ███████║██████╔╝██║  ██║  ██║  ███╗███████║██╔████╔██║█████╗  ███████╗
  ██║     ██╔══██║██╔══██╗██║  ██║  ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ╚════██║ {Colors.blue}
  ╚██████╗██║  ██║██║  ██║██████╔╝  ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗███████║
   ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝ {Colors.reset}
                                                                                 """
