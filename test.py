import Graph, numpy as np, PMUconfiguration

""" Example using Graph class""" 
"""IEEE14 power network """
branch=[[1,2],[1,5],[2,3],[2,4],[2,5],[3,4],[4,5],[4,7],[4,9],[5,6],[6,11],[6,12],[6,13],[7,8],[7,9],[9,10],[9,14],[10,11],[12,13],[13,14]]

g=Graph.Graph(14,branch)
A=g.getA()
"""optimal PMU configuration obtained by solving integer linear problem"""
#pos=g.getPDS()

#print(pos)

"""PageRAnk"""
n=g.getN()
pr=g.pageRank()


PMUconfig1=PMUconfiguration.PMUconfiguration(n)


PMUconfig1.GTP1(A)

PMUconfig1.GTP2(g,pr)
print(PMUconfig1.getPMUconfig())
