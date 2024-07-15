## juego piedra papel tijera##

import random


def jugar_ppt():
    opciones = ["piedra", "papel", "tijera"]
    ganador = {"piedra": "tijera", "papel": "piedra", "tijera": "papel"}

    while True:
        jugador = input(
            "Elige piedra, papel o tijera (o 'salir' para terminar el juego): ").lower()
        if jugador == "salir":
            print("Gracias por jugar. ¡Hasta luego!")
            break

        if jugador not in opciones:
            print("Opción inválida. Por favor, elige piedra, papel o tijera.")
            continue

        computadora = random.choice(opciones)
        print("La computadora eligió:", computadora)

        if jugador == computadora:
            print("Es un empate.")
        elif ganador[jugador] == computadora:
            print("¡Ganaste!")
        else:
            print("¡Perdiste!")

        seguir_jugando = input("¿Quieres seguir jugando? (s/n): ").lower()
        if seguir_jugando != "s":
            print("Gracias por jugar. ¡Hasta luego!")
            break


jugar_ppt()
