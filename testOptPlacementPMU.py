import OptPlacementPMU, pickle as p, random, numpy as np, Graph




with open('case14.pickle','rb') as f:
   branch=p.load(f)
N=14
print('b=',branch)


G=Graph.Graph(N,branch)
   
OptPlacement=OptPlacementPMU.OptPlacementPMU(N,branch)



PMUconfigPPA=OptPlacement.PPA()
n_pmu=PMUconfigPPA.getnPMU()
print(n_pmu)
pmu1=PMUconfigPPA.getPMUnodes()
print(pmu1)

PMUconfigmin=OptPlacement.ILS()
n_pmu=PMUconfigmin.getnPMU()
print(n_pmu)
pmu1=PMUconfigmin.getPMUnodes()
print(pmu1)

G.rperesentation('IEEE14',PMUconfigPPA)
