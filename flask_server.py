#!flask/bin/python

"""
Project assessment
Machine Learning and Statistics Module - GMIT 2020
Submitted by: Olga Rozhdestvina (Student No: G00387844)
Lecturer: Ian McLoughlin
"""

# Flask.
from flask import Flask, render_template, abort, request, jsonify
from werkzeug.exceptions import BadRequest, NotFound, MethodNotAllowed, InternalServerError
#from Model import model
# Model Building and training

# Model.
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

# Preprocessing.
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import PolynomialFeatures

# Numerical arrays.
import numpy as np
# Data frames.
import pandas as pd
# Flask app.
app = Flask(__name__, static_folder="static",
            template_folder="templates")

# Home page.
@app.route('/')
def home():
    return render_template("index.html")

# Outputting power.
@app.route('/calculate/', methods=["POST"])
def power():
    try:
        # Load the data and preprocess it. 
        df = pd.read_csv("powerproduction.csv")
        df_new = df.drop(df[(df.power == 0) & (df.speed > 5)].index)

        speed = df_new.iloc[:, 0].values
        power = df_new.iloc[:, 1].values

        X = np.array(speed).reshape(-1,1)
        y = np.array(power).reshape(-1,1)

        # Scaling
        scaler = MinMaxScaler()
        X = scaler.fit_transform(X)
        y = scaler.fit_transform(y)
        
        # Split the data on training and test
        speed_train, speed_test, power_train, power_test = train_test_split(X, y, test_size=0.3, random_state=1)
        
        # Create a model.
        pipeline = make_pipeline(PolynomialFeatures(22), LinearRegression())
        pipeline.fit(speed_train, power_train)

        # Get speed input from the form and preprocess it.
        speed = float(request.form['speed'])
        speed = np.array(speed).reshape(-1,1)
        input_speed = scaler.fit_transform(speed)
        print(input_speed)
        print(speed_test[5])

        # Power prediction
        power_output = pipeline.predict(speed_test)
        print(power_output)
        print(f"Predicted power: {str(scaler.inverse_transform(power_output)[5])[1:-1]}")
        return {str(scaler.inverse_transform(power_output)[5])[1:-1]}

    except:
        print("Failed to preprocess data")

# Error handlers.
@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return 'Bad request!', e


@app.errorhandler(NotFound)
def handle_bad_request(e):
    return 'Page is not found!', e


@app.errorhandler(MethodNotAllowed)
def handle_bad_request(e):
    return 'Method is not allowed!', e


@app.errorhandler(InternalServerError)
def handle_bad_request(e):
    return 'Internal server error!', 500

if __name__ == '__main__':
    app.run(debug=True)