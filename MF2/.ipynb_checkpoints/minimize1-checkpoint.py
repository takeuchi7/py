from scipy.optimize import minimize

class Minimize:
	def __init__(self, node, ob_variables,state):
		self.node = node
		self.ob_variables = ob_variables
		self.state = state
	def func(self):
		E=0
		for i in range(x*y):
            if(i%x!=(x-1)):
                E+=((X[i]-X[i+1])**2)
		for i in range(x):
            for j in range(y-1):
                E+=((X[i+(j*x)]-X[i+(j*x)+x])**2) 
		for i in range(x*y):
            if(innode[i]!=None):
                E+=(X[i]-innode[i])**2
		return E

    def risan(self):
		res1 = minimize(func,self.node,args=(x,y,self.ob_variables,), method='cobyla')
		A=res1.x.tolist()
		return A