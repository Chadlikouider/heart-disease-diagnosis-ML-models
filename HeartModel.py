"""

@author: CHADLI KOUIDER
Written : Saturday,May 28th 2022 (beginning)
          Thursday,June 2nd 2022 (finished)
Email: chadli_kouider@hotmail.com
       chadkouider@gmail.com
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from joblib import dump, load # to save and load the model
import os.path
import sys


np.random.seed(123)

testPerc = 0.2    # Size of the test data with respect to raw data (range(0,1))

KNN_CONST = 14     # The K constant used in KNN

FILENAME = "processed.cleveland.data" # file containing Raw data

NAMES = ["Age","Sex","cp","trestbps","chol","fbs","restecg","thalach",
         "exang","oldpeak","slope","ca","thal","num"] 


"""
Attribute documentation:
    Age: age in years
    Sex: sex (1 = male; 0 = female)
    cp: chest pain type
        -- Value 1: typical angina
        -- Value 2: atypical angina
        -- Value 3: non-anginal pain
        -- Value 4: asymptomatic
    trestbps: resting blood pressure (in mm Hg on admission to the hospital)
    chol: serum cholestoral in mg/dl
    fbs: (fasting blood sugar > 120 mg/dl)  (1 = true; 0 = false)
    restecg: resting electrocardiographic results
        -- Value 0: normal
        -- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
        -- Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria
    thalach: maximum heart rate achieved
    exang: exercise induced angina (1 = yes; 0 = no)
    oldpeak: ST depression induced by exercise relative to rest
    slope: the slope of the peak exercise ST segment
        -- Value 1: upsloping
        -- Value 2: flat
        -- Value 3: downsloping
    ca: number of major vessels (0-3) colored by flourosopy
    thal: 3 = normal; 6 = fixed defect; 7 = reversable defect
    num: diagnosis of heart disease (angiographic disease status) 
         from the scale of 0 to 4 (However for this program I overwrote the result to make it
                                    0: Healthy and 1: Sick)
"""

# Pick a name for the file of the saved model depending on the picked ML model
def model_name(pick):
    try:
        
        if (pick == 0):
            return "Logistic_Regression_model.sav"
        elif (pick == 1):
            return "Decision_Tree_model.sav"
        elif (pick == 2):
            return "KNN_model.sav"
        else:
            print("selected Unknown model")
            sys.exit(1)
    except:
        print("selected Unknown model")
        sys.exit(1)   


# Create a model if it does NOT already exist   
def CreateModel(model_index) :
    # model_index : 0>>Logistic Regression, 1>> Decision Tree end so on
    
    data = pd.read_csv(FILENAME,names=NAMES)
    
    # rectify some of the elements on the dataset
    # Some of the data are defined as "?"(unknown), thus it is required to change it
    for i in data.columns[:-1]:
        data[i] = data[i].apply(lambda x: data[data[i] != '?'][i].astype(float).mean()
                                if x == '?' else x)
        data[i] = data[i].astype(float)
    # map the outputs (0,1,2,3,4) to (0,1)
    # 0>>0 meaning healthy
    # 1,2,3,4 >> 1 meaning sick
    #data["num"] = data["num"].apply(lambda y: 1
                                   # if y > 1 else y)
    
    
    #   Define the Inputs and the output
    Inputs = np.array(data.drop(columns="num", axis = 1))
    Outputs = np.array(data["num"])
    
    #   Set the data to training/testing data
    x_train, x_test, y_train, y_test = train_test_split(Inputs, Outputs, test_size = testPerc )
    
    
    #   Define the model and train it
    if model_index == 0:
        Model = LogisticRegression(solver='liblinear', max_iter=100)
        Model.fit(x_train, y_train)
    elif model_index == 1:
        Model = DecisionTreeClassifier()
        Model.fit(x_train, y_train)    
    elif model_index == 2:
        Model = KNeighborsClassifier(n_neighbors=KNN_CONST)
        Model.fit(x_train, y_train)
        
    # Compute the Evaluation and validation accuracy and save them on a txt file
    eval_accuracy = Model.score(x_train, y_train)
    val_accuracy = Model.score(x_test,y_test)
    
    f = open("scores_"+model_name(model_index)[:-4]+".txt","w")
    f.write(model_name(model_index)+": \n")
    f.write("the evaluation accuracy : "+ str(eval_accuracy)+"\n")
    f.write("the validation accuracy : "+ str(val_accuracy)+"\n\n")
    f.close()
    # Compute the accuracy, precision and recall
    Predictions = Model.predict(x_test)
    
    f = open("scores_"+model_name(model_index)[:-4]+".txt","a")
    f.write("Accuracy : "+str(accuracy_score(y_test, Predictions))+"\n")
    f.write("Precision : "+str(precision_score(y_test, Predictions,average=None)[1])+"\n")
    f.write("Recall : "+ str(recall_score(y_test, Predictions,average=None)[1]))
    f.close()
    
    
    # Save the model on the folder or disk (to use later)
    dump(Model, model_name(model_index))
    dump(accuracy_score(y_test, Predictions),"Accuracy_"+model_name(model_index))
    
    
def main(data_string):
    
    # set the arguments on form of a list then do type casting
    InputData = data_string.split(" ") # seperate the string to a set of string
    InputData = [float(e) for e in InputData] # Type casting  
    
    model_pick = InputData.pop() # Pop the last element of the array and assign it to a variable
                                 # the value express the choice of the Model
    # check if the model already exists
    model_savename = model_name(model_pick)
    print(model_savename)
    # If the model does not exists then create one
    if not os.path.isfile('/'.join((os.path.dirname(os.path.realpath("__file__")),model_savename))):
        CreateModel(model_pick) # create a model then store it on the folder
    # load the model
    Model = load(model_savename)
    Predictions = Model.predict([InputData[:]])
    print("The Output is :"+str(Predictions[0])+"\n")
    return [Predictions[0],model_name(model_pick)[:-4],load("Accuracy_"+model_name(model_pick))]
# the return of the main is  [float : Prediction (0-4), string:name of the model, float:the accuracy of the model]
    








