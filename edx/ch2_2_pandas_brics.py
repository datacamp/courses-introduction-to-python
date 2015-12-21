import pandas as pd

data = [['Brazil',200,8515767,'Brasilia'],
['Russia',144,17098242,'Moscow'],
['India',1252,3287590,'New Dehli'],
['China',1357,9596961,'Bejing'],
['South Africa',55,1221037,'Pretoria']]

columns = ['country','population','area','capital']
index = ['BR','RU','IN','CH','SA']

path = "~/courses/courses-intermediate-python/edx/brics.csv"

pd.DataFrame(data=data,columns=columns,index=index).to_csv(path)
brics = pd.read_csv(path, index_col = 0)
print(df.to_dict())



dict = {
    'area': [8515767, 17098242, 3287590, 9596961, 1221037],
    'capital': ['Brasilia', 'Moscow', 'New Dehli', 'Bejing', 'Pretoria'],
    'country': ['Brazil', 'Russia', 'India', 'China', 'South Africa'],
    'population': [200, 144, 1252, 1357, 55]
}

df2 = pd.DataFrame(dict)
