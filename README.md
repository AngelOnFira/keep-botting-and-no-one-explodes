# Keep Botting and No One Explodes

Kristoffer Anderson - 101009514
Arryan Zaman - 101091460
Nem Zutkovic - 101085982
Aaron Ramos-Lazette - 101039899

![bomb](images/bomb-front.jpg)

## Usage

This project requires Python 3.7, the easiest way to do this is probably with [Pyenv](https://github.com/pyenv/pyenv). Once it's installed, you can run `pyenv install 3.7.0` and then `pyenv global 3.7.0`.

This project uses the Poetry package manager for the Python dependencies. [Install it](https://github.com/python-poetry/poetry) and then run `poetry install` from the root folder of this project. After the deps are installed, you can run any Python commands in this env as long as they are preceded by `poetry run`.

To run the tests, you'll need to run `poetry run pytest`. To run the project, you'll use `poetry run python main.py`.

## Summary

Keep Botting and No One Explodes (KBE) is a bot that can play "Keep Talking and Nobody Explodes". Keep Talking is a video game in which human players work together to defuse a bomb. The difference between the actual video game and what we are trying to accomplish is that KBE uses computer vision to analyze and manipulate the bomb by mimicking a controller, inspecting specific features, and recognizing modules. KBE will then find solutions to each puzzle and execute them without any human interaction.

## Background

In “Keep Talking and No One Explodes”, a single player is the “Bomb Defuser” who interacts with and relays information about the bomb to one or more “Bomb Experts” who hold the [bomb defusal manual](http://www.bombmanual.com/web/index.html). The bomb defusal manual holds the key to solving each puzzle/module. The bomb experts, in turn, provide the bomb defuser with step-by-step instructions to progress through the various challenges of defusing the bomb. To defuse a bomb, the bomb defuser must disarm all of its modules before the countdown timer expires or before three strikes (bomb defusal failures) are made.

Computer assistance has been used before to help play the game. A bot was created that could listen to instructions that a human bomb diffuser would give. It would solve a module, and speak the solution to the bomb defuser. You can see the bot defuse the bomb with human guidance [here](https://www.youtube.com/watch?v=psiyI6jVpKI). This bot still requires human interaction to analyze the visual information from the bomb. The key difference with their project and what we are trying to do is to eliminate the human interaction completely and have the bot defuse the bomb.


## The Challenge

There are different types of challenges that will have to be approached to defuse a bomb.

### Optical Character Recognition

Many of the modules and features of the bomb have some form of numbering or Unicode characters that need to be understood by the bomb defuser. For example, there is a module that uses a subset of four Extended-Unicode characters that must be mapped to a set of characters in the Defusal Manual held by the bomb expert. This module can be seen in the top right of Figure 1 (seen above).

Other modules require similar character recognition, as well as general features of the bomb such as the serial number. To solve these issues, the bomb defuser needs to be able to interpret these characters using OCR by passing in screen captures.

### Video Analysis

Some modules require a more complex solution than just screen captures. Specifically, there is a morse code module that requires the bomb defuser to be able to watch a blinking light. To interpret this light, we will require some way to analyze it over time. Likely, this will require some form of video capture. OpenCV does have the ability to process video, which will be investigated as an option. If video processing becomes too complex of an endeavor, then the video analysis will be done across many frame captures at a decent rate (e.g. 45fps).

### Feature Detection

Feature detection is where the majority of the OpenCV work will take place. We must be able to successfully classify modules to determine what module logic to use. Likewise, we need to be able to determine the features of said module and pick out information relevant to solving the logic puzzle. This is necessary because it allows the bomb defuser, which is our bot, to know where on the module it needs to interact.