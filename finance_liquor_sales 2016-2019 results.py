
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("finance_liquor_sales 2016-2019.csv")
f = data.groupby('zip_code').bottles_sold.sum()
import numpy as np
colors = np.random.randint(47, size=(47))

plt.scatter(f.index, f, c=colors)
plt.xlabel('zip code')
plt.xticks()
plt.ylabel('Bottles sold')
plt.title ('Bottles Sold')
plt.show()


