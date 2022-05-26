# Gradient Boosting Classifier Model
from sklearn.ensemble import GradientBoostingClassifier
import pandas as pd
import pickle
data = pd.read_csv("C:/Users/hp/desktop/project/urldata.csv")
#droping index column
data = data.drop(['Domain'],axis = 1)
# Splitting the dataset into dependant and independant fetature

y = data['Label'].values
X = data.drop('Label',axis=1).values 

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 12)
print(X)
print(y)
gbc = GradientBoostingClassifier(max_depth=4,learning_rate=0.7)
gbc.fit(X,y)
y_pred =gbc.predict(X)[0]
print(y_pred)
y_pro_phishing = gbc.predict_proba(X)[0,0]
y_pro_non_phishing = gbc.predict_proba(X)[0,1]
    # save the model to disk
filename = 'finalized_model_gb.sav'
pickle.dump(gbc, open(filename, 'wb'))
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, y_test)
print(result)

'''if(y_pred ==1 ):
    print("It is {0:.2f} % safe to go ".format(y_pro_phishing*100))
else:
    print("It is {0:.2f} % unsafe to go ".format(y_pro_non_phishing*100))'''

if(result>0.8):
    print("The System detected best accuracy  of {0:.2f} !!".format(result*100))
    print("Leigtimate site")

else:
    print("System detected less accuracy")
    print("Warning !, suspicious site")
