from prettytable import PrettyTable
from sklearn import preprocessing
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기
bat_total=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/real_bat_total.csv')
r=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/bat_r.csv')

b_corr=bat_total[['R','H','2B','HR','RBI','SF','OPS','BB']]

# 승률
rank_PCT=r[["R"]]

def make_plot():
    y=rank_PCT; X=b_corr
    # SPLIT
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,shuffle=False)
    plt.figure(figsize=(15,8))

    plt.subplot(3,3,1)
    sns.set_palette('pastel')
    sns.regplot(x=X_train.R, y=y_train['R'], color='#e5b343', ci=20, logx=True,scatter_kws={'s':15}) 
    plt.title('corrcoef of R')

    plt.subplot(3,3,2)
    sns.regplot(x=X_train.H, y=y_train['R'], color='#077284', ci=2, logx=True,scatter_kws={'s':15})
    plt.title('corrcoef of H')

    plt.subplot(3,3,3)
    sns.regplot(x=X_train['2B'], y=y_train['R'], color='#77a380', ci=2, logx=True,scatter_kws={'s':15})
    plt.title('corrcoef of 2B')

    plt.subplot(3,3,4)
    sns.regplot(x=X_train.BB, y=y_train['R'], color='#665326', ci=2, logx=True,scatter_kws={'s':15})
    plt.title('corrcoef of BB')

    plt.subplot(3,3,5)
    sns.regplot(x=X_train.HR, y=y_train['R'], color='#618728', ci=2, logx=True,scatter_kws={'s':15})
    plt.title('corrcoef of HR')

    plt.subplot(3,3,6)
    sns.regplot(x=X_train.RBI, y=y_train['R'], color='#f77388', ci=2, logx=True,scatter_kws={'s':15})
    plt.title('corrcoef of RBI')

    plt.subplot(3,3,7)
    sns.regplot(x=X_train.SF, y=y_train['R'], color='#803387', ci=2, logx=True,scatter_kws={'s':15})
    plt.title('corrcoef of SF')

    plt.subplot(3,3,8)
    sns.regplot(x=X_train.OPS, y=y_train['R'], color='#bc3f3e', ci=2, logx=True,scatter_kws={'s':15})
    plt.title('corrcoef of OPS')

    plt.tight_layout()

    plt.show()
