from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Perform authentication here
        # If authentication is successful, redirect to the home page
        return redirect(url_for('index'))
    return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        # Perform user registration here
        # If registration is successful, redirect to the home page
        return redirect(url_for('index'))
    return render_template('signup.html')

@app.route('/')
def index():
    return render_template('index.html')

    if __name__ == "__main__":
        aoo.run(debug=True)