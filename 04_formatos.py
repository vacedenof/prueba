# Formatos de impresión
edad = 60
estatura = 1.8
print("La edad es:", edad)
print("La estatura es:", estatura)
#1ra manera de uso de formato:
print("La edad es:", edad, "y la estatura es:", estatura)
#2da manera de uso de formato (la más utilizada):
print(f"La edad es: {edad} y la estatura es: {estatura}")
#3ra manera de uso de formato:
print("La edad es: {} y la estatura es: {}".format(edad,estatura))

print("La edad más la estatura es:", edad + estatura)
print(f"La edad más la estatura es: {edad + estatura}")
print("La edad más la estatura es: {}". format(edad + estatura))