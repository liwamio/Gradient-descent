import sys
import numpy as np

class GradientDescent: 
    
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def residual(Theta, X, Y):
        r = []
        m = len(Y)
        for i in range(m):    
            r.append(Y[i] - (np.dot(X[i], Theta)))
        return r
    
    def sse(Theta, X, Y):        
        m = len(X)
        r = GradientDescent.residual(Theta, X, Y)
        SE = []
        for i in range(len(Y)): 
            SE.append(r[i]**2)
        SSE = sum(SE)
        return SSE
    
    def gradient(Theta, X, Y):    
        grad = []   
        n = len(X)  
        
        resid = sum(Theta*X)-Y   
        
        for j in range(n):            
            grad.append((2 * X[j] * resid))
       
        return grad
                        
    def run(self, max_steps=500):
        m = len(self.X)        
        n = len(self.X[0])
        Theta = [0]*n        
        sse = GradientDescent.sse(Theta, self.X, self.Y)                        
        alpha = 1
        for s in range(max_steps):            
            for i in range(m):                 
                g = GradientDescent.gradient(Theta, self.X[i], self.Y[i])
                newTheta = [Theta[j] - alpha * g[j] for j in range(len(g))]     

    
                newSse = GradientDescent.sse(newTheta, self.X, self.Y)          

      
                if newSse < sse: 
                    Theta, sse = newTheta, newSse
                    alpha *= 2   
                else:                    
                    alpha /= 2             

        return Theta
    

file_input = sys.argv[1:]
file = []
for i in range(len(file_input)):    
    with open(file_input[i]) as f: 
        file.append(list(filter(lambda x: x != '', map(float,f.read().split

()))))    
X = file[0]
Y = file[1]

X = np.array(X).reshape(len(Y), -1)
for i in GradientDescent(X,Y).run(): 
    print('{0:.2f}'.format(i), end = ' ')
    