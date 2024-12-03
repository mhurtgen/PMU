import OptPlacementPMU_constr, pickle as p, random, numpy as np, Graph_constraint




with open('buscase14.pickle','rb') as f:
   bus=p.load(f)

with open('buscase14.pickle','rb') as f:
   bus=p.load(f)



N=14
print('b=',branch)


G=Graph_constraint.Graph_constraint(N,branch)
   
OptPlacement=OptPlacementPMU_constr.OptPlacementPMU_constr(N,branch)


PMUconfigPPA_constr,I_measurements=OptPlacement.PPA(1)

print('I_measurements=',I_measurements)

n_pmu=PMUconfigPPA_constr.getnPMU()
print(n_pmu)
pmu1=PMUconfigPPA_constr.getPMUnodes()
print('pmu=')
print(pmu1)

G. representation('IEEE14_1',PMUconfigPPA_constr,1,I_measurements)

"""
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

"""
