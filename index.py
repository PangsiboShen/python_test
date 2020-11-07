import pandas as pd
import matplotlib.pyplot as plt

filepath = './data/Knee.csv'
col_names = ['Below Average', 'Average', 'Above Average']
knee = pd.read_csv(filepath, header = 0, names = col_names)
print(knee.iloc[0: , :])

out_csv = 'new_knee'
knee.to_csv(out_csv)
knee_df = pd.DataFrame(knee)

knee_df.plot(subplots = True)
plt.ylabel("days")
plt.xlabel('counts')
plt.title('Distribution of Days needed to recover')
plt.show()
plt.savefig('knee.pdf')