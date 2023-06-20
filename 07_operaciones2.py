# ****** Operaciones relacionales o de comparación******
number = int(input('Digite un número: '))
print(number > 3)  #pregunta si number es mayor a 3
print(number >= 3)  #pregunta si number es igual o mayor a 3
print(number < 3)  #si number es menor a 3
print(number <= 3)  #si number es menor o igual a 3
print(number == 3)  #si number es igual a 3
print(number != 3)  #si number es diferente a 3

# ****** Operaciones lógicas******
# True (1) / False (0)
print("Operaciones lógicas")

# Conjunción (and &)
print('Conjunción:')
print(True and True)
print(False & False)
print(number > 3 and number < 10)

# Disyunción (or |)
print('Disyunción:')
print(False or True)
print(number <= 3 or number >= 10)
print(not ((number <= 3 | number >= 10)))

# Negación (not)
print('Negación:')
print(not (True))
print(False)

# Or exclusiva (^)
print('Or exclusiva:')
print(False ^ False)
print(False ^ True)
print(True ^ False)
print(True ^ True)

# ****** Operaciones de pertenencia******
#in
print('Operador in:')
nombre = "Cesar Quintero"
print('Q' in nombre)
print('z' in nombre)
