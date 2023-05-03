import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_excel('./dat/Ver6.xlsx')  # excel file 불러오기
df.drop(['No',' X Index',' Y Index',' X Size',' Y Size'],axis=1,inplace=True) #불필요한 column 지우기
df['PL JudgeType'].unique()  # PL JudgeType을 고유값으로 설정

P0 = (7E-12 * df[' PL_Sum']-2.5E-7)

#print(P0)
print(df[' PL_Sum'])
#plt.plot(df[' PL_Sum'],P0)
#plt.show()