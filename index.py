import pandas as pd

filepath = './data/Knee.csv'
knee = pd.read_csv(filepath)
knee.info()