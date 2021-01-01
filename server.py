from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    """
    Renders the root page for the site.  Asks the user to guess a number.
    """
    return '<h1>Guess a number between 0 and 9</h1>' \
    '<img src="https://media0.giphy.com/media/4pvW2P5L1GmkM/giphy.gif?cid=ecf05e47fwmqa1qgds7b6ceefqum0kpzb8un9pvajqdkjbwt&rid=giphy.gif" alt="Ellen Page Giphy"></img>'

if __name__ == "__main__":
    app.run(debug=True)
