# 2.4.1
import numpy as np
import pandas as pd
list1 = [1, 2, 3]
df_list1 = pd.DataFrame(list1, columns=['col'])
print(df_list1)
array1 = np.array([1, 2, 3])
df_array1 = pd.DataFrame(array1, columns=['col'])
print(df_array1)

# 2.4.2
cols = ['col1','col2','col3']
list2 = [[1,2,3],[11,12,13]]
df_list2 = pd.DataFrame(list2,columns=cols)
print(df_list2)


# 2.4.3
cols = ['국어','수학','영어','과학','사회']
lists = [[83,68,92,55,85],[40,95,64,87,77],[65,87,58,92,72]]
indexes=['태현','준수','기준']
dfs=pd.DataFrame(lists,columns=cols,index=indexes)
print(dfs)
