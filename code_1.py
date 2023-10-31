## importations de base

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def f(x:float) -> float:
    """
    Calcule 2x
    """
    return 2*x

df=pd.read_csv('fichier.csv')

df.head()

df = df[df.default_flag == 1]

## Partie Lise - la découverte des planètes

dfl = df



## Partie Romain - caractéristiques mécaniques de la planète

dfr = df


## Partie Ombline - caractéristiques physico-chimiques des planètes

dfo = df


#étude des températures des planètes

temperature = dfo["st_teff"]

#regardons quelle est la tendance de température des planètes
plt.hist(temperature, bins=1000)
plt.show()

#on voit qu'une température est privilégiée, regardons laquelle

description_temperature = temperature.describe()

# on lit que la moyenne de température est de 5420.06057 K




## Partie Camille - 

dfc = df