f = 1 #factorial
num = int(input("Escriba el numero del que quiere saber el factorial: "))#numero que ingresa el usuario

for i in range(1,num + 1):#bucle para realizar la operacion del factorial
    f = f * i

print("El factorial de ", num, "es: ", f)