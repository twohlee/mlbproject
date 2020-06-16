from csv import reader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from prettytable import PrettyTable

# 데이터 로드
y_60_70=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/y_60_70.csv')
Precision=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/Precision.csv')

# 변수 정의
Team=Precision['Team']
Predict=Precision["Predict"]
Condition=Precision['Condition']
min1=Precision['Min']
max1=Precision['Max']
max_min=max1-min1
accuracy1=Precision['Accuracy']

y_60=y_60_70['y_60']
y_70=y_60_70['y_70']

Accuracy=[]
for i in accuracy1:
    if i=="False":
        Accuracy.append(0.88)
    else:
        Accuracy.append(round(float(i),2))

df = Precision[['Team', 'Predict', 'Condition','Error','Min','Max']]
df1=df.set_index('Team')

# 함수 구현

plt.figure(figsize=(20,10))

plt.subplot(3,1,1)
plt.plot(Team,y_60*0.6,'g',linewidth=0.5,ls="dashed",color="#0A30BD")
plt.plot(Team,y_60*1.4,'g',linewidth=0.5,ls="dashed",color="#0A30BD")
plt.plot(Team,Condition,linewidth=2,color="#0A30BD")
plt.fill_between(Team, y_60*0.6, y_60*1.4, color="#BDC7EC") 
plt.text(0.3, y_60[0]*0.6+50, s='Accuracy 60% Min Value', fontsize=10, horizontalalignment='center', verticalalignment='center', bbox=dict(facecolor='#BDC7EC', alpha=0.5))
plt.text(0.3, Condition[0]+70, s='Condition', fontsize=10, horizontalalignment='center', verticalalignment='center', bbox=dict(facecolor='b', alpha=0.5))
plt.text(0.3, y_60[0]*1.4+55, s='Accuracy 60% Max Value', fontsize=10, horizontalalignment='center', verticalalignment='center', bbox=dict(facecolor='#BDC7EC', alpha=0.5))
plt.title("Accuracy of Precision 60%")
plt.xlabel("Team")

plt.subplot(3,1,2)
plt.plot(Team,y_70*0.7,'g',linewidth=0.5,ls="dashed",color="#0A30BD")
plt.plot(Team,y_70*1.3,'g',linewidth=0.5,ls="dashed",color="#0A30BD")
plt.plot(Team,Condition,linewidth=2,color="#0A30BD")
plt.fill_between(Team, y_70*0.7, y_70*1.3, color="#BDC7EC") 
plt.text(0.3, y_70[0]*0.7+50, s='Accuracy 70% Min Value', fontsize=10, horizontalalignment='center', verticalalignment='center', bbox=dict(facecolor='#BDC7EC', alpha=0.5))
plt.text(0.3, Condition[0]+70, s='Condition', fontsize=10, horizontalalignment='center', verticalalignment='center', bbox=dict(facecolor='b', alpha=0.5))
plt.text(0.3, y_70[0]*1.3+55, s='Accuracy 70% Max Value', fontsize=10, horizontalalignment='center', verticalalignment='center', bbox=dict(facecolor='#BDC7EC', alpha=0.5))
plt.title("Accuracy of Precision 70%")
plt.xlabel("Team")

plt.subplot(3,1,3)
plt.plot(Team,max1,'g',linewidth=0.5,ls="dashed",color="#0A30BD")
plt.plot(Team,min1,'g',linewidth=0.5,ls="dashed",color="#0A30BD")
plt.plot(Team,Condition,linewidth=2,color="#0A30BD")
plt.text(0.3, max1[0]*0.9+150, s='Accuracy 91% Max Value', fontsize=10, horizontalalignment='center', verticalalignment='center', bbox=dict(facecolor='#BDC7EC', alpha=0.5))
plt.text(0.3, Condition[0]+50, s='Condition', fontsize=10, horizontalalignment='center', verticalalignment='center', bbox=dict(facecolor='b', alpha=0.5))
plt.text(0.3, min1[0]*1.1-100, s='Accuracy 91% Min Value', fontsize=10, horizontalalignment='center', verticalalignment='center', bbox=dict(facecolor='#BDC7EC', alpha=0.5))
plt.title("Accuracy of Precision 91%")
plt.xlabel("Team")
plt.fill_between(Team, min1, max1, color="#BDC7EC") 

plt.tight_layout()
plt.show()

