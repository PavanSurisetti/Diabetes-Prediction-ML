import pandas as p  # for loading the dataset
from sklearn.model_selection import train_test_split  # for training and splitting the data
from sklearn.linear_model import LogisticRegression  # this is the algorithm i have used
from sklearn.metrics import accuracy_score  # measures my model accuracy
import joblib  # for saving the trained model

# loading the dataset
ds = p.read_csv('diabetes2.csv')

# separating input and output
input = ds.iloc[:, :8]
output = ds['Outcome']

# splitting the dataset
x_train, x_test, y_train, y_test = train_test_split(
    input, output, random_state=42, test_size=0.2
)

# creating the model
model = LogisticRegression(max_iter=1000)

# training the model
model.fit(x_train, y_train)

# saving the trained model using joblib
joblib.dump(model, 'diabetes_model.pkl')  # model saved for deployment

# predict on test data
y_pred = model.predict(x_test)

# i want to give my own input now!
my_input = [[1, 146, 74, 36, 0, 35, 0.795, 42]]

'''
Value	Meaning
0	    Not diabetic
1	    Diabetic
'''

# converting input into DataFrame
my_input = p.DataFrame(my_input, columns=input.columns)

# predicting for custom input
print(f'the prediction says: {model.predict(my_input)[0]}')  # 1-yes there 0-not there

# calculating the metrics
print(f'the accuracy score: {accuracy_score(y_test, y_pred)}')
