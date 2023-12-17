# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

# моя версия

# data = pd.DataFrame({'robot': lst, 'human': lst})
# data = data.replace({'robot': {'robot': 1, 'human': 0}, 'human': {'robot': 0, 'human': 1}})

# версия через get_dummies

data = pd.get_dummies(data['whoAmI'])
data = data.replace({True: 1, False: 0})

# какая-то непонятная версия с интернет ресурса (не понял как работает)

# data['tmp'] = 1
# data.set_index([data.index, 'whoAmI'], inplace=True)
# data = data.unstack(level=-1, fill_value=0).astype(int)
# data.columns = data.columns.droplevel()
# data.columns.name = None

print(data)
