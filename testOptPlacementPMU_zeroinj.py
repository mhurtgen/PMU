import PMUconfiguration_zeroinj, OptPlacementPMU_zeroinj, pickle as p, random, numpy as np, Graph_zeroinjection
import yaml
from yaml import load, dump

"""
with open('case14.pickle','rb') as f:
   branch=p.load(f)

with open('buscase14.pickle','rb') as f:
   bus=p.load(f)

with open('gencase14.pickle','rb') as f:
   gen=p.load(f)

N=14

"""

"""
with open('case57.pickle','rb') as f:
   branch=p.load(f)

with open('buscase57.pickle','rb') as f:
   bus=p.load(f)

with open('gencase57.pickle','rb') as f:
   gen=p.load(f)

N=57

with open('pmuIEEE57.yml','r') as f:
   pmu=yaml.safe_load(f)

"""

with open('case118.pickle','rb') as f:
   branch=p.load(f)

with open('buscase118.pickle','rb') as f:
   bus=p.load(f)

with open('gencase118.pickle','rb') as f:
   gen=p.load(f)

N=118

with open('pmuIEEE118.yaml','r') as f:
   pmu=yaml.safe_load(f)


G=Graph_zeroinjection.Graph_zeroinjection(N,branch,bus,gen)
   
OptPlacement_zeroinj=OptPlacementPMU_zeroinj.OptPlacementPMU_zeroinj(N,branch,bus,gen)


PMUconfig0=PMUconfiguration_zeroinj.PMUconfiguration(N)
#PMUconfig0=PMUconfiguration.PMUconfiguration(N)

PMUconfig0.setPMUvec(pmu)
print(pmu)
print(PMUconfig0.getPMUnodes())

#vec2=PMUconfig0.shuffle()
PMUconfigmin=OptPlacement_zeroinj.ILS(PMUconfig0)
n_pmu=PMUconfigmin.getnPMU()
print(n_pmu)
pmu1=PMUconfigmin.getPMUnodes()
print(pmu1)
G.representation(PMUconfigmin)
"""
with open('pmuIEEE57.yml', 'w') as file:
    #dump(n_pmu,file)
    dump(pmu1,file)




vec=np.zeros((N))
pmu=[1,8,10,12]

for n in pmu:
   vec[n]=1

PMUconfig=PMUconfiguration.PMUconfiguration(N)
PMUconfig.setPMUconfig(vec)
print('pmu=',pmu)
obsvec=G.observability(PMUconfig)
print(obsvec)

ILS1=ILS.ILS(10,60,n)
PMUconfig=ILS1.locsearch(G,PMUconfig)
pmus=PMUconfig.getPMUnodes()
print(pmus)


PMUconfigPPA=OptPlacement_zeroinj.PPA()
n_pmu=PMUconfigPPA.getnPMU()
print(n_pmu)
pmu1=PMUconfigPPA.getPMUnodes()
print(pmu1)
"""
