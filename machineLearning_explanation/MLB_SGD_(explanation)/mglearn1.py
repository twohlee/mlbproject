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

from mglearn.plot_helpers import cm2
from mglearn.datasets import make_wave
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

bat_total=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/real_bat_total.csv')
pit_total=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/pit_total.csv')
rank_total=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/rank_good.csv')
b_total=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/b_total_no_scale.csv')
p_total=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/p_total_no_scale.csv')
r=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/bat_r.csv')
line=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/line.csv')

del pit_total['Unnamed: 0']
# del bat_total['Unnamed: 0']
del b_total['Unnamed: 0']
del p_total['Unnamed: 0']

p_corr=p_total[['IP','K','ERA','WHIP']]
# b_corr=b_total[['R','H','2B','3B','HR','RBI','SF','OPS']]
b_corr=b_total[['R']]
line1=line[['RBI','R']]
line2=line1.to_numpy()
rank_PCT=r[['R']]
# print(line2)
def plot_linear_regression_wave():
    y=rank_PCT; X=b_corr
    # X , y = line2()

    # X, y = make_wave(n_samples=60)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=None)

    print(X_train)
    line = np.linspace(-3, 3, 100).reshape(-1, 1)

    lr = LinearRegression().fit(X_train, y_train)
    # print("w[0]: %f  b: %f" % (lr.coef_[0], lr.intercept_))

    plt.figure(figsize=(8, 8))
    # plt.plot(line, lr.predict(line))
    plt.plot(line, lr.predict(line))
    plt.plot(X_train, y_train, 'o')
    # ax = plt.gca()
    # ax.spines['left'].set_position('center')
    # ax.spines['right'].set_color('none')
    # ax.spines['bottom'].set_position('center')
    # ax.spines['top'].set_color('none')
    # ax.set_ylim(-3, 3)
    #ax.set_xlabel("Feature")
    #ax.set_ylabel("Target")
    # ax.legend(["model", "training data"], loc="best")
    # ax.grid(True)
    # ax.set_aspect('equal')
    plt.show()

plot_linear_regression_wave()   