import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib as mpl
mpl.rcParams["figure.figsize"] = [20, 10]

# Loading the dataset with the corrected filename
df1 = pd.read_csv("Bengaluru_House_Data.csv")
print(df1.head())

print(df1.shape)

print(df1.groupby('area_type')['area_type'].agg('count'))
