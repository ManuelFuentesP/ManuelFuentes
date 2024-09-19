print('soy el Profesor Oak')
genero = input("Eres un chico o una chica? ")

if genero == "chico":
    print('Bienvenido!')
    
else: 
    print('Bienvenida!')
print("Al mundo de los Pokemon")

y=input("Que edad tienes?")

if int(y)<10:
    if genero == "chico":
        print("No tienes edad suficiente para ser entrenador")
    else:
        print("No tienes edad suficiente para ser entrenadora")
    quit()
    
print("Tu aventura comienza ya!")

reg = input("Necesitaras un compañero de viaje, En que region te encuentras?")
if reg == 'Kanto' and genero == 'chico':
    print("Tu compañero sera Misty!")
else:
    print("Tu compañero sera Brook!")
    
tipo = input("Que tipo de Pokemos quieres para empezar? ")
if tipo == 'agua':
    print("Tu starter es Oshawott!")
elif tipo == 'fuego':
    print("Tu starter es Cyndaquil!")
elif tipo == 'planta':
    print("Tu starter es Rowlet!")
else:
    print("Debes escoger agua, fuego o planta")
    
if genero == 'chico':
    print("""Ya estas listo para empezar tu aventura
          Buena suerte!""")
    
else:
    print("""Ya estas lista para empezar tu aventura
          Buena suerte!""")