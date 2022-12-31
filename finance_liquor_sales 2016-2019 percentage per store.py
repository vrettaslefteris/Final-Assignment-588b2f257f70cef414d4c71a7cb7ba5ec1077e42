import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("finance_liquor_sales 2016-2019.csv")
df1 = pd.DataFrame(data, columns=['store_number', 'sale_dollars'])
df1['percent'] = (df1['sale_dollars'] / df1['sale_dollars'].sum()) * 100

print(df1)

df1.groupby(['store_number']).sum().plot(
kind='pie', y='sale_dollars', autopct='%1.1f%%')
plt.legend(loc='lower right', ncol=1)
plt.show()


