
import PMUconfiguration, Graph

class ILS():
    def __init__(self,M):
        self.T=10
        self.M=60

    def locsearch(self,G,PMUconfig):
        """local search starting from given PMU configuration"""

        
        G.perturb(PMUconfig)
        G.removeextra(PMUconfig)
        return PMUconfig

    
    def IterationsLocalSearch(self,G,PMUconfig):
        for i in range(0,self.M):
            self.locsearch(G,PMUconfig)
            PMUconfig=G.randomadditionPMUs(PMUconfig,npmus)
