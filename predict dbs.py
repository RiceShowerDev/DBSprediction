from os import renames
from pyexpat import model
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn import tree
import joblib
df = pd.read_csv(r'D:\PROGRAMS\NTU\DBS_SingDollar.csv')
# print(df.head)
X=df.loc[:,["SGD"]]
Y=df.loc[:,["DBS"]]

##线性回归
model = linear_model.LinearRegression()
model.fit(X,Y)
# print(model.coef_)
# print(model.intercept_)

# DBS=90.2-50.6
# excel里面不用scv，一定要用xlsx文件

pred = model.predict(X)
# print(pred)
rmse=mean_squared_error(Y,pred) ** 0.5
# print(rmse)
joblib.dump(model,"regression.jl")


##决策树
model=tree.DecisionTreeRegressor()
model.fit(X,Y)
pred = model.predict(X)
rmse=mean_squared_error(Y,pred) ** 0.5
# print(rmse)
joblib.dump(model,"decisiontree.jl")