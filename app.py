#Insert necessary libraries
from flask import Flask, render_template, request, Markup
import config
import requests
import numpy as np
import pandas as pd
import pickle

#==========loading trained models
# Loading crop recommendation model

crop_recommendation_model_path = 'models/RandomForest.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))


#=========custom functions=================
#function for get weather data

def weather_fetch(city_name):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    api_key = config.weather_api_key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    #print(x["cod"])
    if x["cod"] != "404":
        y = x["main"]

        temperature = round((y["temp"] - 273.15), 2)
        humidity = y["humidity"]
        return temperature, humidity
    else:
        return None



#======= Flask app starts here==============================


app = Flask(__name__)

# render home page

@ app.route('/')
def home():
    title = 'Farmhelper - Home'
    return render_template('index.html', title=title)
    


# render crop recommendation form page


@ app.route('/crop_recommend')
def crop_recommend():
    title = 'Farmhelper - Crop Recommendation'
    return render_template('crop.html', title=title)



#render crop prediction from page
@ app.route('/crop_prediction',methods=['POST'])
def crop_prediction():
    title = 'Farmhelper - Crop Prediction'

    if request.method == 'POST':
        #print("method post")
        N = int(request.form['N'])
        P = int(request.form['P'])
        K = int(request.form['K'])
        ph = float(request.form['ph'])
        rl = float(request.form['rl'])

        # state = request.form.get("stt")
        district = request.form.get("district")
        #print(N,P,K,ph,rl,district)
        
        if weather_fetch(district) != None:
            temperature, humidity = weather_fetch(district)
            data = np.array([[N, P, K, temperature, humidity, ph, rl]])
            my_prediction = crop_recommendation_model.predict(data)
            final_prediction = my_prediction[0]

            #return render_template('crop-result.html', prediction=final_prediction, title=title)
            print(data)
            return render_template('error.html', title=title)

        else:
            return render_template('error.html', title=title)
            
    
# ===============================================================================================
if __name__ == '__main__':
    app.run(debug=True)
