"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page. <a href='/hello'>Click here</a> for the hello page.</html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet" method="POST">
          What's your name? <input type="text" name="person">
          <br>
          <label>What compliment would you like?</label>
          <select name="compliment">
            <option value="awesome">Awesome</option>
            <option value="terrific">Terrific</option>
            <option value="fantastic">Fantastic</option>
            <option value="neato">Neato</option>
            <option value="fantabulous">Fantabulous</option>
            <option value="wowza">Wowza</option>
          </select>
          <br>

          <label>What diss would you like?</label>
          <select name="diss">
            <option value="terrible">Terrible</option>
            <option value="smelly">Smelly</option>
            <option value="loser">Loser</option>
            <option value="poopy">Poopy</option>
          </select>
          <br>
          <label>Would you like a diss or compliment?</label>
          <input type="radio" value="diss" name="diss-option"> Diss
          <input type="radio" value="compliment" name="diss-option"> Compliment
          <br>
          <input type="submit" value="Submit">

        </form>

      </body>
    </html>
    """


@app.route('/greet', methods=["POST"])
def greet_person():
    """Get user by name."""
    diss_option = request.form.get("diss-option")
    player = request.form.get("person")
    diss = request.form.get("diss")
    comp = request.form.get("compliment")

    if diss_option == "diss":
      return """
        <!doctype html>
        <html>
          <head>
            <title>A Diss</title>
          </head>
          <body>
            Hi, {}! I think you're {}!
          </body>
        </html>
        """.format(player, diss)

    if diss_option == "compliment":
      return """
        <!doctype html>
        <html>
          <head>
            <title>A Compliment</title>
          </head>
          <body>
            Hi, {}! I think you're {}!
          </body>
        </html>
        """.format(player, comp)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
