from csv import reader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from prettytable import PrettyTable

Precision=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/Precision.csv')
# print(type(Precision['Team']))
# print(Precision['Team'])
Team=Precision['Team']
Predict=Precision["Predict"]
Condition=Precision['Condition']
min1=Precision['Min']
max1=Precision['Max']
max_min=max1-min1
accuracy1=Precision['Accuracy']
Accuracy=[]
for i in accuracy1:
    if i=="False":
        Accuracy.append(0.88)
    else:
        Accuracy.append(round(float(i),2))

df = Precision[['Team', 'Predict', 'Condition','Error','Min','Max']]
df1=df.set_index('Team')

# df1.plot.area(stacked=False, figsize=(18,10),grid=True,use_index=True)
# plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29])
# plt.xlim([1,29])

plt.figure(figsize=(20,10))

plt.subplot(2,1,1)
plt.plot(Team,Predict,linewidth=1, ls="dashed",color='g')
plt.plot(Team,Condition,linewidth=1,color="#BDC7EC")
plt.text(0.3, Condition[0]+50, s='Condition', fontsize=10, horizontalalignment='center', verticalalignment='center', bbox=dict(facecolor='#BDC7EC', alpha=0.5))
plt.text(0.3, Predict[0]+55, s='Predict', fontsize=10, horizontalalignment='center', verticalalignment='center', bbox=dict(facecolor='g', alpha=0.5))
plt.title("Precision & Condition")
plt.xlabel("Team")
plt.ylabel("Run scored")

plt.subplot(2,1,2)
plt.plot(Team,max1,'g',linewidth=0.5,ls="dashed")
plt.plot(Team,min1,'g',linewidth=0.5,ls="dashed")
plt.plot(Team,Condition,linewidth=2,color="#0A30BD")
plt.text(0, max1[0]+40, s='Max', fontsize=10, horizontalalignment='center', verticalalignment='center', bbox=dict(facecolor='#BDDAEC', alpha=0.5))
plt.text(0, Condition[0]+40, s='Condition', fontsize=10, horizontalalignment='center', verticalalignment='center', bbox=dict(facecolor='b', alpha=0.5))
plt.text(0, min1[0]+40, s='Min', fontsize=10, horizontalalignment='center', verticalalignment='center', bbox=dict(facecolor='#BDDAEC', alpha=0.5))
plt.title("Range of MinMax")
plt.xlabel("Team")
plt.ylabel("Run scored")
plt.fill_between(Team, min1, max1, color="#BDC7EC")  

plt.tight_layout()
plt.show()

