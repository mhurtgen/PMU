import Graph, PMUconfiguration, pickle as p, ILS


class OptPlacementPMU:
    def __init__(self,N,branch):
         self.g=Graph.Graph(N,branch)

    def getinfo(self):
         n=self.g.getN()
         A=self.g.getA()
    
         ed=self.g.endnodes()
         return n,A,ed

    def PowerDominatingSet(self):
         """optimal PMU configuration obtained by solving integer programming formulation"""
         n,A,ed=self.getinfo()
         pos=g.getPDS()
         PMUconfigPDS=PMUconfiguration.PMUconfiguration(n)
         PMUconfigPDS.setPMUconfig(pos)
         pmupds=PMUconfigPDS.getPMUnodes()
         return pmupds

    def PPA(self):
         
         n,A,ed=self.getinfo()
         """PageRAnk"""

         PMUconfig=PMUconfiguration.PMUconfiguration(n)

         """Implementing PageRank Placement Algorithm for PMU placement"""
         PMUconfig.PPA1(A)

         pr=self.g.pageRank()
         PMUconfig.PPA2(self.g,pr)
         

         return PMUconfig

    def ILS(self):
         """Iterated Local search starting from PMU configuration obtained by PPA"""

         n,A,ed=self.getinfo()
         
         PMUconfig=self.PPA()

         #ILS1=ILS.ILS(10,10,n)
         #ILS1=ILS.ILS(10,30,n)
         ILS1=ILS.ILS(20,30,n)
         PMUconfig=ILS1.locsearch(self.g,PMUconfig)
         PMUconfigmin=ILS1.IteratedLocalSearch(self.g,PMUconfig,2)
         n_min=PMUconfigmin.getnPMU()
         print(n_min)
         return PMUconfigmin
     
    def PPA_constr(self, n_Imeas):

         n,A,ed=self.getinfo()
         """PageRAnk"""

         PMUconfig=PMUconfiguration.PMUconfiguration(n)

         """Implementing PageRank Placement Algorithm for PMU placement"""
         I_measurements, obsvec=PMUconfig.PPA1_constr(A)

         pr=self.g.pageRank()
         I_measurements=PMUconfig.PPA2_constr(self.g,n_Imeas,I_measurements,obsvec)
         n=PMUconfig.getnPMU()
         print(n)
         pmu1=PMUconfig.getPMUnodes()
         print(pmu1)
         return PMUconfig, I_measurements


