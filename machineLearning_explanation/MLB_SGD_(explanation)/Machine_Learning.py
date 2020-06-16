# import necessary libraries
import warnings
warnings.filterwarnings("ignore")
from random import seed
from random import randrange
from csv import reader
from math import sqrt
import pandas as pd
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from prettytable import PrettyTable

from sklearn import preprocessing
from sklearn import linear_model
from sklearn.linear_model import SGDRegressor
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error,mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import RANSACRegressor
from sklearn.linear_model import LinearRegression
import mglearn

from subplot import make_plot

b_total=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/b_total_no_scale.csv')
p_total=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/p_total_no_scale.csv')
# 순위
r=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/bat_r.csv')

# 2010~2018년 데이터 & 2019년 데이터
bat_total_2010_2018=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/bat_total_2010_2018.csv')
bat_total_2019=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/bat_total_2019.csv')
r_total_2010_2018=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/r_2010_2018.csv')
r_total_2019=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/r_2019.csv')


# 타자, 투수 지표
p_corr=p_total[['IP','K','ERA','WHIP']]
b_corr=b_total[['R','H','2B','HR','RBI','SF','OPS','BB']]
# b_corr=b_total[['H','R','AVG','SO','HBP','SF','SB','TH','2B','3B','HR','RBI','OPS']]

# 승률
rank_PCT=r[['R']]

# y = 득점, X = 투수지표
# y=rank_PCT; X=b_corr

# scatter로 확인
make_plot()

# train 데이터와 test 데이터 정의 및 분리
# X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,shuffle=False)
X_train=bat_total_2010_2018[['R','H','2B','HR','RBI','SF','OPS','BB']]
X_test=bat_total_2019[['R','H','2B','HR','RBI','SF','OPS','BB']]
y_train=r_total_2010_2018[['R']]
y_test=r_total_2019[['R']]

# # 표준화 함수 정의
# sc = preprocessing.StandardScaler()
# # 데이터를 표준화
# sc.fit(X_train)
# X_train_std = sc.transform(X_train)
# sc.fit(X_test)
# X_test_std = sc.transform(X_test)

# clf_ = linear_model.LinearRegression(normalize=True) # 89%
clf_ = linear_model.Ridge() # 91%
# clf_ = linear_model.LassoLars(alpha=.1) #87%
# clf_ = RANSACRegressor(random_state=None) #85%
# clf_ = linear_model.MultiTaskLasso(alpha=0.1, random_state=None) #88%
# clf_ = KNeighborsRegressor(n_neighbors=15) 70%
# clf_ = linear_model.Lasso(alpha=0.1,max_iter=5000) 88%
    
# 학습 
clf_.fit(X_train, y_train)
y_pred  = clf_.predict(X_test)
print(clf_.coef_)
print(clf_.intercept_)

# # scatter 함수 구현
# plt.scatter(X_train.R,y_train)
# plt.grid()
# plt.xlabel('Actual X')
# plt.ylabel('Predicted y')
# plt.title('scatter plot between actual y and predicted y')
# plt.tight_layout()
# plt.show()

# 학습정확도 확인
print('Mean Squared Error :',mean_squared_error(y_test,y_pred))
print('Mean Absolute Error :',mean_absolute_error(y_test,y_pred))
print("train 학습 정확도 :", clf_.score(X_train, y_train)) 
print("test 학습 정확도 :", clf_.score(X_test, y_test)) 

# y=17.0871797*'R'-6.38402358*'H' -9.03972435*'2B' -18.60040656*'3B' -15.98107795*'HR' 1.71235341*'RBI' 3.43366458*'SF' 627.58482031*'OPS' + 153.42452726
y=(17.0871797*45.294118)+(-6.38402358*49.058824)+ (-9.03972435*16.294118)+ (-18.60040656*2.176471)+ (-15.98107795*12.588235)+ (1.71235341*43.705882) \
    +(3.43366458*2.235294) +(627.58482031*0.742824) + 153.42452726
print(y)

