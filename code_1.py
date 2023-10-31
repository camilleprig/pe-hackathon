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

dfr = df[["pl_name","hostname","default_flag","sy_snum","sy_pnum","rowid","pl_refname","pl_orbper","pl_orbsmax","pl_rade","pl_bmasse","pl_orbeccen"]]
dfr.rename(axis="columns", mapper={"pl_name":"nom","pl_orbper":"période_orbite","pl_orbsmax":"demi_grand_axe","pl_rade":"rayon","pl_bmasse":"masse","pl_orbeccen":"excentricité"},inplace=True)

# Répartition des orbites
dfr.demi_grand_axe.plot(xlabel="Demi grand axe de l'orbite (en unités astronomiques)",ylabel="Nombre de planètes")

## Partie Ombline - caractéristiques physico-chimiques des planètes
dfo = df

##Partie Camille, analyse des systèmes 
par_etoile=df.groupby(by='hostname')
dfc = df
dfc_entité=dfc[['pl_name', 'hostname', 'sy_snum', 'sy_pnum', ]]

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
