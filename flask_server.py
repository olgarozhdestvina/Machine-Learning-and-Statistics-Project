#!flask/bin/python

"""
Project assessment
Machine Learning and Statistics Module - GMIT 2020
Submitted by: Olga Rozhdestvina (Student No: G00387844)
Lecturer: Ian McLoughlin
"""
# Numerical arrays.
import numpy as np
# Data frames.
import pandas as pd
# Flask.
from flask import Flask, render_template, request
from werkzeug.exceptions import BadRequest, NotFound, MethodNotAllowed, InternalServerError
# Model.
import tensorflow.keras as kr
# Preprocessing.
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import PolynomialFeatures

# Flask app.
app = Flask(__name__, static_folder="static",
            template_folder="templates")

# Home page.
@app.route('/')
def home():
    return render_template("index.html")


"""
Creating a Neural Network model 
and predicting power from the input speed.
"""
@app.route('/calculate/', methods=["POST"])
def power():
    try:
        speed_train, power_train, input_speed, scaler = preprocess()
        # Create a model.
        model = kr.models.Sequential()
        model.add(kr.layers.Dense(55, input_shape=(53,), activation='relu',
                                  kernel_initializer=kr.initializers.RandomUniform(seed=1)))
        model.add(kr.layers.Dense(25, activation='relu',
                                  kernel_initializer=kr.initializers.he_uniform(seed=1)))
        model.add(kr.layers.Dense(1, activation='softplus',
                                  kernel_initializer=kr.initializers.RandomUniform(seed=1)))
        # Compile the model.
        model.compile(optimizer=kr.optimizers.Adam(0.01), loss='mse')
        # Fit the model to the training data (hide the output).
        model.fit(speed_train, power_train, verbose=False,
                  epochs=130, batch_size=len(speed_train))
        # Power prediction, round the output to three decimal places and return as a trimmed string.
        power_output = model.predict(input_speed)
        power_output = scaler.inverse_transform(power_output.reshape(-1, 1))
        return str(np.round(power_output, 3))[2:-2]
    except:
        print("Failed to predict the power output")


# Loading the data set and separating for variables.
def load_dataset():
    try:
        df = pd.read_csv("powerproduction.csv")
        df_new = df.drop(df[(df.power == 0) & (
            df.speed > 5) & (df.speed < 24)].index)
        speed = df_new.iloc[:, 0].values
        power = df_new.iloc[:, 1].values
        # Convert into 2D numpy arrays
        X = np.array(speed).reshape(-1, 1)
        y = np.array(power).reshape(-1, 1)
        return X, y
    except FileNotFoundError:
        print("The data set doesn't exist in the same directory")


"""
Data preprocessing of the data set variables 
and input speed from the Web service
"""


def preprocess():
    try:
        X, y = load_dataset()
        # Get speed input from the form, convert into 2D array.
        s = request.form['speed']
        s = np.array(s).reshape(-1, 1)
        # Scaling
        scaler = MinMaxScaler()
        X = scaler.fit_transform(X)
        input_speed = scaler.transform(s)
        y = scaler.fit_transform(y)
        # Split the data on training and test
        speed_train, speed_test, power_train, power_test = train_test_split(
            X, y, test_size=0.3, random_state=1)
        # Apply plynominal Features
        poly = PolynomialFeatures(52)
        speed_train = poly.fit_transform(speed_train)
        speed_test = poly.fit_transform(speed_test)
        input_speed = poly.transform(input_speed)
        return speed_train, power_train, input_speed, scaler
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
    return 'Internal server error!', e


if __name__ == '__main__':
    app.run(debug=True)