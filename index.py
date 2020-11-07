import pandas as pd

filepath = './data/Knee.csv'
col_names = ['Below Average', 'Average', 'Above Average']
knee = pd.read_csv(filepath, header = None, names = col_names)
print(knee.iloc[0: , :])

out_csv = 'new_knee'
knee.to_csv(out_csv)