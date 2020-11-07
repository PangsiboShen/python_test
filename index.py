import pandas as pd
import matplotlib.pyplot as plt

filepath = './data/Knee.csv'
col_names = ['Below Average', 'Average', 'Above Average']
knee = pd.read_csv(filepath, header = 0, names = col_names)
print(knee.iloc[0: , :])

out_csv = 'new_knee'
knee.to_csv(out_csv)

col_1 = knee['Below Average'].values
plt.plot(col_1)
plt.show()