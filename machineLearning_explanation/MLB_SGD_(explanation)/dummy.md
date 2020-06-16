from prettytable import PrettyTable
from sklearn import preprocessing
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

bat_total=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/real_bat_total.csv')
pit_total=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/real_pit_total.csv')
rank_total=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/rank_good.csv')
b_total=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/b_total_no_scale.csv')
p_total=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/p_total_no_scale.csv')
r=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/bat_r.csv')

p_corr=p_total[['IP','K','ERA','WHIP']]
b_corr=b_total[['R','H','2B','3B','HR','RBI','SF','OPS']]

# 승률
rank_PCT=r[['R']]

# y = 승률, X = 투수지표
def make_plot():
    y=rank_PCT; X=b_corr
    # SPLIT
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,shuffle=False)
    plt.figure(figsize=(15,8))

    plt.subplot(3,3,1)
    plt.scatter(X_train.R,y_train, c='b', s=12)
    plt.title("R")

    # plt.subplot(3,3,2)
    # plt.scatter(X_train.H,y_train)

    plt.subplot(3,3,3)
    plt.scatter(X_train['2B'],y_train, c='r', s=12)
    plt.title("2B")
    plt.subplot(3,3,4)
    plt.scatter(X_train.HR,y_train, c='k', s=12)
    plt.title("HR")

    # plt.subplot(3,3,5)
    # plt.scatter(X_train['3B'],y_train, c='y', s=12)
    # plt.subplot(3,3,6)
    # plt.scatter(X_train.HR,y_train, c='c', s=12)

    plt.subplot(3,3,7)
    plt.scatter(X_train.RBI,y_train, c='g', s=12)
    plt.title("RBI")

    plt.subplot(3,3,8)
    plt.scatter(X_train.SF,y_train, c='m', s=12)
    plt.title("SF")

    plt.subplot(3,3,9)
    plt.scatter(X_train.OPS, y_train ,c='b', s=12)
    plt.title("OPS")

    plt.tight_layout()
    plt.show()