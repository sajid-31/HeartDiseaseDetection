from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
# import keras
# from keras.models import Sequential
# from keras.layers import Dense
# from keras.layers import LeakyReLU,PReLU,ELU
# from keras.layers import Dropout
# from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('this_is_it.pkl', 'rb'))
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/A',methods=['GET'])
def Home():
    return render_template('A.html')

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Age = int(request.form['Age'])
        RestingBP = int(request.form['RestingBP'])
        Cholesterol = int(request.form['Cholesterol'])
        MaxHR = int(request.form['MaxHR'])
        Oldpeak = float(request.form['Oldpeak'])

        M = request.form['Sex']
        if(M=='M'):
            M=1
        else:
            M=0

        Flat= request.form['ST_Slope']
        if(Flat=='Flat'):
             Flat = 1
             Up = 0    
        elif(Flat == 'Up'):
             Flat = 0
             Up = 1    
        else:
            Flat = 0
            Up = 0   

        ATA = request.form('ATA')
        if(ATA == 'ATA'):
             NAP = 0
             TA = 0
             ATA = 1 
        elif(ATA == 'NAP'): 
             NAP = 1
             TA = 0
             ATA = 0    
        elif(ATA == 'ASY'): 
             NAP = 0
             TA = 0
             ATA = 0   
        elif(ATA == 'TA'): 
             NAP = 0
             TA = 1
             ATA = 0

        FastingBS = int(request.form('FastingBS'))

        Normal = request.form('RestingECG')                  
        if(Normal == 'Normal'):
             Normal = 1
             ST =  0
        elif(Normal == 'LVH'):
             Normal = 0
             ST =  0
        elif(Normal == 'ST'):
             Normal = 0
             ST =  1   

        Y = request.form('ExerciseAngina')
        if( Y == 'Y'):
             Y = 1
        else:
             Y = 0

        prediction = model.predict([['Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak', 'M', 'Flat','Up', 'Y', 'Normal', 'ST', 'ATA', 'NAP', 'TA']])   

        output=round(prediction[0],2)

        return render_template('A.html',prediction_text="You Can Sell The Car at {}".format(output))           




if __name__=="__main__":
    app.run(debug=True)
