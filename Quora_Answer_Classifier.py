# Import the classifier
from sklearn.naive_bayes import  GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

# Read in the first lines
first = list(map(int,raw_input().split(" ")))
train_no_obs = first[0]
no_of_param = first[1]

# Read in the training values:
training_obs = []
for i in range(0,train_no_obs):
    training_obs.append(raw_input().replace("\n",""))
    
# Read in test values
test_obs = int(raw_input())
testing_obs = []
for i in range(0,test_obs):
    testing_obs.append(raw_input().replace("\n",""))
    
# Separate Features and Target
training_features = []
training_target = []
int_data = []
for i in training_obs:
    a = i.split(" ")
    training_target.append(int(a[1]))
#    for i in a[2:]:
#         training_features.append(float(i.split(":")[1]))
    training_features.append([float(a1.split(":")[1]) for a1 in a[2:]])

#print training_features
#print training_target

# Separate testing ID, features into separate lists

testing_features = []
int_data = []
testing_id = []
for i in testing_obs:
    testing_id.append(i.split(" ")[0])
    counter = 0
    for j in i.split(" ")[1:]:
        counter = counter+1
        int_data.append(float(j.split(":")[1]))
        if counter == no_of_param:
            testing_features.append(int_data)
            counter = 0
            int_data = []
            
#print testing_features 
#print testing_id

# Build a Naive Bayes model

#clf = GaussianNB()
#clf.fit(training_features,training_target)
#predictions = clf.predict(testing_features)

# Build a SVM model 

#clf1 = SVC(C = 1.0, kernel='linear')
#clf1.fit(training_features,training_target)
#predictions = clf1.predict(testing_features)


# Build a RandomForest Classifier

clf3 = RandomForestClassifier(n_estimators = 20).fit(training_features,training_target)
predictions = clf3.predict(testing_features)


# Define function to print the results in the correct format
def printresults(input):
    for i in range(len(input)):
        if input[i]==1:
            print testing_id[i]+" +1"
        else:
            print testing_id[i]+" -1"
            
            
printresults(predictions)