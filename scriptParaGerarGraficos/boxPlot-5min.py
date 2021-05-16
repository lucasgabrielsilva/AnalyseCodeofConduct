import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
 
# Dataset:
MATLAB = pd.DataFrame({ 'Linguagem de Programação' : np.repeat('MATLAB', 13), 'Quantidade de Palavras': (463,
698,
39,
446,
688,
443,
446,
446,
450,
363,
448,
443,
461)
})
Julia = pd.DataFrame({ 'Linguagem de Programação' : np.repeat('Julia', 16), 'Quantidade de Palavras': (374,
374,
374,
374,
39,
712,
446,
374,
374,
452,
374,
445,
374,
374,
319,
446)
})
Clojure = pd.DataFrame({ 'Linguagem de Programação' : np.repeat('Clojure', 22), 'Quantidade de Palavras': (461,
186,
460,
448,
580,
712,
446,
443,
461,
446,
761,
461,
447,
710,
580,
461,
37,
710,
64,
698,
225,
446)
})
Perl = pd.DataFrame({ 'Linguagem de Programação' : np.repeat('Perl', 25), 'Quantidade de Palavras': (176,
467,
69,
461,
710,
39,
446,
461,
461,
446,
456,
461,
461,
459,
461,
9,
186,
461,
446,
108,
24,
463,
38,
463,
21)
})
ObjectiveC = pd.DataFrame({ 'Linguagem de Programação' : np.repeat('Objective-C', 40), 'Quantidade de Palavras': (322,
443,
446,
462,
710,
219,
446,
463,
461,
461,
764,
1059,
37,
446,
446,
37,
446,
37,
39,
866,
462,
446,
37,
446,
666,
462,
461,
446,
461,
39,
462,
443,
37,
443,
8,
446,
446,
461,
324,
461)
})

df=MATLAB.append(Julia).append(Clojure).append(Perl).append(ObjectiveC)

# boxplot
ax = sns.boxplot(x='Linguagem de Programação', y='Quantidade de Palavras', data=df)
# add stripplot
ax = sns.stripplot(x='Linguagem de Programação', y='Quantidade de Palavras', data=df, color="orange", jitter=0.2, size=2.5)

# add title
plt.title("Boxplot da contagem de palavras das 5 linguagens de programação com menos códigos de conduta", loc="left")

# show the graph
plt.show()