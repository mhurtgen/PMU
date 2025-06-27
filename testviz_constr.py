import Graph_constraint, PMUconfiguration_constr
import pickle as p


with open('Grids/branchcase14.pickle','rb') as f:
   branch=p.load(f)


N=14
nImes=1


G=Graph_constraint.Graph_constraint(N,branch)

pmuconfig=PMUconfiguration_constr.PMUconfiguration_constr(N,nImes)
pmuconfig.fromfile('pmuIEEE14_1.yml','ImesIEEE14_1.yml')
   
#G.representation(pmuconfig)
