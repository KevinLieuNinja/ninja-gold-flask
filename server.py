from flask import Flask, session, redirect, request, render_template
import random 
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

@app.route('/process_money' ,methods = ["POST"])

def process_money():
    activity = request.form['action']
    if activity == 'farm':
        gold = random.randint(10,20)
        session['activities'].insert(0,'you got ' + str(gold) + ' from the farmer you hustled')
        session['gold'] += gold
        print ('you got ' + str(gold))
    if activity == 'cave':
        gold = random.randint(5,10)
        session['activities'].insert(0,'you got ' + str(gold) + ' from that cave diving trip with that one chick')
        session['gold'] += gold
        print ('you got ' + str(gold))
    if activity == 'house':
        gold = random.randint(2,5)
        session['activities'].insert(0,'you got ' + str(gold) + ' from the house you hit')
        session['gold'] += gold
        print ('you got ' + str(gold))
    if activity == 'casino':
        gold = random.randint(-50,50)
        if 'casino' >= 0:
            print ('lost')

        session['activities'].insert(0,'you got ' + str(gold))
        session['gold'] += gold
        print ('you got ' + str(gold))
    

    return redirect('/')



@app.route('/destroy_session', methods = ['POST'])
def destroyer():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)