import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from pandas import DataFrame


index = ['1',
'2',
'3',
'4',
'5',
'6',
'7',
'8',
'9',
'10',
'11',
'12',
'13']
columns = ['MATLAB-Octave - 1',
'DeepSqueak - 2',
'ccodashboard - 3',
'TIGRE - 4',
'bids-starter-kit - 5',
'ffcc - 6',
'MBeautifier - 7',
'plotly-library - 8',
'cobratoolbox - 9',
'machine-learning - 10',
'fieldtrip - 11',
'yang_vocoder - 12',
'Kilosort - 13']

testdict = {
    "MATLAB-Octave - 1": [0,86,30,98,80,72,98,98,98,97,97,72,99],
    "DeepSqueak - 2": [86,0,28,84,75,69,84,85,84,85,84,69,86],
    "ccodashboard - 3": [30,28,0,27,28,25,27,26,27,27,26,25,28],
    "TIGRE - 4": [98,84,27,0,79,70,100,99,100,95,100,70,98],
    "bids-starter-kit - 5": [80,75,28,79,0,66,79,79,79,78,78,66,79],
    "ffcc - 6": [72,69,25,70,66,0,70,71,70,68,70,100,72],
    "MBeautifier - 7": [98,84,27,100,79,70,0,99,100,95,100,70,98],
    "plotly-library - 8": [98,85,26,99,79,71,99,0,99,96,99,71,98],
    "cobratoolbox - 9": [98,84,27,100,79,70,100,99,0,95,99,70,98],
    "machine-learning - 10": [97,85,27,95,78,68,95,96,95,0,95,68,97],
    "fieldtrip - 11": [97,84,26,100,78,70,100,99,99,95,0,70,98],
    "yang_vocoder - 12": [72,69,25,70,66,100,70,71,70,68,70,0,72],
    "Kilosort - 13": [99,86,28,98,79,72,98,98,98,97,98,72,0],

}
df = pd.DataFrame(testdict, index=index, columns=columns)
#df = Teste.append(a).append(b)
df = df.transpose()

sns.heatmap(df,annot=True,cmap='Blues', fmt='g')
#print(df)
#plt.pcolor(df)
#plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
#plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns)
plt.show()