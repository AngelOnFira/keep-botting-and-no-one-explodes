# Keep Botting and No One Explodes
[![codecov](https://codecov.io/gh/AngelOnFira/keep-botting-and-no-one-explodes/branch/master/graph/badge.svg?token=HLX1iYCMof)](https://codecov.io/gh/AngelOnFira/keep-botting-and-no-one-explodes)

Kristoffer Anderson - 101009514  
Arryan Zaman - 101091460  
Nem Zutkovic - 101085982  
Aaron Ramos-Lazette - 101039899  

## Usage

This project requires Python 3.7, the easiest way to do this is probably with [Pyenv](https://github.com/pyenv/pyenv). Once it's installed, you can run `pyenv install 3.7.0` and then `pyenv global 3.7.0`.

This project uses the Poetry package manager for the Python dependencies. [Install it](https://github.com/python-poetry/poetry) and then run `poetry install` from the root folder of this project. After the dependencies are installed, you can run any Python commands in this environment as long as they are preceded by `poetry run`.

To run the tests, you'll need to run `poetry run pytest`. To run the project, you'll use `poetry run python main.py`.

## Summary

Keep Botting and No One Explodes (KBE) is a bot that can play "Keep Talking and Nobody Explodes". Keep Talking is a video game in which human players work together to defuse a bomb. The difference between the actual video game and what we are trying to accomplish is that KBE uses computer vision to analyze and manipulate the bomb by mimicking a controller, inspecting specific features, and recognizing modules. KBE will then find solutions to each puzzle and execute them without any human interaction.

![bomb](images/bomb-front.jpg)

## Background

In “Keep Talking and No One Explodes”, a single-player is the “Bomb Defuser” who interacts with and relays information about the bomb to one or more “Bomb Experts” who hold the [bomb information manual](http://www.bombmanual.com/web/index.html). The bomb information manual holds the key to solving each puzzle/module. The bomb experts, in turn, provide the bomb defuser with step-by-step instructions to progress through the various challenges of defusing the bomb. To defuse a bomb, the bomb defuser must disarm all of its modules before the countdown timer expires or before three strikes are made. Unable to do so, will cause the bomb to explode.

Computer assistance has been used before to help play the game. A bot was created that could listen to instructions that a human bomb diffuser would give. It would solve a module, and speak the solution to the bomb defuser. You can see the bot defuse the bomb with human guidance [here](https://www.youtube.com/watch?v=psiyI6jVpKI). This bot still requires human interaction to analyze the visual information from the bomb. The key difference with their project and what we are trying to do is to eliminate the human interaction and have the bot defuse the bomb.

## Challenges

Different types of challenges will have to be approached to defuse a bomb.

### Optical Character Recognition

Many of the modules and features of the bomb have some form of numbering or Unicode characters that need to be understood by the bomb defuser. For example, there is a module that uses a subset of four Extended-Unicode characters that must be mapped to a set of characters in the Defusal Manual held by the bomb expert. This module can be seen in the top right of Figure 1 (seen above).

Other modules require similar character recognition, as well as general features of the bomb such as the serial number. To solve these issues, the bomb defuser needs to be able to interpret these characters using OCR by passing in screen captures.

### Video Analysis

Some modules require a more complex solution than just screen captures. Specifically, there is a morse code module that requires the bomb defuser to be able to watch a blinking light. To interpret this light, we will require some way to analyze it over time. Likely, this will require some form of video capture. OpenCV does have the ability to process video, which will be investigated as an option. If video processing becomes too complex of an endeavor, then the video analysis will be done across many frame captures at a decent rate (e.g. 45fps).

### Feature Detection

Feature detection is where the majority of the OpenCV work will take place. We must be able to successfully classify modules to determine what module logic to use. Likewise, we need to be able to determine the features of said module and pick out information relevant to solving the logic puzzle. This is necessary because it allows the bomb defuser, which is our bot, to know where on the module it needs to interact.

## Goals and Deliverables
The Minimum Viable Product (MVP) for this project is to have KBE complete a trivial level in the game. This level will consist of the following:
* Picking up the bomb
* Identifying basic bomb features (time, battery count, etc…)
* Identifying the single module to complete
* Identifying the logic puzzle on the module
* Calculating the solution for module
* Executing the solution for module
* Level complete

The module that will be used in the MVP can be seen in the bottom right of Figure 1 (seen above). It will make use of simple OCR and does not require any other information from the bomb. This makes it a good goal to test out our system and includes a full game being played. This will be Deliverable 1.

Once this is complete, we can extend our systems to encompass more modules. This will allow any level of the game to be played. This will be Deliverable 2, and also the end goal. If we achieve this before the project is over, some other tasks that can be done that aren’t essential:

The bot will be designed to solve bombs within certain parameters. It won’t take into account the screen resolution or rotation speed of controllers. Feature detection can be used to calibrate the bot before starting a solution.
Ability to visually describe what the bot is working on. The bot will go through its logic rapidly without user input, and so it will be difficult to know what it is doing. It might be possible to create an overlay video that highlights what the bot is analyzing at any given time. This would have to be a separate system to be implemented alongside each other.

We will be able to easily record videos of the bot in progress. This can be used to see that the goal was achieved. We will have a video ready after deliverable 1 as well so that we can show the improvements at the end of the project.

This project’s scope is quite large, however, we have a strong plan to complete it. We are confident in our team’s ability to overcome obstacles, and we have a full team of four members. See the schedule below for our plan to achieve this.

## Schedule
This schedule will be used tentatively. We are doing project management within Github using Projects. From there, we can more efficiently manage tasks and a schedule. We can assign tasks to group members, and have discussions on particular issues.

| TASKS PER WEEK                                                          | DUE DATE  |
| ------------------------------------------------------------------------| ---------|
| Finalize project architecture. Separated systems need to be implemented:<br> - Feature detection<br> - Module logic<br> - Bomb interaction | FEB 1
| Tasks assigned to prepare systems for MVP:<br> - Research to mimic a game controller<br> - Basic bomb feature detection<br> - “On The Subject of Memory” | FEB 8
| Deliverable 1: Project MVP:<br> - Need to be able to solve trivial bomb | FEB 15
| Complete 3/11 Modules:<br> - “On The Subject of Passwords”<br> - “On The Subject of Who’s On First” | FEB 22
| Complete 5/11 Modules (Will require more feature detection on the bomb):<br> - “On The Subject of Complicated Wires”<br> - “On The Subject of The Button” | FEB 29
| Complete 7/11 Modules:<br> - “Simple wires” module feature detection<br> - “On The Subject of Simon Says” |  MAR 7
| Complete 9/11 Modules (Will require specific research):<br> - “On The Subject of Mazes”<br> - “On The Subject of Wire Sequences” | MAR 14
| Complete 11/11 Modules:<br> - “On The Subject of Morse Code”<br> - “On The Subject of Keypads” | MAR 21
| Deliverable 2: Game Completion<br> - The bot should be able to solve any bomb in the campaign<br> - We should be confident in the ability of any module to be solved | MAR 28<br> <em>Results date</em>
| Documentation Week:<br> - Time will be used to work on any project write-ups<br> - Work on extra project goals | APR 4
| Bonus Week:<br> - Used as buffer week if needed<br> - Work on extra project goals | APR 10<br> <em>The project must be completed.</em>
