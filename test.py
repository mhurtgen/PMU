import Graph, numpy as np, PMUconfiguration

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

v1=PMUconfig1.getPMUconfig()
print(v1)
#PMUconfig1.shuffle(ed,A)
#v2=PMUconfig1.getPMUconfig()
#print(v2)
PMUconfig2=g.perturb(PMUconfig1)
v2=PMUconfig2.getPMUconfig()
print(v2)

g.representation('IEEE14', PMUconfig2)



