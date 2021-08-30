from typing_extensions import Concatenate
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)




@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    if request.method == "POST":

        Rnumber = (request.form["Rnumber"])
        Fnumber = (request.form["Fnumber"])
        Mnumber = (request.form["Mnumber"])
        RFM =((int(Rnumber)+int(Fnumber)+int(Mnumber))/3)

        Prediction = []
        if(RFM<1.33):
            Prediction.append("Medium")
        elif((RFM > 1.33) & (RFM <2.66)):
            Prediction.append("Best")
        elif((RFM > 2.66) & (RFM <=3)):
            Prediction.append("Worst")
        
    

        return render_template('index.html', prediction_text='Category of the Customer should be {}'.format(Prediction[0]))



if __name__ == "__main__":
    app.run(debug=True)