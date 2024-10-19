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
       

    def GTP2(self,g,pr):
        """second part of graph theoretic procedure:"""
        """placement of PMUs at most important nodes"""
        """pr: PageRank classification"""

        """sorting of pagerank list of nodes in descending order"""
        lg=len(pr)
        Node_PR=list()
        for i in range(0,lg):
            Node_PR.append([i,pr[i]])
        Node_PR.sort(key=lambda x:x[1],reverse=True)
        
        """Placement of PMUs"""
        obsvec=g.observability(self)
        for a in Node_PR:
            i=a[0]
            if (obsvec[i]==0):
                self.addPMU(i)
            obsvec=g.observability(self)    
            o=g.isobs(self)
            if (o==1):break

        


