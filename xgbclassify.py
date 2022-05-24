import numpy as np
import pandas as pd
from sklearn import metrics 
import warnings
warnings.filterwarnings('ignore')
from xgboost import XGBClassifier
data = pd.read_csv("E:\phish\Phishing\phishing.csv")
#droping index column
data = data.drop(['Index'],axis = 1)

y = data['class'].values
X = data.drop('class',axis=1).values 
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score,roc_curve
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 12)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y_train = le.fit_transform(y_train) 

xgb=XGBClassifier()
xgb.fit(X_train,y_train)


y_pred =xgb.predict(X)[0]
        #1 is safe       
        #-1 is unsafe

y_pro_phishing = xgb.predict_proba(X)[0,0]
y_pro_non_phishing = xgb.predict_proba(X)[0,1]
yp = y_pro_non_phishing*100
ys = y_pro_phishing*100

if(y_pred ==1 ):
    print("It is {0:.2f} % safe to go ".format(y_pro_phishing*100))
else:
    print("It is {0:.2f} % unsafe to go ".format(y_pro_non_phishing*100))
import pickle
filename = 'xbgoost_model.pckl'
pickle.dump(xgb, open(filename, 'wb'))

#Predicting the height of Sons
y_test=xgb.predict(X_test)

loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, y_test)
print(result)
