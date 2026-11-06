import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib as mpl
mpl.rcParams["figure.figsize"] = [20, 10]

# Loading the dataset with the corrected filename
df1 = pd.read_csv("/content/Bengaluru_House_Data.csv")
df1.head()