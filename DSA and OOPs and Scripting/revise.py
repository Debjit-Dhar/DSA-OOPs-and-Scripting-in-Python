import pandas as pd
import matplotlib.pyplot as pl
df=pd.read_csv('atomic vol.csv')
'''x=df['Calories'].mean()
df['Calories'].fillna(x,inplace=True)
df.drop_duplicates(inplace=True)'''
print(df.to_string())
ax=df['Atomic Volume'].plot()
'''L=['H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn','Fr','Ra','Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es']
for idx, row in df.iterrows():
    ax.annotate(L,(row['Atomic No'],row['Atomic Volume']))'''
pl.title('Lothar Meyers Curve')
pl.xlabel('Atomic Number')
pl.ylabel('Atomic Volume')
pl.show()
