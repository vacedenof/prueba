#Cambiar datos por medio de indexación
num = [99, 34, 25, 56, 72]
print(num)
num[1] = 88
print(num)
#Resultado: num = [99,88,25,56,72]

#Función 'insert'
num.insert(1, 77)
print(num)
#Resultado: num = [99,77,88,25,56,72]

#Función append:
num.append(100)
print(num)
#Resultado: num = [99,77,88,25,56,72,100]

#Función extend:
num2 = [9, 8, 7]
num.extend(num2)
print(num)
#Resultado: num = [99,77,88,25,56,72,100,9,8,7]

#Función remove:
num.remove(100)
print(num)
#Resultado: num = [99,77,88,25,56,72,9,8,7]

#Función pop:
num.pop(2)
print(num)
#Resultado: num = [99,77,25,56,72,9,8,7]

#Función del:
del num[0]
print(num)
#Resultado: num = [77,25,56,72,9,8,7]

#Función clear:
num2.clear()
print(num2)
