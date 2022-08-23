print("-----------------------------")
print("Complementario 4")
print("-----------------------------")


print("Ingrese el año ")
a = int(input("Ingrese A: "))

print("Ingrese el mes ")
m = int(input("Ingrese B: "))

print("Ingrese los días ")
d = int(input("Ingrese C: "))

if d>0 and d<30 :
    print("Mañana es ", d+1, m , a)
else:
    if m>0 and m<12 : 
        print("Mañana es ", 1 ,m+1,a)
    else :
        print("Mañana es ", 1,1,a+1)
    
