import os
from flask import Flask, render_template, send_from_directory

TEMPLATE_DIR = os.path.abspath('../../public/pages')
STATIC_DIR = os.path.abspath('../../public')
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

# Main Routes
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about-us')
def about():
  return render_template('about-story.html')

@app.route('/board-members')
def board():
  return render_template('about-board.html')

@app.route('/donate')
def donate():
  return render_template('donate.html')

@app.route('/foster-with-us')
def foster():
  return render_template('foster.html')

@app.route('/volunteer-with-us')
def volunteer():
  return render_template('volunteer.html')

@app.route('/why-nafn')
def why():
  return render_template('why-nafn.html')

if __name__ == '__main__':
  app.run(debug=True)

app.run("0.0.0.0", ssl_context=("cert.pem", "key.pem"), port=3000)
