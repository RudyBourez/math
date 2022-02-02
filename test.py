import pandas as pd
import numpy as np

liste = [1, 5, 5, 2, 8, 12, 11, 10, 4, 5]
liste.sort()
Q1 = (len(liste)+3)/4
Me = (len(liste)+1)/2
Q3 = (3*len(liste)+1)/4
print(Q1,Me,Q3)

quartile1 = liste[2]+0.25*(liste[3]-liste[2])
mediane_calc = liste[4] + 0.5*(liste[5]-liste[4])
quartile3 = liste[6]+0.75*(liste[7]-liste[6])

print(quartile1,mediane_calc,quartile3)
