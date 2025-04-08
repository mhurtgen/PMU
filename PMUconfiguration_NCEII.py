from PMUconfiguration import PMUconfiguration
import numpy as np
import random

class PMUconfiguration_NCIEE(PMUconfiguration):

   def PPA1(self,A):
        """first part of PageRank Placement Algorithm:"""
        """placement of a PMU at end node (node with only one neighbour)"""
        n=len(A)
        
        for i in range(0,n):
            sum=0
            for j in range(0,n):
                sum=sum+A[i][j]
             
            if (sum==1):
                for j in range(0,n):
                    if (A[i][j]==1):
                        self.addPMU(i)
       
   
   def PPA2(self,g,pr,nopmu):
        """second part of PageRank Placement Algorithm:"""
        """placement of PMUs at most important nodes"""
        """pr: PageRank classification of nodes"""

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
                if (i not in nopmu):
                    self.addPMU(i)
                    obsvec=g.observability(self)    
                    o=g.isobs(self)
                    if (o==1):break
                    
def getcandidates(self,endnodes,A):
        """get potential nodes for PMU placements"""
        """no nodes with pmus, or end nodes or nodes adjacent to end nodes"""
        
        l=len(self.PMUvec)
        
        e=len(endnodes)
        """potential nodes"""
        nodes=list(range(0,l))

        n=len(A)
        
          
        
        for i in range(0,e):
            endnode=endnodes[i]
            #no end nodes are chosen
            nodes.remove(endnode)
            #no nodes adjacent to end nodes are chosen
            for j in range(0,n):
               if A[endnode][j]==1:
                    nodes.remove(j)
        
        pmu=self.getPMUnodes()
        
        lpmu=len(pmu)
        #print('pmu ',pmu)
        for j in range(0,lpmu):
            #print('remove ',j,' ',pmu[j])
            if (pmu[j] in nodes):
                nodes.remove(pmu[j])
        
        return nodes
