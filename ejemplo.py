num1= int(input("Ingrese un número "))
num2= int(input("ingrese otro número "))
c= 0
resultado= 0
while c < num1:
    resultado += num2
    print(resultado)
    c+= 1
print(f"El resultado es: {resultado}")
