from Graph import Graph
import graphviz

class Graph_zeroinjection(Graph):
    """overloading of methods for Graphs with constraints on PMUs"""
    
        

    def isobs(self,obsvec):
        
        l=len(obsvec)
        for i in range(0,l):
            if obsvec[i]==0:
                return 0
        return 1
