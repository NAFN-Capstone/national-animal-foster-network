import os
from flask import Flask, render_template, send_from_directory

# Resolve paths relative to this file so behavior is consistent inside containers
HERE = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.abspath(os.path.join(HERE, '../../public/pages'))
STATIC_DIR = os.path.abspath(os.path.join(HERE, '../../public'))
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
  # Respect environment variables so Docker can set the port/host
  host = os.environ.get('HOST', '0.0.0.0')
  port = int(os.environ.get('PORT', 3000))
  debug = os.environ.get('FLASK_DEBUG', 'false').lower() in ('1', 'true', 'yes')

  # Optional SSL: set SSL_CERT and SSL_KEY environment vars if you really want TLS inside the container
  ssl_cert = os.environ.get('SSL_CERT')
  ssl_key = os.environ.get('SSL_KEY')
  ssl_context = (ssl_cert, ssl_key) if ssl_cert and ssl_key else None

  app.run(host=host, port=port, debug=debug, ssl_context=ssl_context)
