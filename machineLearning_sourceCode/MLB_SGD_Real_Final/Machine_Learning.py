# import necessary libraries
from csv import reader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# 사이킷 런
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error,mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 사용자 함수 호출
from subplot import make_plot

# 2010~2018년 데이터 & 2019년 데이터
bat_total_2010_2018=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/bat_total_2010_2018.csv')
bat_total_2019=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/bat_total_2019.csv')
r_total_2010_2018=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/r_2010_2018.csv')
r_total_2019=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/r_2019.csv')

# scatter로 확인
make_plot()

# train 데이터와 test 데이터 정의 및 분리
X_train=bat_total_2010_2018[['R','H','2B','HR','RBI','SF','OPS','BB']]
X_test=bat_total_2019[['R','H','2B','HR','RBI','SF','OPS','BB']]
y_train=r_total_2010_2018[['R']]
y_test=r_total_2019[['R']]

# 표준화 함수 정의
sc = preprocessing.StandardScaler()
# 데이터를 표준화
sc.fit(X_train)
X_train_std = sc.transform(X_train)
sc.fit(X_test)
X_test_std = sc.transform(X_test)

# 머신러닝 기법 적용
clf_ = linear_model.Ridge() # 91%

# 학습 
clf_.fit(X_train, y_train)
y_pred  = clf_.predict(X_test)


# 학습정확도 확인
print('Mean Squared Error :',mean_squared_error(y_test,y_pred))
print('Mean Absolute Error :',mean_absolute_error(y_test,y_pred))
print("train 학습 정확도 :", clf_.score(X_train, y_train)) 
print("test 학습 정확도 :", clf_.score(X_test, y_test)) 

