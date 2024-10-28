
import PMUconfiguration, Graph

class ILS():
    def __init__(self,T,M):
        self.T=T
        self.M=M

    def locsearch(self,G,PMUconfig):
        """local search starting from given PMU configuration"""
        obs=0
        for i in range(0,self.T):
            
                PMUconfig=G.perturb(PMUconfig)
                print('obs=',G.isobs(PMUconfig))
                PMUconfig=G.removeextra(PMUconfig)
            
        return PMUconfig

    
    def IterationsLocalSearch(self,G,PMUconfig):
        for i in range(0,self.M):
            PMUconfig=self.locsearch(G,PMUconfig)
            PMUconfig=G.randomadditionPMUs(PMUconfig,npmus)
