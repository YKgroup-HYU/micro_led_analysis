import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_excel('./dat/Ver6.xlsx')  # excel file 불러오기
df.drop(['No',' X Index',' Y Index',' X Size',' Y Size'],axis=1,inplace=True) #불필요한 column 지우기
df['PL JudgeType'].unique()  # PL JudgeType을 고유값으로 설정

P0 = (7E-12 * df[' PL_Sum']-2.5E-7)

a = []
b = []
for i in range(0,7590):
    if 1.2E-6 > P0[i] > 0.4E-6 :
        a.append(P0[i])
        b.append(df['EL_PO-Top(W)'][i])
        

print(P0)
print(a)
print(df[' PL_Sum'])
plt.scatter(a,b)
plt.show()