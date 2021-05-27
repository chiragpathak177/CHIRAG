from sklearn.linear_model import LinearRegression
import pandas
model=LinearRegression()
box=pandas.read_csv('marks1.csv')
x=box['hrs'].values.reshape(6,1)
y=box['marks']
model.fit(x,y)
print("Your Cofficient is :",int(model.coef_))
Data=int(input("Enter Value for Prediction : "))
Result=int(model.predict([[Data]]))
print("Result of precition : ",Result)
© 2021 GitHub, Inc.
