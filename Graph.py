import numpy as np
from scipy.optimize import LinearConstraint, milp
import PMUconfiguration

"""get gain and adjacency matrix"""

class Graph:

        def __init__(self,N,branch):
                self.N=N
                self.branch=branch

        def getN(self):
                return self.N
        
        def getA(self):
                """get adjacency matrix"""
                m=len(self.branch)
                n=self.N

                A=np.zeros((n,n))

                for el in self.branch:
                        i=el[0]
                        j=el[1]

                   
                        A[i-1][j-1]=1
                        A[j-1][i-1]=1

                return A

        def getPDS(self):
                """get vector giving power dominating set - optimal PMU configuration"""
                """implementation of the integer linear programming formulation"""
                """minimisation of number of PMUs while guaranteeing that each node is observed"""
                """minimise sum of compents of X vector with the constraint (A+I).X>=1"""
                """, where X is the binary vector where X_i=1 if a PMU is placed at the node and 0 otherwise"""
                """A is the incidence matrix"""
                """I is the unity matrix"""
                
                A=self.getA()
                I=np.identity(self.N)

                B=A+I

                c=np.ones((self.N))

                b_l=np.ones((self.N))
                b_u=np.full_like(b_l, np.inf, dtype=float)

                constraints = LinearConstraint(B, b_l, b_u)


                integrality=np.ones_like(c)
                res=milp(c=c,constraints=constraints,integrality=integrality)
                
                
                pos=np.nonzero(res.x)

                return pos
     
        # normalize the matrix (make it a probability matrix (all cols sum to 1))
        def normalizeAdjacencyMatrix(self):
                A=self.getA()
                n = len(A) # n = num of rows/cols in A
                for j in range(len(A[0])):
                        sumOfCol = 0
                        for i in range(len(A)):
                             sumOfCol += A[i][j]
        
                        if sumOfCol == 0: # adjust for dangling nodes (columns of zeros)
                             for val in range(n):
                                 A[val][j] = 1/n
                             else:
                                 for val in range(n):
                                      A[val][j] = (A[val][j] / sumOfCol)
                return A

        # implement damping matrix using formula
        # M = dA + (1-d)(1/n)Q, where Q is an array of 1's and d is the damping factor
        def dampingMatrix(self):
                A=self.getA()
                n = len(A) # n = num of rows/cols in A
                dampingFactor = 0.85
                Q = [[1/n]*n]*n
                arrA = np.array(A)
                arrQ = np.array(Q)
                arrM = np.add((dampingFactor)*arrA, (1-dampingFactor)*arrQ) # create damping matrix
                return arrM

        # find eigenvector corresponding to eigenvalue 1
        def  findSteadyState(self,M, n):
                # find eigenvectors
                evectors = np.linalg.eig(M)[1]
    
                # find eigenvalues
                eigenValues = np.linalg.eig(M)[0]
                lstEVals = []
                for val in eigenValues:
                        lstEVals.append(round(val))
    
                # find eigenvector with eigenvalue 1
                idxWithEval1 = lstEVals.index(1)
                steadyStateVector = evectors[:, idxWithEval1]
    
                # normalize steady state vector so its components sum to 1
                lstVersionSteadyState = []
                sumOfComps = 0
                returnVector = []
                for val in steadyStateVector:
                        sumOfComps += val
                        lstVersionSteadyState.append(val)
                        
                for val in lstVersionSteadyState:
                        returnVector.append(val/sumOfComps)
    
                return returnVector

        def pageRank(self):
                A=self.getA()
                n = len(A) # n = num of rows/cols in A
                A = self.normalizeAdjacencyMatrix() 
                M = self.dampingMatrix() 
    
                # find steady state vector
                steadyStateVectorOfA = self.findSteadyState(M, n)
                return steadyStateVectorOfA

        def observability(self,PMUveconfig):
                """determines if PMU coonfiguration makes system observable"""
                A=self.getA()
                """obsvec:observability vector"""
                obsvec=np.zeros(self.N)
                PMUvec=PMUconfig.getPMUconfig()
                lg=len(PMUvec)
                for i in range(0,lg):
                       b_pmu=PMUvec(i)
                       if (b_pmu==1):
                               obsvec[i]=1
                               for j in range (0,N):
                                       if (A[i][j]==1):
                                               obsvec[j]=1
                return obsvec

        def isobs(self,obsvec):
                l=len(obsvec)
                for i in range(0,l):
                        if obsvec[i]==0:
                                return 0
                return 1
                
                             


                
        
