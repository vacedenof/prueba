# Condicional if
adivinar = 42
numero = int(input('Sra usuaria, digite un número: '))
if (numero > adivinar):
  print('Bajele el volumen')
elif (numero < adivinar):
  print('Subale el volumen')
else:
  print('VERDADERO')



#if anidado 2
if (numero >= adivinar):
  if (numero > adivinar):
    print('Coloque un número menor')
  else:
    print('Acertado!!!')
else:
  print('Coloque un número mayor')
  
  
print('La instrucción "IF" terminó')


