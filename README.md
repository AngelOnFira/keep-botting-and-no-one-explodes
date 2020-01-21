# Keep Botting and No One Explodes

Kristoffer Anderson

![bomb](images/bomb-front.jpg)

## Usage

This project requires Python 3.7, the easiest way to do this is probably with [Pyenv](https://github.com/pyenv/pyenv). Once it's installed, you can run `pyenv install 3.7.0` and then `pyenv global 3.7.0`.

This project uses the Poetry package manager for the Python dependencies. [Install it](https://github.com/python-poetry/poetry) and then run `poetry install` from the root folder of this project. After the deps are installed, you can run any Python commands in this env as long as they are preceded by `poetry run`.

To run the tests, you'll need to run `poetry run pytest`. To run the project, you'll use `poetry run python main.py`.

## Summary

Keep Botting and No One Explodes (KBE) is a bot that is able to play the video game "Keep Talking and No One Explodes", in which players work together to defuse a bomb. KBE uses computer vision to manipulate and analyze the bomb by calibrating movement, inspecting specific features, and recognizing modules. The bot will then find solutions to each puzzle and execute them.

## Background

In Keep Talking and No One Explodes, a single player is a bomb defuser and relays information about the bomb to the rest of the player. Each other player works through instructions on how do solve certain modules on the bomb. They relay this solution back to the bomb defuser, who executes it on the bomb.

Computer assistance has been used before to help play the game. A bot was created that could listen to instructions that a human bomb defuser would give. It would solve a module, and speak the solution to the defuser. You can see this bot [here](https://www.youtube.com/watch?v=psiyI6jVpKI). This bot still requires human interaction to analyze the visual representation of the bomb.

## The Challenge

There are different types of challenges that will have to be approached to defuse a bomb.

### Optical Character Recognition

### Video Analysis

### Feature Detection
