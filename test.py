import Graph, numpy as np, PMUconfiguration, ILS

""" Example using Graph class""" 
"""IEEE14 power network """
branch=[[1,2],[1,5],[2,3],[2,4],[2,5],[3,4],[4,5],[4,7],[4,9],[5,6],[6,11],[6,12],[6,13],[7,8],[7,9],[9,10],[9,14],[10,11],[12,13],[13,14]]

g=Graph.Graph(14,branch)

n=g.getN()


A=g.getA()

ed=g.endnodes()



PMUconfig1=PMUconfiguration.PMUconfiguration(n)
"""Implementing PageRank Placement Algorithm for PMU placement"""
PMUconfig1.PPA1(A)

pr=g.pageRank()
PMUconfig1.PPA2(g,pr)
pmu1=PMUconfig1.getPMUnodes()
print(pmu1)

"""Iterated Local search starting from PMU configuration obtained by PPA"""
ILS1=ILS.ILS(10,10)

#PMUconfig=ILS1.locsearch(g,PMUconfig1)
PMUconfig=ILS1.IteratedLocalSearch(g,PMUconfig1)
pmu2=PMUconfig.getPMUnodes()
print(pmu2)
print(g.isobs(PMUconfig))
