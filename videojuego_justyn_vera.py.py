import json
import os

if os.path.exists("videojuego1.json"):
    archivo = open("videojuego1.json", "r",encoding="utf-8")
    jugador = json.load(archivo)
    archivo.close()
    print("Partida de cargada correctamente")
else:
    print("Te damos la bienvenida a la aventura mas epica de toda tu vida..")
    nombre = input("Ingresa tu nombre futuro maestro pokemon: ")
    jugador = {
        "nombre" : nombre
    }

opcion = 0

while opcion != 2:
    print("Hola", nombre,"tu aventura esta por comenzar")
    print("1.comenzar juego")
    print("2.creditos del videojuego")
    opcion = int(input("Seleccion una opcion para empezar: "))
    
    if opcion == 1:
        subopcion = 0
        
        while subopcion != 4:
            print("--POKEMON: MAESTROS DEL UNIVERSO--")
            print("1.Explorar zonas")
            print("2.Comprar energia")
            print("3.Tu camino pokemon hasta ahora")
            print("4.Guardar y salir")
            subopcion = int(input("Selecciona una para empezar: "))
            
            if subopcion == 1:
                print("=====REGION KANTO====")
                print("""Bienvenido a la region Kanto entrenador, en esta region encontraras maravillosas zonas de 
                     diferentes tipos de pokemon, pero antes tienes que saber que el nivel de energia a consumir varia
                     depende de la zona a explorar.
                     te indicamos a continuacion:
                     ========================================================================
                     -Pradera Inicial: 5 de energia        -Central Electrica: 20 de energia. 
                     -Bosque Verde: 10 de energia          -Cueva Rocosa: 20 de energia
                     -Playa Azul: 10 de energia            -Montaña Nevada: 35 de energia.
                     -Volcan Ardiente: 20 de energia       -Mansion Misteriosa: 35 de energia.
                     =========================================================================
                     pero no te preocupes podras recuperar energias siempre y cuando ganes los combates con los pokemones que te enfrentes
                     asi es evita perder combates contra pokemones si no se te restara 15 de energia al perder un combate. Pero asi 
                     mismo ganaras energia comprando en la tienda de cada zona, solo debes ganar un combate o recogiendo recursos
                     el juego te dara 3 monedas por cada combate ganado y 1 moneda por cada recurso obtenido. Mucha suerte :)
                     """)
                print("1.Pradera Inicial: Tipo Volador y Normal")
                print("2.Bosque Verde: Tipo Planta y Bicho")
                print("3.Playa Azul: Tipo Agua")
                print("4.Volcan Ardiente: Tipo Fuego ")
                print("5.Central Electrica: Tipo Electrico")
                print("6.Cueva Rocosa: Tipo Roca y Tierra")
                print("7.Montaña Nevada: Tipo Hielo")
                print("8.Mansion Misteriosa: Tipo Fantasma")
                subopcion = int(input("Selecciona una zona para empezar: "))
                
               

    
    