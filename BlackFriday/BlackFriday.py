####################################RND:Black Friday
# -*- coding: utf-8 -*-

import dask.array as da

#Using arange to create an array with values from 0 to 10
X = da.arange(11,chunks=5)
X.compute()

#Let's see the size of each chunk
X.chunks

#Converting a Numpy array to Dask Array
import numpy as np

x = np.arange(10)

y = da.from_array(x,chunks = 5)
y.compute() #Results in a dask array

#Calculating mean of the first 100 numbers
x = np.arange(1000) #arange is used to create array on values from 0 to 1000
y = da.from_array(x,chunks = (100)) #Converting numpy array to dask array

y.mean().compute() #Computing mean of the array


#Reading a csv (Comparing the read time with pandas)
import pandas as pd

%time temp = pd.read_csv("BlackFriday_train.csv")

#Reading the ile using dask
import dask.dataframe as dd
%time df = dd.read_csv("BlackFriday_train.csv")

#Finding value count for a particular column
df.Gender.value_counts().compute()

#Using groupby on the Dask dataframe - Finding maximum value of purchase for both genders
df.groupby(df.Gender).Purchase.max().compute()

##ML models - Parallelize Scikit-Learn directly: Creating a local scheduler & worker on the machine
from dask.distributed import Client
client = Client()

#Instantiating dask joblib in backend-import parallel_backend from sklearn joblib as below:
import dask_ml.joblib

from sklearn.externals.joblib import parallel_backend

with parallel_backend('dask'):
    #Your normal scikit-learn code here:
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier()    

#Reimplementing Algorithms with dask array 
    #Linear Model
from dask_ml.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(data,labels)
    
    #Pre-processing example
from dask_ml.preprocessing import OneHotEncoder
encoder = OneHotEncoder(sparse=True)
result = encoder.fit(data)

    #Clustering example
from dask_ml.cluster import KMeans
model = KMeans()
model.fit(data)




###Solving a Machine Learning Problem:
#1. Using a simple logistic regression model and making predictions
#reading the csv files
import dask.dataframe as dd
df = dd.read_csv('BlackFriday_train.csv')
test=dd.read_csv("BlackFriday_test.csv")

#having a look at the head of the dataset
df.head()

#finding the null values in the dataset
df.isnull().sum().compute()

#defining the data and target
categorical_variables = df[['Gender', 'Age', 'Occupation', 'City_Category', 'Stay_In_Current_City_Years', 'Marital_Status']]
target = df['Purchase']

#creating dummies for the categorical variables
data = dd.get_dummies(categorical_variables.categorize()).compute()

#converting dataframe to array
datanew=data.values

#fit the model
from dask_ml.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(datanew, target)

#preparing the test data
test_categorical = test[['Gender', 'Age', 'Occupation', 'City_Category', 'Stay_In_Current_City_Years', 'Marital_Status']]
test_dummy = dd.get_dummies(test_categorical.categorize()).compute()
testnew = test_dummy.values

#predict on test and upload
pred=lr.predict(testnew)

##2. Using grid search and random forest algorithm to find the best set of parameters.
from dask.distributed import Client
client = Client() # start a local Dask client

import dask_ml.joblib
from sklearn.externals.joblib import parallel_backend
with parallel_backend('dask'):

    # Create the parameter grid based on the results of random search 
     param_grid = {
    'bootstrap': [True],
    'max_depth': [8, 9],
    'max_features': [2, 3],
    'min_samples_leaf': [4, 5],
    'min_samples_split': [8, 10],
    'n_estimators': [100, 200]
    }

# Create a based model
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()

# Instantiate the grid search model
import dask_searchcv as dcv
grid_search = dcv.GridSearchCV(estimator = rf, param_grid = param_grid, cv = 3)
grid_search.fit(data, target)
grid_search.best_params_