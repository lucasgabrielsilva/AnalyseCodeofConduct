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
Kotlin = pd.DataFrame({ 'Linguagem de Programação' : np.repeat('Kotlin', 68), 'Quantidade de Palavras': (446,
462,
461,
710,
74,
28,
446,
447,
464,
461,
72,
219,
443,
766,
28,
461,
737,
446,
28,
461,
446,
446,
446,
28,
446,
464,
446,
446,
710,
768,
446,
12,
74,
444,
461,
334,
464,
72,
28,
28,
461,
443,
443,
28,
161,
461,
443,
461,
28,
443,
461,
72,
711,
446,
28,
187,
449,
435,
708,
28,
28,
2,
446,
461,
447,
710,
737,
462)
})
Java = pd.DataFrame({ 'Linguagem de Programação' : np.repeat('Java', 69), 'Quantidade de Palavras': (443,
447,
446,
318,
74,
446,
317,
446,
443,
443,
446,
318,
446,
460,
443,
710,
1221,
318,
443,
446,
318,
443,
491,
712,
443,
466,
746,
446,
446,
172,
443,
443,
160,
33,
443,
461,
710,
766,
318,
443,
446,
318,
321,
446,
37,
461,
461,
461,
446,
443,
1059,
461,
446,
461,
461,
461,
114,
74,
447,
318,
175,
461,
446,
318,
446,
268,
37,
318,
318)
})
C = pd.DataFrame({ 'Linguagem de Programação' : np.repeat('C', 72), 'Quantidade de Palavras': (1003,
39,
446,
33,
866,
461,
446,
461,
710,
13,
39,
446,
466,
474,
461,
39,
461,
39,
466,
446,
446,
687,
461,
443,
701,
443,
747,
451,
412,
557,
35,
464,
764,
268,
446,
2247,
33,
39,
507,
444,
463,
210,
39,
461,
72,
794,
33,
448,
35,
446,
219,
443,
446,
72,
215,
461,
446,
15,
461,
37,
461,
446,
463,
1014,
443,
39,
507,
16,
446,
10,
37,
443)
})
Swift = pd.DataFrame({ 'Linguagem de Programação' : np.repeat('Swift', 90), 'Quantidade de Palavras': (446,
446,
461,
710,
476,
74,
74,
446,
446,
710,
446,
461,
463,
446,
474,
446,
446,
465,
474,
446,
461,
446,
446,
446,
474,
446,
16,
446,
340,
446,
446,
446,
446,
446,
474,
334,
467,
446,
446,
461,
461,
74,
446,
7,
725,
447,
465,
448,
461,
444,
16,
446,
465,
461,
489,
446,
21,
446,
446,
461,
444,
465,
446,
446,
530,
446,
447,
208,
1264,
30,
444,
616,
461,
446,
446,
318,
465,
12,
710,
461,
72,
446,
474,
461,
321,
438,
454,
446,
461,
461)
})
Scala = pd.DataFrame({ 'Linguagem de Programação' : np.repeat('Scala', 99), 'Quantidade de Palavras': (27,
461,
27,
446,
39,
27,
44,
98,
866,
711,
104,
501,
821,
299,
74,
145,
101,
446,
128,
112,
445,
32,
1059,
318,
27,
461,
866,
33,
446,
866,
44,
307,
102,
27,
27,
461,
105,
866,
27,
866,
866,
446,
27,
20,
20,
866,
113,
27,
446,
27,
446,
27,
27,
27,
463,
26,
866,
468,
27,
27,
866,
27,
128,
26,
27,
20,
1144,
501,
446,
26,
26,
446,
98,
468,
446,
823,
27,
465,
446,
27,
33,
104,
27,
98,
27,
128,
102,
101,
27,
446,
1059,
453,
20,
847,
665,
866,
712,
670,
866)
})

df=MATLAB.append(Julia).append(Clojure).append(Perl).append(ObjectiveC).append(Kotlin).append(Java).append(C).append(Swift).append(Scala)

# boxplot
ax = sns.boxplot(x='Linguagem de Programação', y='Quantidade de Palavras', data=df, showfliers=False)
# add stripplot
ax = sns.stripplot(x='Linguagem de Programação', y='Quantidade de Palavras', data=df, color="orange", jitter=0.2, size=2.5)

# add title

plt.title("Boxplot da contagem de palavras das 10 linguagens de programação com menos códigos de conduta", loc="left")

# show the graph
plt.show()