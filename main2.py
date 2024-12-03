from flask import Flask, render_template, request, redirect, url_for, session
import random
import string

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Important for session management

# Admin credentials (replace with secure storage later)
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'password'

def generate_otp(length=6):
  """Generates a random OTP."""
  characters = string.ascii_letters + string.digits + string.punctuation
  otp = ''.join(random.choice(characters) for i in range(length))
  return otp

@app.route('/', methods=['GET', 'POST'])
def index():
  if 'logged_in' in session:
    if request.method == 'POST':
      if __name__ == '__main__':
        app.run(debug=True)
        length = int(request.form.get('length'))
      otp = generate_otp(length)
      return render_template('index.html', otp=otp, length=length)
    return render_template('index.html')
  else:
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
      session['logged_in'] = True
      return redirect(url_for('index'))
    else:
      return 'Invalid username or password'
  return render_template('login.html')  
  