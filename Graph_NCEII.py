from Graph import Graph
import numpy as np
import graphviz
import PMUconfiguration_zeroinj

class Graph_NCIEE(Graph):
     """overloading of methods for Graph of NCIEE"""

     def getA(self):
                """get adjacency matrix"""
                m=len(self.branch)
                n=self.N

                A=np.zeros((n,n))
                
                for el in self.branch:
                        
                        i=int(el[0])
                        j=int(el[1])

                   
                        A[i][j]=1
                        A[j][i]=1

                return A


    
     def representation(self,PMUconfig):#,Obsvec):
                """representation of power system with colored nodes if pmu is present"""
                g = graphviz.Graph()
                n=self.N
                #zeroinj=self.get_zeroinj()
                vecPMU=PMUconfig.getPMUconfig()
                
                for i in range(0,n):
                        #j=i-1
                        u=vecPMU[i]
                        if (u==1):
                                g.node(str(i),style='filled',fillcolor='green')
                 #       elif (i+1 in zeroinj):
                  #              g.node(str(i),style='filled',fillcolor='cyan')
                              
                        else:
                                g.node(str(i))
                                
                for el in self.branch:
                        i=int(el[0])
                        j=int(el[1])
                        g.edge(str(i),str(j))
                filename='IEEE'+str(self.N)#+'_zeroinj'
                g.render(filename)
