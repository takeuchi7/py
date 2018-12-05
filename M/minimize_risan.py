from scipy.optimize import minimize
import simple_func
import imp
imp.reload(simple_func)

class Minimize_risan(object):
    def __init__(self,x,y,node,ob_variables,state):
        self.x=x
        self.y=y
        self.node=node
        self.ob_variables=ob_variables
        self.state=state
        #最小化：隣接同士と、入力の遷移を観測値と捉えていく
        
    def risan(self):
        minimize_node = minimize(simple_func.func,self.node,args=(self.x,self.y,self.ob_variables,), method='cobyla')
        minimize_node=minimize_node.x.tolist()
        print('状態の最小化結果',['{:.2f}'.format(n) for n in minimize_node])
        minimize_risan_node=self.risanka(minimize_node)
        print('状態の離散化',['{:.2f}'.format(n) for n in minimize_node])
        return minimize_risan_node


    #連続的に最小化しているので、離散的になるよう処理する
    #ICMだと局所的最大になる．まだビタビは使えないので、あくまで処置
    def risanka(self,minimize_node):
        for n in range(len(self.node)):
            m=10000
            M=0
            for i in self.state:
                if((minimize_node[n]-i)**2 < m):
                    m=(minimize_node[n]-i)**2
                    M=i
            minimize_node[n]=M
        return minimize_node
