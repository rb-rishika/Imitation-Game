import csv
import pandas as pd
import os
import numpy as np

result = pd.read_csv(r'C:\Users\ruchi\Downloads\AGENTONE\ActualGrid.txt',sep= '[\t, \n]')

res=result.T

#res.index = np.arange(1, len(result)+1)
res.to_csv(r'C:\Users\ruchi\Downloads\AGENTONE\ActualGrid.csv', header=False)

print (result)

