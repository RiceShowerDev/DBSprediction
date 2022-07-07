import joblib
model=joblib.load(r'D:\PROGRAMS\NTU\regression.jl')
model.coef_
model.intercept_
print(model.predict([[1.4]]))
model=joblib.load(r'D:\PROGRAMS\NTU\decisiontree.jl')
print(model.predict([[1.4]]))