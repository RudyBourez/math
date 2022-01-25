import pandas as pd
import numpy as np

liste = [1, 5, 5, 2, 8, 12, 11, 10, 4, 5]
liste.sort()
moyenne = sum(liste)/len(liste)
ecart_type = (sum(list(map(lambda x: (x - moyenne)**2, liste)))/10) ** (1/2)
minimum = min(liste)
maximum = max(liste)
print(f'Ecart-type calcul : {ecart_type}')

df = pd.DataFrame(liste, columns=["values"])
print(df.describe())
matrice = np.array(liste)
print(f'Ecart-type numpy : {matrice.std(ddof=1)}')

# print(mediane)