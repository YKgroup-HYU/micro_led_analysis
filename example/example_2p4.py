# 2.4.1
import numpy as np
import pandas as pd





# 2.4.3
cols = ['국어','수학','영어','과학','사회']
lists = [[83,68,92,55,85],[40,95,64,87,77],[65,87,58,92,72]]
indexes=['태현','준수','기준']
dfs=pd.DataFrame(lists,columns=cols,index=indexes)
print(dfs)
