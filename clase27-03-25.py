nmed = int(input("Número de mediciones: "))
prom= 0
c= 0 
while c < nmed:
    t= float(input("Temperatura: "))
    if t < 15 or t > 30:
        print("ALERTA!!!!!!")
    prom+= t
    c+= 1
prom=  prom / nmed