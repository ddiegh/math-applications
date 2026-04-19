#definimos las ecuaciones, en donde cada una se le pueden ir moviendo los paramentros

# y[0] son los valores de nos conejos en el tiempo anterior 
# y[1] son los valores de los conejos en el tiempo anterior

#lo hacemos en este formato para que sea compatible con el solucionador de Euler
def conejos(r,b):
    def Cn(t,y:list):
        valor_conejo = (r*y[0])*(1-y[0]) - b*y[0]*y[1]
        return valor_conejo
    return Cn

def zorros(d,c):
    def Zn(t, y:list):
        valor_zorros = -d*y[1] + c*y[0]*y[1]
        return valor_zorros
    return Zn


