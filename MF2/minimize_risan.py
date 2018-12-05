from scipy.optimize import minimize

def risan(x,y,node,ob_variables,state):
    res1 = minimize(func,node,args=(x,y,ob_variables,), method='cobyla')
    A=res1.x.tolist()
    A=risanka(A,node,state)
    return A

#最小化：隣接同士と、入力の遷移を観測値と捉えていく
def func(X,x,y,ob_variables):
    E = 0
    for i in range(x*y):
        if(i%x!=(x-1)):
            E+=((X[i]-X[i+1])**2)
        for i in range(x):
            for j in range(y-1):
                E+=((X[i+(j*x)]-X[i+(j*x)+x])**2)
        for i in range(x*y):
            if(ob_variables[i]!=None):
                E+=(X[i]-ob_variables[i])**2
        return E

#連続的に最小化しているので、離散的になるよう処理する
#ICMだと局所的最大になる．まだビタビは使えないので、あくまで処置
def risanka(A,node,state):
    print('状態の最小化結果',['{:.2f}'.format(n) for n in A])
    for n in range(len(node)):
        m=10000
        M=0
        for i in state:
            if((A[n]-i)**2 < m):
                m=(A[n]-i)**2
                M=i
        A[n]=M
    print('状態の離散化',['{:.2f}'.format(n) for n in A])
