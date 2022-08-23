print("------------------------------")
print("Complementario 5")
print("------------------------------")

print("Ingrese las velocidades de ambos vehiculos ")
vel1 = float(input("Ingrese A:"))
vel2 = float(input("Ingrese B:"))

print("Ingrese la distancia que los separa ")
dist = float(input("Ingrese C: "))

if vel1>0 and vel2>0 : 
    t = dist/(vel1+vel2)
    print(t, " Segundos")
else :
    print("Error")
