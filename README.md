<img align="right" height=200px src="assets/readme/logo.png">

# CardGames.py

<div>

![GitHub Release (Latest)](https://img.shields.io/github/v/release/74C17N3P7UN3/CardGames.py?label=Latest)
![GitHub All Downloads](https://img.shields.io/github/downloads/74C17N3P7UN3/CardGames.py/total?color=blue&label=Downloads)
![GitHub Issues](https://img.shields.io/github/issues/74C17N3P7UN3/CardGames.py?label=Issues)

![GitHub License](https://img.shields.io/github/license/74C17N3P7UN3/CardGames.py?color=blue&label=License)
![GitHub Size](https://img.shields.io/github/repo-size/74C17N3P7UN3/CardGames.py?label=Repo%20Size)
![Lines of Code](https://img.shields.io/tokei/lines/github/74C17N3P7UN3/CardGames.py?label=Total%20Lines)

</div>

A compilation of card games in python.

## đ Table of Contents

- [đ§ī¸ About](#-about)
- [đī¸ Getting Started](#-getting-started)
  - [Getting the game](#getting-the-game)
  - [Requirements](#requirements)
- [đšī¸ Running](#-running)
  - [With the GUI](#with-the-gui)
  - [With terminal args](#from-the-terminal)
  - [Standalone games](#standalone-games)
- [đ¨ī¸ Bug Fixing](#-bug-fixing)
- [â Authors](#-authors)


> [đī¸ Docs](/README.md)\
> [đī¸ī¸ī¸ī¸ī¸ī¸ī¸ī¸ī¸ Licence](/LICENSE)

## đ§ About

I started working on this project for fun, and I ended up with leaning how to use GitHub.\
This is a collection of some italian card games I enjoy and that I hope you will too.

## đ Getting Started

These instructions will get you a copy of the project up and running on your computer.

### Getting the game

You have two main methods of getting the full game.

> **Method 1: GitHub release**
>
> Go to the [latest release](https://github.com/74C17N3P7UN3/CardGames.py/releases) and download the .zip archive.\
> Extract it in an empty folder of your choice.

> **Method 2: Clone the repo with Git**
>
> Create an empty folder of your choice.\
> Open the terminal in that directory and paste this command:
>
> ```commandline
> git clone https://github.com/74C17N3P7UN3/CardGames.py
> ```

### Requirements

You can install the required packages with pip.\
In the main folder, open the terminal and paste this command:

```commandline
pip install -r requirements.txt
```

## đšī¸ Running

The full game can be played with the GUI or directly from the terminal.\
In alternative, you can download the standalone version of the desired game.

### With the GUI

To play the games from the GUI, and therefore with the default settings, just double-click [master.py](/master.py).\
This will open a default python terminal. But if you wish to play it in your terminal, just use this command:

```commandline
python .\master.py
```

### From the terminal

If you wish to play with modified games settings, you can do it by running [master.py](/master.py) from the terminal.\
You can find all the documentation in-game by running this command:

```commandline
python .\master.py --help
```

### Standalone games

If you don't want to download the full game, you can download the standalone version of the game you're interested in.
To do so, navigate to the game's folder and download the file named after the game's name.

> #### Example: download 'Rubamazzetto'
> 1. Navigate to the game's folder: [rubamazzetto](https://github.com/74C17N3P7UN3/CardGames.py/tree/main/rubamazzetto)
> 2. Download the file named after the game's
     name: [rubamazzetto.py](https://github.com/74C17N3P7UN3/CardGames.py/blob/main/rubamazzetto/rubamazzetto.py)
>
> ![Example file](/assets/readme/rubamazzetto.png)

After you've downloaded the standalone game, you can both use it with the GUI or from the terminal.\
You can always find the game's documentation by running the `--help` command.
Just remember to change the name of the file with the correct one:

```commandline
python .\rubamazzetto.py --help
```

## đ¨ Bug Fixing

Here are some quick fixes to the known bugs.

### Regex doesn't work

Most of the games use regex to clear the terminal.
If your terminal is not clearing for some reason, just open [clear.py](/utils/clear.py) and follow the instructions.

> Your code should look like this:
>
> ![Example file](/assets/readme/clear.png)
>
> This basically overrides the clear function to use the system 'clear' command.

> **Note**: The same applies to standalone games. Just change the clear function in the file.

## â Authors

- [@74C17N3P7UN3](https://github.com/74C17N3P7UN3) - All the code (For now)
