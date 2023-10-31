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

dfr = df[["pl_name","hostname","default_flag","sy_snum","sy_pnum","rowid","pl_refname","pl_orbper","pl_orbsmax","pl_rade","pl_bmasse","pl_orbeccen"]]


## Partie Ombline - caractéristiques physico-chimiques des planètes

dfo = df


## Partie Camille - 

dfc = df