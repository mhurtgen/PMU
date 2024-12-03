from PMUconfiguration import PMUconfiguration
import numpy as np


class PMUconfiguration_constr(PMUconfiguration):

    def PPA1(self,A):
          """first part of PageRank Placement Algorithm:"""
          """placement of a PMU at adjacent node of nodes with only one neighbour"""
          n=len(A)
          I_measurements=list()
          obsvec=np.zeros(n)
        
          for i in range(0,n):
              sum=0
              for j in range(0,n):
                  sum=sum+A[i][j]
             
              if (sum==1):
                  for j in range(0,n):
                      if (A[i][j]==1):
                          self.addPMU(j)
                          I_measurements.append([j,i])
                          obsvec[i]=1
                          obsvec[j]=1
          return I_measurements, obsvec
    
    def addImes(self,j,AdjNode_PR,obs,obsvec,I_measurements,nImeas,nmeas):


        if (nmeas==nImeas):
            return obsvec,I_measurements
        nAdj=len(AdjNode_PR)
        brmes=list()
        k=0
        
        for a in AdjNode_PR:
            i=a[0]
            if (nmeas<nImeas):

                print('i=',i)
            
                if (obsvec[i]==obs):
                    print('measurement ',j,'-',i)
                    I_measurements.append([j,i])
                    brmes.append(i)
                    obsvec[i]=1
                    nmeas=nmeas+1

            
        
        if (nmeas<nImeas):
            k=0
            for a in AdjNode_PR:
                i=a[0]
                if (i not in brmes):
                    print('2')
                    I_measurements.append([j,i])
                    brmes.append(i)
                    obsvec[i]=1
                    nmeas=nmeas+1
                if (nmeas==nImeas):break
                k=k+1
            
        return obsvec,I_measurements
                
            
    def selectbranches(self,pr,A,j,obsvec,I_measurements,nImeas):
        """select branches for PMU current measurements"""
        nmeas=0
        n=len(A)
        AdjNode_PR=list()
        for k in range(0,n):
            if (A[j][k]==1):
                AdjNode_PR.append([k,pr[k]])

        AdjNode_PR.sort(key=lambda x:x[1],reverse=True)
        print('node ',j)
        print(AdjNode_PR)

        obsvec,I_measurements=self.addImes(j,AdjNode_PR,0,obsvec,I_measurements,nImeas,nmeas)
       

        return obsvec, I_measurements


    
    def PPA2(self,g,n_Imeas,I_measurements,obsvec):
        """second part of PageRank Placement Algorithm:"""
        """placement of PMUs at most important nodes"""
        A=g.getA()
        n=g.getN()
        """pr: PageRank classification of nodes"""
        pr=g.pageRank()
        """sorting of pagerank list of nodes in descending order"""
        lg=len(pr)
        Node_PR=list()
        for i in range(0,lg):
            Node_PR.append([i,pr[i]])
       
        Node_PR.sort(key=lambda x:x[1],reverse=True)
      
        """Placement of PMUs"""
        obsvec=np.zeros(n)
        for a in Node_PR:
            i=a[0]
            if (obsvec[i]==0):
                self.addPMU(i)
                print('i=',i)
                obsvec[i]=1
                """selection of branches for current measurements"""
                obsvec, I_measurements=self.selectbranches(pr,A,i,obsvec,I_measurements,n_Imeas)

            o=g.isobs_constr(obsvec)
            print('o=',o)
            if (o==1):
                print('obsvec=',obsvec)
                return I_measurements
        return I_measurements
