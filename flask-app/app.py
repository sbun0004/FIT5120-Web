from flask import Flask, render_template
app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/volunteering')
def volunteering():
    return render_template('volunteering.html')

@app.route('/history')
def history():
    return render_template('history.html')

if __name__ == '__main__':
   app.run()