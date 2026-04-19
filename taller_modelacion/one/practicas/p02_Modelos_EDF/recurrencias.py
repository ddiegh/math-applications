def crec_exp(k):
    Po = 2 
    P = [Po]
    for _ in range(49):
        P.append(k*P[-1])
    return P 

def logistica(t, P):
    r = 0.5
    k = 1000
    return r * P * (1-(P/k))

def lineal(r,b,Xo=1):
    X = [Xo]
    for _ in range(20):
        Xn = r*X[-1] + b 
        X.append(Xn)
    return(X)

def simp(t,y):
    return -6*t+3
def solucion(t):
    return -3*t**2 + 3*t + 2
