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
import pickle



#=====================================step1
# 전체 타자 데이터
bat_total=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/real_bat_total.csv')
# 전체 투수 데이터
pit_total=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/real_pit_total.csv')
# 전체 랭크 데이터
rank_total=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/rank_good.csv')
# 10년치 팀 평균(타자)
# R, 2B, HR, RBI, BB, SF, OBP, SLG, OPS 사용
b_total=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/b_total_no_scale.csv')
# 10년치 팀 평균(투수)
# IP, K, ERA, WHIP 사용
p_total=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/p_total_no_scale.csv')
# 득점률/방어율
r=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/bat_r.csv')


# 타자, 투수 지표
p_corr=p_total[['IP','K','ERA','WHIP']]
b_corr=b_total[['R','H','2B','HR','RBI','SF','OPS','BB']]

# 승률
rank_PCT=r[['R']]

# y = 승률, X = 투수지표
y=rank_PCT; X=b_corr

# ====================================step2
# scatter로 확인
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

# clf_ = linear_model.LinearRegression(normalize=False) # 0.89
clf_ = linear_model.Ridge(alpha=0.09) # 0.88
# clf_ = linear_model.LassoLars(alpha=.1) #0.87
# clf_ = RANSACRegressor(random_state=None) #0.85
# clf_ = linear_model.MultiTaskLasso(alpha=0.1, random_state=None) #0.886
# clf_ = KNeighborsRegressor(n_neighbors=15) 0.70
# clf_ = linear_model.Lasso(alpha=0.1,max_iter=5000) 0.88

# 학습 
print(X_train.R)
clf_.fit(X_train, y_train)
y_pred  = clf_.predict(X_test)

# scatter 함수 구현
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
# print(clf_.coef_)
# print(clf_.intercept_)


with open('./bs.dat', 'wb') as fp:
    pickle.dump(sc, fp)
    pickle.dump(clf_, fp)

# ==========================================step3
with open('./bs.dat', 'rb') as fp:
    sc = pickle.load(fp)
    clf_ = pickle.load(fp)


#X = [[100, 161, 29, 44, 97, 3,  1.1, 80]]
X = [[97.1,151.1, 32.3, 35.5,101,5.1, 0.9656 , 75.9]] 

# Yelich [100, 161, 29, 44, 97, 3,  1.1, 80]
# Bellinger [121, 170, 34, 47, 115, 4, 1.035, 95]
# Trout [110, 137, 27, 45, 104, 4, 1.083, 110]
# 이대호 [33, 74, 9, 14, 49, 0, 0.740, 20]
# 강정호 [45, 81, 19, 21, 62, 2, 0.867, 36]
# 김현수 [36, 92, 16, 6, 22, 1, 0.801, 36]

# R                97.100000
# H               151.100000
# 2B               32.300000
# HR               35.500000
# RBI             101.000000
# SF                5.100000
# OPS               0.965600
# BB               75.900000



X_std = sc.transform(X)
    # 결과를 추출한다

y_pred = clf_.predict(X_std)
print("★ 예상 총 득점수는 ★")
print(y_pred)


