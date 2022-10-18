import pandas as pd
import numpy as np

# 載入資料集
df = pd.read_csv('./train.csv')
# unique 是列出每個不一樣的值，以列的形式表示，size是查看該列表的數量
df = df.set_index('PassengerId')
# 當 Sex 值為 female 則設為 1，反之為 0
df['SexCode'] = np.where(df['Sex'] == 'female', 1, 0)
# 在顯示資料的欄位資訊時我們有發現有些欄位有缺值，我們進一步使用 isnull() 方法來檢視：

print(df.isnull().sum())
print(df['Age'].isnull().sum())
avg_age = df['Age'].mean()
# 發現 Age 有 177 個缺值，Cabin 有 687，Embarked 有 2。其中 Age 我們可以使用現有資料的年齡平均數來補齊，讓資料分析更為方便。
df['Age'] = df['Age'].fillna(avg_age)
print(df['Age'].isnull().sum())

# 根據性別進行年齡的統計：
print(df.groupby('Sex')['Age'].size())
print(df.groupby('Sex')['Age'].mean())



