from Graph import Graph
import graphviz

class Graph_constraint(Graph):
    """overloading of methods for Graphs with constraints on PMUs"""
    
    def representation(self,text,PMUconfig,nImes,Imeas):#,Obsvec):
                """representation of power system with colored nodes if pmu is present; thick branches if measurements made on branch"""
                g = graphviz.Graph(comment=text)
                n=self.N

                vecPMU=PMUconfig.getPMUconfig()
                
                for i in range(0,n):
                        u=vecPMU[i]
                        if (u==1):
                                g.node(str(i),style='filled',fillcolor='0.051 0.718 0.627')
                        else:
                                g.node(str(i))
                for el in self.branch:
                        i=int(el[0])
                        j=int(el[1])
                        b=self.test_branch_mes(Imeas,i,j)
                        #print(b)
                        if (b==1):
                              g.edge(str(i-1),str(j-1),style='bold')
                        else:
                              g.edge(str(i-1),str(j-1))

                filename='IEEE'+str(self.N)+'_'+str(nImes)+'.gv.pdf'
                g.render(filename)
        

    def isobs(self,obsvec):
        
        l=len(obsvec)
        for i in range(0,l):
            if obsvec[i]==0:
                return 0
        return 1
