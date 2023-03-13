from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__, template_folder='templates', static_folder='static')
GoogleMaps(app)

app.config['GOOGLEMAPS_KEY'] = "8JZ7i18MjFuM35dJHq70n3Hx4"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/volunteering')
def volunteering():
    markers=[
   {
   'lon':143.93109284099341,
   'lat':-36.96788448566131,
   'popup':'Victoria'
    }
   ]
    return render_template('volunteering.html',markers=markers)

@app.route('/history')
def history():
    return render_template('history.html')

if __name__ == '__main__':
   app.run()