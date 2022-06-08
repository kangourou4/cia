from population import *

nombre_voraces=2
nombre_sdi=5
nombre_ssp=5

pop=dict()

for k in range(1,nombre_voraces+1):
    pop["v"+str(k)]=Vorace(6,30)
for k in range(1,nombre_sdi+1):
    pop["sdi"+str(k)]=SDI(6,30)
for k in range(1,nombre_ssp+1):
    pop["ssp"+str(k)]=SSP(6,30)
