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




cols = ['PL JudgeType',' PL_Sum','PL_Average','PL_Max Value','EL_PW','EL_PI','EL_DW','EL_II','EL_FWHM','EL_IR(A)','EL_VR(V)','EL_VF1(V)','EL_VF2(V)','EL_VF3(V)','EL_PO-Top(W)','Itself Judge']
corr = df_1[cols].corr(method = 'pearson')

corr.values
column_names = ['PL JudgeType',' PL_Sum','PL_Average','PL_Max Value','EL_PW','EL_PI','EL_DW','EL_II','EL_FWHM','EL_IR(A)','EL_VR(V)','EL_VF1(V)','EL_VF2(V)','EL_VF3(V)','EL_PO-Top(W)','Itselff Judge']
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

'''sns.set(style='whitegrid')
sns.pairplot(df_1[['PL JudgeType',' PL_Sum','PL_Average','PL_Max Value','EL_PW','EL_PI','EL_DW','EL_II','EL_FWHM','EL_IR(A)','EL_VR(V)','EL_VF1(V)','EL_VF2(V)','EL_VF3(V)','EL_PO-Top(W)','Itself Judge']])
plt.show()'''

corr_feature =df_1[cols].corr()
fig = plt.figure(figsize=(20,20))

n_feature = len(cols)
for i in range(n_feature):
    for j in range(n_feature):
        ax = fig.add_subplot(n_feature,n_feature,i*n_feature + j + 1)
        plt.scatter(cols[j],cols[i], data=df_1, s=9)

        if i == n_feature-1:
            plt.xlabel(cols[j],fontsize=12)
        if j == 0:
            plt.ylabel(cols[i], fontsize=12)
        ax.annotate(np.round(corr_feature[cols[i],cols[j]],3),xy=(1,0),
                    xycoords='axes fraction', fontsize =16,
                    horizontalalignment='right', verticalalignment='bottom')

plt.show()