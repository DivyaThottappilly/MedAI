# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import math


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    
    final_features = [np.array(int_features)]
    print (final_features)
    scaled_features=scaler.transform(final_features)
    prediction = model.predict(scaled_features)
    
    print ("prediction ",prediction)
    
    output = prediction
    
    if (output ==1):
        prediction='Patient Has Liver Disease '
    else:
        prediction='Patient Has No Liver Disease '

    return render_template('index.html', prediction_text=str(prediction)+' $ {}'.format(output))

@app.route('/meldpredict',methods=['POST'])
def meldpredict():
    '''
    For rendering MELD Score
    '''
    int_features = [x for x in request.form.values()]
    if request.form['choice-radio'] == 'yes':
       print('yes button pressed')
    elif request.form['choice-radio'] == 'no':
        print('no button pressed')
        

    serum_creatinine =float(int_features[1])
    serum_bilirubin = float(int_features[2])
    inr = float(int_features[3])
    sodium = float(int_features[4])
    if sodium <125:
        sodium = 125
    elif sodium >137:
        sodium = 137
        
    meld_score =round( 3.78 * math.log(serum_bilirubin) + 11.2 * math.log(inr) + 9.57 * math.log(serum_creatinine) + 6.43)
    meld_na_score = round(meld_score - sodium - (0.025 * meld_score * (140-sodium)) +140)
    print(meld_score)
    
    print(meld_na_score)
    prediction='MELD Score is '+' {}'.format(meld_score)+' & MELD Na Score is'+' {}'.format(meld_na_score)
   
    #return render_template('index.html', meld_score=str(prediction)+' $ {}'.format(meld_score))
    return render_template('index.html', meld_score=str(prediction))

if __name__ == "__main__":
    app.run(debug=True)
