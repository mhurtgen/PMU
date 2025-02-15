from Graph_zeroinjection import Graph_zeroinjection
import numpy as np
import graphviz

class Graph_zeroinjectionNCEII(Graph_zeroinjection):
    """overloading of methods of Graph_zeroinjection for NCEII grid"""
    def __init__(self,N,branch,zero_injections):
         self.N=N
         self.branch=branch
         self.zero_injections=zero_injections


    def observability(self,PMUconfig):
         """determines if PMU configuration makes system observable"""
         """returns binary vector (1 if node is observable, 0 otherwise)"""
         A=self.getA()
                
         """obsvec:observability vector"""
         obsvec=np.zeros(self.N)
         PMUvec=PMUconfig.getPMUconfig()
         lg=len(PMUvec)
         for i in range(0,lg):
              b_pmu=PMUvec[i]
              if (b_pmu==1):
                   obsvec[i]=1
                   for j in range (0,lg):
                      if (A[i][j]==1):
                           obsvec[j]=1

         #print('before constraint obsvec node 2:',obsvec[2])
         obsvec=self.constraints_zeroinjections(obsvec, self.zero_injections)
         #print('after constraint obsvec node 2:', obsvec[2])
         return obsvec    

    def representation(self,PMUconfig):
                """representation of power system with green nodes if pmu is present, cyan nodes if node is a zero-injection node, yellow if it is observed by a pmu"""
                g = graphviz.Graph()
                n=self.N
                zeroinj=self.zero_injections
                vecPMU=PMUconfig.getPMUconfig()
                
                for i in range(0,n):
                        
                        u=vecPMU[i]
                        
                        if (u==1):
                                #set green color for nodes with pmu
                                g.node(str(i),style='filled',fillcolor='green')
                                #get adjacent nodes to pmu#
                                adjPMU=self. get_adjacentnodes(i)
                                #set yellow for nodes adjacent to pmu
                                for k in adjPMU:
                                      if (k+1 not in zeroinj):
                                           g.node(str(k),style='filled',fillcolor='yellow')
                                
                        elif (i+1 in zeroinj):
                                g.node(str(i),style='filled',fillcolor='cyan')
                              
                        else:
                                g.node(str(i))
                                
                for el in self.branch:
                        i=int(el[0])
                        j=int(el[1])
                        g.edge(str(i),str(j))
                filename='Figure/NCEII'+str(self.N)+'_zeroinj'
                g.render(filename)

     
