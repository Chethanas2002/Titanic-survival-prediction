#importing the dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from Interface import Ui_MainWindow

def perdiction_model(input_data):
    #load data from csv to pandas
    titanic_data = pd.read_csv('train.csv')

    # Drop  cabin column from dataframe as maximimum values are missing
    titanic_data = titanic_data.drop(columns = 'Cabin',axis = 1)

    #replacing missing values in age column with the mean of the same
    titanic_data['Age'].fillna(titanic_data['Age'].mean(),inplace = True)

    #replacing missing values in fare column with the mean of the same
    titanic_data['Fare'].fillna(titanic_data['Fare'].mean(),inplace = True)

    #converting category column
    titanic_data.replace({'Sex':{'male':0,'female':1}, 'Embarked':{'S':0 , 'C':1 , 'Q':2}}, inplace=True)

    #separating features and target inforamtion
    X = titanic_data.drop(columns=['Name','PassengerId','Ticket','Survived'],axis = 1)
    Y = titanic_data['Survived']

    #Splitting the data into training and testing data
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=2)

    #Model Training
    model = LogisticRegression(solver='lbfgs', max_iter=1000)
    #training the logistic regression model with training data
    model.fit(X_train,Y_train)

    #accuracy on traininge data
    X_train_prediction = model.predict(X_train)


    #predictive system
    #Pclass  Sex  Age  SibSp  Parch  Fare  Embarked

   
    #print(input_data)

    #input_data = ()
    """def perform_analysis(age):
        print(age)"""
    #changing the input data to numpy array
    input_data_as_numpy = np.asarray(input_data)

    #reshape the numpy array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy.reshape(1,-1)
    prediction = model.predict(input_data_reshaped)
    mortal_status = ['U Die', "You will see the next day's light"]
    print(mortal_status[prediction[0]])
    #print(input_data)

  