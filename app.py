from flask import Flask, render_template, request
import pandas as pd
import pickle
import sklearn
import mimetypes
mimetypes.add_type('text/css', '.css')
mimetypes.add_type('text/javascript', '.js')


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True

# instead of creating two pickle files we could also create a pipeline
knn_model = pickle.load(open('diabetes_predictions.pkl','rb'))
standard_scaler = pickle.load(open('standard_scaler_model.pkl','rb'))

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods = ["GET", "POST"])
def predict():
    if request.method == 'POST':
        pregnancies = int(request.form['pregnancies'])
        glucose = int(request.form['glucose'])
        blood_pressure = int(request.form['blood_pressure'])
        skin_thickness = int(request.form['skin_thickness'])
        insulin = int(request.form['insulin'])
        bmi = float(request.form['bmi'])
        age = int(request.form['age'])

        d = {
            'Pregnancies':[pregnancies],
            'Glucose':[glucose],
            'BloodPressure':[blood_pressure],
            'SkinThickness':[skin_thickness],
            'Insulin':[insulin],
            'BMI':[bmi],
            # passing the mean value here, as this is a complex field and users won't be able to fill in the data
            'DiabetesPedigreeFunction':0.4718,
            'Age':[age]
        }
        df = pd.DataFrame(d)
        scaledDf = pd.DataFrame(standard_scaler.transform(df))

        prediction = knn_model.predict(scaledDf)
        return "You could be having diabetes. Try consulting a doctor!" if prediction[0]==1 else "Woah! Looks like you don't have diabetes."
        
if __name__ == "__main__":
    app.run(host="0.0.0.0")