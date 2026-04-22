import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_csv(r'data\bird-neck-bones.csv')
data = data.groupby('species').mean().reset_index()
data.plot.bar('species','neck_vertebrae')
plt.ylabel('Neck Vertebrae')
plt.show()