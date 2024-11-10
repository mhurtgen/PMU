import Graph, PMUconfiguration, pickle as p, ILS

""" Example using Graph class""" 
"""IEEE14 power network """
#branch=[[1,2],[1,5],[2,3],[2,4],[2,5],[3,4],[4,5],[4,7],[4,9],[5,6],[6,11],[6,12],[6,13],[7,8],[7,9],[9,10],[9,14],[10,11],[12,13],[13,14]]


def OptPlacementPMU(N,branch):
    g=Graph.Graph(N,branch)
    n=g.getN()
    A=g.getA()
    Adj=g.getAdj(A)
    ed=g.endnodes()
    print('ed=',ed)
    
    """optimal PMU configuration obtained by solving integer linear problem"""
    pos=g.getPDS()
    print(pos)
    PMUconfigPDS=PMUconfiguration.PMUconfiguration(n)
    PMUconfigPDS.setPMUconfig(pos)
    pmupds=PMUconfigPDS.getPMUnodes()
    print(pmupds)
    """PageRAnk"""

    PMUconfig=PMUconfiguration.PMUconfiguration(n)

    """Implementing PageRank Placement Algorithm for PMU placement"""
    PMUconfig.PPA1(A)

    pr=g.pageRank()
    PMUconfig.PPA2(g,pr)
    n=PMUconfig.getnPMU()
    print(n)
    pmu1=PMUconfig.getPMUnodes()
    print(pmu1)

    """Iterated Local search starting from PMU configuration obtained by PPA"""
    ILS1=ILS.ILS(10,60,N)
    PMUconfig=ILS1.locsearch(g,PMUconfig)
    PMUconfigmin=ILS1.IteratedLocalSearch(g,PMUconfig,2)
    n=PMUconfigmin.getnPMU()
    print(n)
    

    #PMUconfig=ILS1.locsearch(g,PMUconfig1)
    
    #PMUconfig=ILS1.IteratedLocalSearch(g,PMUconfig1)
    #n2=PMUconfig.getnPMU()
    #print(n2)
    print(g.isobs(PMUconfig))

"""   
with open('case14.pickle','rb') as f:
   branch=p.load(f)

OptPlacementPMU(14,branch)
"""

with open('case57.pickle','rb') as f:
   branch=p.load(f)

OptPlacementPMU(57,branch)

"""
with open('case118.pickle','rb') as f:
   branch=p.load(f)

OptPlacementPMU(118,branch)"""

