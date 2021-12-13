#Insert necessary libraries
from flask import Flask, render_template, request, Markup




# Flask app starts here


app = Flask(__name__)

# render home page

@ app.route('/')
def home():
    title = 'Farmhelper - Home'
    return render_template('index.html', title=title)
    


# render crop recommendation form page


@ app.route('/crop_recommend')
def crop_recommend():
    title = 'Harvestify - Crop Recommendation'
    return render_template('crop.html', title=title)

# ===============================================================================================
if __name__ == '__main__':
    app.run(debug=True)
