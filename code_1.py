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

