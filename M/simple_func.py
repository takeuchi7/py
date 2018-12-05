from scipy.optimize import minimize

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