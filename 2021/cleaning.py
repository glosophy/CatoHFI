import pandas as pd
import os
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

cwd = os.getcwd()
print(cwd)

df = pd.read_excel(cwd + '/' + 'HFI 2021 - FINALg.xlsx')