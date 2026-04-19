#En este archivo estan las ecuaciones que vamos ocupar (las tenemos de una forma como ecuacion diferencial)
#Las definimos en dos pasos pues queremos que sean compatibles con el modulo que resuelve sistemas de ecuaciones diferenciales, que se creó antes 

#Las funciones dependen de los parametros en cadas caso y ese el primer paso de la funciones. 
# Luego cada ecuacion tiene una misma estructura y esa ya es aceptada por el modulp que ocupamos 

#susceptibles
def S(alfa,N):
    def Sn(t,y):
        return -(alfa*y[0]*y[1])/N
    return Sn
#infectados
def I(alfa,N,beta):
    def In(t,y):
        return (alfa*y[0]*y[1])/N - beta*y[1]
    return In
#removidos
def R(beta):
    def Rn(t,y):
        return beta*y[1]
    return Rn
#valor Ro que define la dinamica de la poblacion 
def R_o(alfa,So,N,beta):
    return (alfa*So) / (N*beta)

