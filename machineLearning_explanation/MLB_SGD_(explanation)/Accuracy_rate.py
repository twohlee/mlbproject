from csv import reader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from prettytable import PrettyTable


# Prepare Data

Precision=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/Precision.csv')
# print(type(Precision['Team']))
# print(Precision['Team'])
Team=Precision['Team']
accuracy1=Precision['Accuracy']
Accuracy=[]
for i in accuracy1:
    if i=="False":
        Accuracy.append(0.88)
    else:
        Accuracy.append(round(float(i),2))

# df.sort_values('cty', inplace=True)
# df.reset_index(inplace=True)

# Draw plot
fig, ax = plt.subplots(figsize=(16,10), dpi= 80)
ax.vlines(x=Precision.Team, ymin=0, ymax=Accuracy,color='firebrick', alpha=0.7, linewidth=2)
ax.scatter(x=Precision.Team, y=Accuracy, s=75, color='firebrick', alpha=0.7)

# Title, Label, Ticks and Ylim
ax.set_title('Accuracy per MLB_Teams by modeling', fontdict={'size':22})
ax.set_ylabel('Accuracy')
ax.set_xticks(Precision.index)
# ax.set_xticklabels(df.manufacturer.str.upper(), rotation=60, fontdict={'horizontalalignment': 'right', 'size':12})
ax.set_ylim(0.85,1.01)

# Annotate
x=[]
for i in range(0,30):
    x.append(i)

for i in range(0,30):
    ax.text(x[i], Accuracy[i]+.001, s=Accuracy[i], horizontalalignment= 'center', verticalalignment='bottom', fontsize=10)
    print(Accuracy[i])
plt.show()
