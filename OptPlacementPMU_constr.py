import Graph_constraint, PMUconfiguration_constr, pickle as p, ILS

""" Example using Graph class""" 
"""IEEE14 power network """
#branch=[[1,2],[1,5],[2,3],[2,4],[2,5],[3,4],[4,5],[4,7],[4,9],[5,6],[6,11],[6,12],[6,13],[7,8],[7,9],[9,10],[9,14],[10,11],[12,13],[13,14]]
class OptPlacementPMU_constr:
    def __init__(self,N,branch):
         self.g=Graph_constraint.Graph(N,branch)

    def getinfo(self):
         n=self.g.getN()
         A=self.g.getA()
    
         ed=self.g.endnodes()
         return n,A,ed
    """
    def PowerDominatingSet(self):
         optimal PMU configuration obtained by solving integer programming formulation
         n,A,ed=self.getinfo()
         pos=g.getPDS()
         PMUconfigPDS=PMUconfiguration.PMUconfiguration(n)
         PMUconfigPDS.setPMUconfig(pos)
         pmupds=PMUconfigPDS.getPMUnodes()
         return pmupds
    
    def PPA(self):
         
         n,A,ed=self.getinfo()
         

         PMUconfig=PMUconfiguration.PMUconfiguration(n)

         
         PMUconfig.PPA1(A)

         pr=self.g.pageRank()
         PMUconfig.PPA2(self.g,pr)
         

         return PMUconfig
    
    def ILS(self):
         

         n,A,ed=self.getinfo()
         
         PMUconfig=self.PPA()
         
         ILS1=ILS.ILS(10,60,n)
         PMUconfig=ILS1.locsearch(self.g,PMUconfig)
         PMUconfigmin=ILS1.IteratedLocalSearch(self.g,PMUconfig,2)
         n_min=PMUconfigmin.getnPMU()
         print(n_min)
         return PMUconfigmin
    """ 
    def PPA(self, n_Imeas):

         n,A,ed=self.getinfo()
         """PageRAnk"""

         PMUconfig=PMUconfiguration_constr.PMUconfiguration_constr(n)

         """Implementing PageRank Placement Algorithm for PMU placement"""
         I_measurements, obsvec=PMUconfig.PPA1(A)


         I_measurements=PMUconfig.PPA2_constr(self.g,n_Imeas,I_measurements,obsvec)
         n=PMUconfig.getnPMU()
         print(n)
         pmu1=PMUconfig.getPMUnodes()
         print(pmu1)
         return PMUconfig, I_measurements


