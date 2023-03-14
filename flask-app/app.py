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
    lon = 143.93109284099341
    lat = -36.96788448566131
    markers=[
    {
        'lon': lon+0.25,
        'lat': lat+0.25,
        'popup': "Event: Cleaning the road, 17 April 2023,  "+str(lon+0.25)+" "+str(lat+0.25)
    },
    {
        'lon': lon-0.25,
        'lat': lat+0.25,
        'popup': "Event: Waste Sorting, 6 April 2023,  "+str(lon-0.25)+" "+str(lat+0.25)
    },
    {
        'lon': lon+0.25,
        'lat': lat-0.25,
        'popup': "Event: Reducing Waste, 12 April 2023,  "+str(lon+0.25)+" "+str(lat-0.25)
    },
    {
        'lon': lon-0.25,
        'lat': lat-0.25,
        'popup': "Event: Recycling, 23 April 2023,  "+str(lon-0.25)+" "+str(lat-0.25)
    }
   ]
    return render_template('volunteering.html',markers=markers)

@app.route('/history')
def history():
    return render_template('history.html')

if __name__ == '__main__':
   app.run()