import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_csv(r'data\bird-neck-bones.csv')
plt.plot(data['species'],data['neck_vertebrae'])
plt.show()