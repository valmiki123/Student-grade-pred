import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.utils import shuffle
import pickle

data=pd.read_csv('student-mat.csv')
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]
predict = "G3"
x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2)

linear_regression = LinearRegression()
linear_regression.fit(xtrain, ytrain)
accuracy = linear_regression.score(xtest, ytest)
print(accuracy)
model=open('modle.pkl','wb')
pickle.dump(linear_regression,model)
model.close()