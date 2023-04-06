from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/') # Must add this to the url to call the function below.
def home():
    return render_template('home.html') #Flask looks inside templates folder by default.

@app.route('/api/v1/<station>/<date>') # Must add this to the url to call the function below.
def about(station, date):
    df = pd.read_csv("")
    temperature = df.station(date)
    return {'station': station, 
            'date': date, 
            'temperature': temperature}
    # return str(temperature)

if __name__ == "__main__":
    app.run(debug=True)