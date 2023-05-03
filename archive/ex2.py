import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns
import numpy as np

df = pd.read_excel('./dat/Ver6.xlsx')
df.drop(['No',' X Index',' Y Index',' X Size',' Y Size'],axis=1,inplace=True)

df['PL JudgeType'].unique()  #array(['PL OK', 'PL NG'], dtype=object)


for i in range(0,7590):
    if df.loc[i,'PL JudgeType'] == 'PL OK':
        df.loc[i,'PL JudgeType'] = 1
    else:
        df.loc[i,'PL JudgeType'] = 0

for i in range(0,7590):
    if df.loc[i,'Itself Judge'] == 'EL OK':
        df.loc[i,'Itself Judge'] = 1
        df.loc[i,'Error flag'] = 'No error'
    else:
        df.loc[i,'Error flag'] = df.loc[i,'Itself Judge']
        df.loc[i,'Itself Judge'] = 0
     
df_1 = pd.read_excel('./dat/Ver6.xlsx')
df_1.drop(['No',' X Index',' Y Index',' X Size',' Y Size',' PL_Min Value'],axis=1,inplace=True)

df_1['PL JudgeType'].unique()  #array(['PL OK', 'PL NG'], dtype=object)


for i in range(0,7590):
    if df_1.loc[i,'PL JudgeType'] == 'PL OK':
        df_1.loc[i,'PL JudgeType'] = 1
    else:
        df_1.loc[i,'PL JudgeType'] = 0

for i in range(0,7590):
    if df_1.loc[i,'Itself Judge'] == 'EL OK':
        df_1.loc[i,'Itself Judge'] = 1
    else:
        df_1.loc[i,'Itself Judge'] = 0




'''col = ['PL JudgeType']
col1 = [' PL_Sum']
col2 = ['EL_PO-Top(W)']
a = df[col1]
plt.plot(a,a)
plt.show()'''

sns.set(style='whitegrid')
sns.pairplot(df_1[[' PL_Sum','EL_PO-Top(W)']])
plt.show()

cols = [' PL_Sum','EL_PO-Top(W)']
corr = df_1[cols].corr(method = 'pearson')

corr.values
column_names = [' PL_Sum','EL_PO-Top(W)']
sns.set(font_scale=1,rc={"axes.unicode_minus":False})
plt.figure(figsize = (13,10))
hm = sns.heatmap(corr.values, #데이터
            cbar=True, #오른쪽 컬러 막대 출력 여부
            annot=True, #차트에 숫자를 보여줄 것인지 여부
            square=True, #차트를 정사각형으로 할 것인지
            fmt='.2f', #숫자의 출력 소수점 자리 개수 조절
            annot_kws={'size': 15}, #숫자 출력 시 숫자 크기 조절
            yticklabels=column_names, #y축에 컬럼명 출력
            xticklabels=column_names, #x축에 컬럼명 출력
            cmap="RdYlGn") 
plt.tight_layout()
plt.show()