from flask import Flask, render_template, session, flash, redirect, url_for, escape, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = 'MD83Sfsadj892sko!2ls#43Jd_8d3_zaza'
Bootstrap(app)

# temp fake database dictionary
users = {
    'james@example.com': {
        'name': 'James',
        'password': 'pass123'
    },
    'frank@example.com': {
        'name': 'Frank',
        'password': '12345'
    }
}

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username=users[session['username']]['name'])
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'username' in session:
            return redirect(url_for('index'))

    if request.method == 'POST':
        if request.form['inputemail'] in users:
            username = request.form['inputemail']
            if request.form['inputpassword'] == users[username]['password']:
                session['username'] = request.form['inputemail']
                flash('You have successfully logged in')
                return redirect(url_for('index'))
            else:
                flash('Incorrect Password', 'bad')
                return redirect(url_for('login'))
        else:
            flash('{} not registered'.format(request.form['inputemail']), 'bad')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been sucessfully logged out', 'ok')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
