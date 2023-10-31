## importations de base

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


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

##Partie Camille, analyse des systèmes 
par_etoile=df.groupby(by='hostname')
dfc = df
dfc_entité=dfc[['pl_name', 'hostname', 'sy_snum', 'sy_pnum', ]]
print("Analysons la répartition du nombre d'étoile par système solaire")
dfc_entité.sy_snum.value_counts().plot(kind='bar')
#On peut voir que le nombre de système avec 1 étoile est très majoriaire et que les systèmes avec 4 étoiles sont extras rares

