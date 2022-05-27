#sai
import pandas as pd
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

df = pd.read_csv (open(r'F:\SEM IV\Applied Statistical Analysis\CIE 3\Stats Project.csv'))

df['pert_estimate']=round((df['tp']+df['to']+4*df['tm'])/6)

mu=df['pert_estimate'].sum()

#alekhya
df['pert_sigma']=((df['tp']-df['to'])/6)

df['variance']= df['pert_sigma']**2
var=df['variance'].sum()
s= (var)**[1/2]

print(df)
print(var)
#rishabh
x = np.arange(135,160,0.1)
px=[]
z=[]

for i in x:
  
     z_score=(i-mu)/s

     z.append(z_score)
     if i>mu:
          px.append(scipy.stats.norm.sf(z_score))
     else :
          px.append(1-scipy.stats.norm.sf(z_score))
#Mihir
plt.style.use('fivethirtyeight')
plt.figure(figsize = (9, 6))
plt.plot(x, px, color = 'cyan') 
plt.show()