# Enter your code here. Read input from STDIN. Print output to STDOUT
from sklearn import linear_model
reg = linear_model.LinearRegression()

# Read input
train = list(map(int,raw_input().split(" ")))
list_train = []


# Read in the values training data
for i in range(0,train[1]):
    list_train.append(list(map(float,raw_input().split(" "))))

# Split Dict_train into features and target
feature_train = []
target_train = []

for i in range(0,len(list_train)):
    feature_train.append(list_train[i][0:train[0]])
    target_train.append(list_train[i][train[0]])
    
# Read in values of test data
test = int(raw_input())
list_test = []

for i in range(0,test):
    list_test.append(list(map(float,raw_input().split(" "))))


# Fit the model
reg.fit(feature_train,target_train)

#predict the values
for i in range(0,len(list_test)):
    print round(reg.predict(list_test[i]),2)