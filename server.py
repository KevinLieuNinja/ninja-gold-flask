from flask import Flask, session, redirect, request, render_template

app = Flask(__name__)
app.secret_key = 'totallytopsecret'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
        session['activities'].insert(0,"Game Began")

    return render_template('index.html', gold=session['gold'], activities=session['activities'])



app.run(debug=True)