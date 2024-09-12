"""Este es un programa que simula hacer arepas
este programa recibira los datos del volumen de los ingredientes
y dara como resultado el volumen total de las arepas"""

#Se declaran los ingredientes
agua=int(input("Cuantas tazas de agua? "))
print("el agua es",agua)
harina=int(input("Cuantas tazas de harina? "))
print("la harina es",harina)
sal=1/16/3 #la sal se convierte de cdtas a tazas, hay 3 cdtas por cda y 16 cdas por taza
print("la sal es",sal)
aceite=1/16 #el aceite se convierte de cdas a tazas

#comienza la preparacion de la arepa
bol=agua+harina+sal
budare=bol+aceite

#se imprime el resultado
print("la arepa final es",budare)

input("presione enter para continuar")