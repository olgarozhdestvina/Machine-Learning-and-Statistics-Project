## Wind Turbine Power Production
### [Project assessment or Machine Learning and Statistics Module - GMIT 2020]

<img height="300" src="https://images.vexels.com/media/users/3/169388/isolated/preview/8ae55200ad8cdc41bac73f0334acbafe-wind-turbine-generator-wind-farm-three-flat-by-vexels.png">

<br>
This repository contains a web service that uses a machine learning approach to make accurate predictions of wind turbine power from given wind speed
based on the data set powerproduction. 

The project has the following features:

* Jupyter notebook with three machine learning models trained on the data set _powerproduction_.
* Python script running a web service based on the best performing model.
* Dockerﬁle that builds and runs the web service in a container.

<br>

*Submitted by:* Olga Rozhdestvina (Student No: G00387844) 

*Lecturer:* [Ian McLoughlin](https://github.com/ianmcloughlin)

*Programming Language used:* [Python](https://www.python.org/)

<br>

### Set up
___

Applications used for completion of the project are [The Jupyter Notebook](https://jupyter.org/), [Visual Studio Code](https://code.visualstudio.com/), [cmder](http://cmder.net/)

Distribution of the Python used is [Anaconda Python distribution](https://www.anaconda.com/). 

<br>

###  How to run the code
___

1. Make sure that you have Python installed
2. Download or clone current repository "Machine-Learning-and-Statistics-Project"
3. Open Command Interpreter and get into correct directory
4. Install packages and run the app: 
    * If using a virtual environment: 

        ```bash
        pip install -r requirements.txt
        export FLASK_APP=flask_server
        python3 -m flask run
        ```

        # Windows
        ```bash
        pip install -r requirements.txt
        set FLASK_APP=flask_server
        python -m flask run
        ```
    * If using Docker:

        ```bash
        docker build . -t wind-power
        docker run -d -p 5000:5000 wind-power
        ```
        In case of an error, change the first line of the Docker file for your version of Python.
5. To view the model analysis run Jupyter Notebook and open Power_production_models.ipynb. 

<br>

### License
___

This project is licensed under the MIT License - see the LICENSE.md file for details