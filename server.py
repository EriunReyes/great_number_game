from flask import Flask, render_template, request, session, redirect
import random

app=Flask(__name__)
app.secret_key = "secretkey"
@app.route('/')
def game():
    if 'numbers' not in session:
        session['numbers'] = random.randint(1,100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def random():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)