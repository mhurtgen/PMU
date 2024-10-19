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
    
        
    def GTP1(self,A):
        """first part of graph theoretic procedure:"""
        """placement of a PMU at each node with only one neighbour"""
        n=len(A)
        
        for i in range(0,n):
            sum=0
            for j in range(0,n):
                sum=sum+A[i][j]
             
            if (sum==1):
                    self.addPMU(i)
       

    def GTP2(self,A):
        """second part of graph theoretic procedure:"""
        """placement of PMUs at most important nodes"""
        return


