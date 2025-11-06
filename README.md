# 5AI Chess Project
A basic framework built around python-chess.

use the python-chess library which implements the chess logic. We have provided you with a framework that abstracts away some of the quirky details of this library and implements the Universal Chess Interface (UCI), an open communication protocol that enables chess engines to communicate with user interfaces. There are a few steps to take to run the code for this lab on your machine.

## Getting started

Install the framework for the chess project we provided with the following commands:

```bash
cd chess_project
pip install -e .
```

This will automatically install the python-chess library, which can also be installed separately with:

```bash
pip install python-chess
```

## Documentation

The framework contains a basic class structure for utilities, agents and engines (can be used in combination with a GUI).

### Agents
Agents contain the logic to search through the game tree (this is where you would place a minimax). Agents use a Utility to give values to positions, these values are then used to select the best action according to your search tree.

### Utilities
Utilities contain the logic to give a value to a state of the game (heuristics). This value determines how advantageous a position is for either side. This value can be calculated very naively (number of black pieces vs number of white pieces) or more advanced (taking into account things like position, state of game, importance of pieces, etc.).

### Engines
The uci_engine.py script handles all the background stuff to allow you to interact with a GUI. You probably never have to touch this file. The example_engine.py script shows how you can use this script to actually interact with a GUI. This script also shows how you should use the Agent and Utility classes.

## Examples
This folder contains three example scripts to show you how you can use (or train) your agent.
The scripts show how to play against yourself, how to play against stockfish and how to read from pgn files.
To play against stockfish, remember to install it from https://stockfishchess.org/ and reference the path where you installed it correctly.
