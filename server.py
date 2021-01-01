from flask import Flask
from random import randint

app = Flask(__name__)

random_number = randint(0,9)


@app.route('/')
def home():
    """
    Renders the root page for the site.  Asks the user to guess a number.
    """
    return '<h1>Guess a number between 0 and 9</h1>' \
    '<img src="https://media0.giphy.com/media/4pvW2P5L1GmkM/giphy.gif?cid=ecf05e47fwmqa1qgds7b6ceefqum0kpzb8un9pvajqdkjbwt&rid=giphy.gif" alt="Ellen Page Giphy"></img>'


@app.route('/<int:guess>')
def guess_number(guess):
    """
    Takes in the user's guess and returns if high low or correct.

    Args:
        guess (int): User's guess

    Returns:
        str: Too high, try again!
                or
             Too low, try again!
                or
             You found me!
    """
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


@app.route('/answer')
def show_answer():
    """
    Renders a page to show the correct answer.
    """
    return f"The correct answer is {random_number}."


if __name__ == "__main__":
    app.run(debug=True)
