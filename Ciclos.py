PS_jugador = 100
PS_oponente = 100
defensa_jugador = 100
defensa_oponente = 100
import random

while PS_jugador > 0 and PS_oponente > 0:
    while True:
        ataque_jugador = input("Introduzca un ataque: ")
        if ataque_jugador == "malicioso":
            defensa_oponente = defensa_oponente - 10
        elif ataque_jugador == "placaje":
            PS_oponente = PS_oponente - 35 * 100/defensa_oponente
            #dividir entre la defensa hace que el ataque se pueda hacer mas fuerte
            break #break es para salir instantaneo del while cuando esta condicion se cumpla
        elif ataque_jugador == "ascuas":
            PS_oponente = PS_oponente - 20
            break
        else:
            print("Que estas haciendo?? Tus atques son malicioso, placaje y ascuas!!")
            #No hay break porque no se selecciono un ataque valido
            
    ataque_oponente = random.randrange(0,3) #Esto nos va a dar un resultado aleatorio entre 0 y 2 (3 opciones)
    if ataque_oponente == 0: #latigo
        defensa_jugador = defensa_jugador - 10
        print("El oponente uso Latigo, tu defensa ha disminuido")
    elif ataque_oponente == 1: #placaje
        PS_jugador = PS_jugador - 35 * 100/defensa_jugador
        print("El oponente uso Placaje")
    elif ataque_oponente == 2: #ascuas
        PS_jugador = PS_jugador - 40
        print("El oponente uso Ascuas")
    else:
        print("Error en la generacion random")
    
    print("Jugador: ", PS_jugador, "PS")
    print("Oponente: ", PS_oponente, "PS")
    
if PS_oponente <= 0:
    print("GANASTE!!!")
else:
    print("Perdiste :(")
