# Keep Botting and No One Explodes

This project requires Python 3.7, the easiest way to do this is probably with [Pyenv](https://github.com/pyenv/pyenv). Once it's installed, you can run `pyenv install 3.7.0` and then `pyenv global 3.7.0`.

This project uses the Poetry package manager for the Python dependencies. [Install it](https://github.com/python-poetry/poetry) and then run `poetry install` from the root folder of this project. After the deps are installed, you can run any Python commands in this env as long as they are preceded by `poetry run`.

To run the tests, you'll need to run `poetry run pytest`. To run the project, you'll use `poetry run python main.py`.
