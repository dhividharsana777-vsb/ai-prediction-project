from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Create database
def create_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)')
    conn.commit()
    conn.close()

create_db()

# ---------------- ROUTES ----------------

# DEFAULT ROUTE (LOGIN PAGE)
@app.route('/')
def login():
    try:
        return render_template('login.html')
    except Exception as e:
        return str(e)


# SIGNUP PAGE
@app.route('/signup_page')
def signup_page():
    return render_template('signup.html')


# SIGNUP
@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

    return redirect(url_for('login'))


# LOGIN CHECK
@app.route('/login', methods=['POST'])
def login_check():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    conn.close()

    if user:
        return redirect(url_for('home'))
    else:
        return render_template('login.html', error="Invalid Login")


# HOME (Prediction Page)
@app.route('/home')
def home():
    return render_template('index.html')


# PREDICT
@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        final = [np.array(features)]
        prediction = model.predict(final)

        return render_template('index.html', prediction_text=f"Prediction: {prediction[0]:.2f}")
    except:
        return render_template('index.html', prediction_text="Invalid Input")


# RUN APP (RENDER COMPATIBLE)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
