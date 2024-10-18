import numpy as np

class PMUconfiguration:
    def __init__(self,N):
        self.PMUvec=np.zeros(N)

    def addPMU(self,i):
        self.PMUvec[i]=1
        
    def setPMUconfig(self,v):
        self.PMUvec=v

    def getPMUconfig(self):
        return self.PMUvec
    
        
