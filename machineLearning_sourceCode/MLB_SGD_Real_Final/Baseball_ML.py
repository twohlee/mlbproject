from csv import reader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

from sklearn import preprocessing
from sklearn import linear_model
from sklearn.metrics import mean_squared_error,mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from subplot import make_plot
import pickle

#=====================================step1
b_total=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/b_total_no_scale.csv')

# 승률
r=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/bat_r.csv')


# 타자 지표
b_corr=b_total[['R','H','2B','HR','RBI','SF','OPS','BB']]

# 승률
rank_PCT=r[['R']]

# y = 득점 수, X = 타자지표
y=rank_PCT; X=b_corr

# ====================================step2
# 사용자 함수 호출
make_plot()

# train 데이터와 test 데이터 정의 및 분리
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,shuffle=False)


# 표준화 함수 정의
sc = preprocessing.StandardScaler()

# 데이터를 표준화
sc.fit(X_train)
X_train_std = sc.transform(X_train)
sc.fit(X_test)
X_test_std = sc.transform(X_test)

clf_ = linear_model.Ridge() 

# 학습 
print(X_train.R)
clf_.fit(X_train, y_train)
y_pred  = clf_.predict(X_test)


# 학습정확도 확인
print('Mean Squared Error :',mean_squared_error(y_test,y_pred))
print('Mean Absolute Error :',mean_absolute_error(y_test,y_pred))
print("train 학습 정확도 :", clf_.score(X_train, y_train)) 
print("test 학습 정확도 :", clf_.score(X_test, y_test)) 

with open('./bs.dat', 'wb') as fp:
    pickle.dump(sc, fp)
    pickle.dump(clf_, fp)

# ==========================================step3
with open('./bs.dat', 'rb') as fp:
    sc = pickle.load(fp)
    clf_ = pickle.load(fp)

#X = [[100, 161, 29, 44, 97, 3,  1.1, 80]]
X = [[97.1,151.1, 32.3, 35.5,101,5.1, 0.9656 , 75.9]] 

# 결과를 추출한다
X_std = sc.transform(X)

y_pred = clf_.predict(X_std)
print("★ 예상 총 득점수는 ★")
print(y_pred)


