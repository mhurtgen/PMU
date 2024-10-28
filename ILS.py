
import PMUconfiguration, Graph

class ILS():
    def __init__(self,T,M):
        self.T=T
        self.M=M

    def locsearch(self,G,PMUconfig):
        """local search starting from given PMU configuration"""
        obs=0
        for i in range(0,self.T):
            
                PMUconfig2=G.perturb(PMUconfig)
                # print('obs=',G.isobs(PMUconfig))
                for i in range(0,5):
                    PMUconfig2=G.removeextra(PMUconfig2)

        l=PMUconfig.getnPMU()
        l2=PMUconfig2.getnPMU()
        
        if (l2<l):
            return PMUconfig2
        else:
            return PMUconfig

    
    def IteratedLocalSearch(self,G,PMUconfig):

        npmus=2
        for i in range(0,self.M):
            PMUconfig=G.randomadditionPMUs(PMUconfig,npmus)
            PMUconfig=self.locsearch(G,PMUconfig)
            
            #print(PMUconfig.getPMUnodes())
            

        return PMUconfig
