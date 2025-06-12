import random
opc = ["piedra", "papel", "tijera"]
gana_a = {"piedra": "tijera","papel": "piedra","tijera": "papel"}
def pedir_opcion():
    elec = input("Elige piedra, papel o tijera o salir para terminar").lower()
    while elec not in opc and elec != "salir":
        print("Error")
        elec = input("Elige piedra, papel o tijera (o 'salir'): ").lower()
    return elec
def ronda(jugador, pc):
    print(f"Elegiste {jugador}")
    print(f"La compu eligió {pc}")
    if jugador == pc:
        print("Empate")
        return "empate"
    elif gana_a[jugador] == pc:
        print("Ganaste")
        return "jugador"
    else:
        print("La compu ganó esta ronda")
        return "pc"



def jugar():
    puntos = {"jugador": 0,"pc": 0,"empate": 0}
    print("Bienvenido a Piedra, Papel o Tijera")

    while True:
        jugada = pedir_opcion()
        if jugada == "salir":
            print("El juego acabo")
            break
        compu = random.choice(opc)
        res = ronda(jugada, compu)
        if res == "jugador":
            puntos["jugador"] += 1
        elif res == "pc":
            puntos["pc"] += 1
        else:
            puntos["empate"] += 1
        print("--- Puntaje ---")
        print(f"Tu: {puntos['jugador']}")
        print(f"Compu: {puntos['pc']}")
        print(f"Empates: {puntos['empate']}")
        print("---------------\n")
    print("---Puntaje Final---")
    print(f"Tú: {puntos['jugador']}")
    print(f"Compu: {puntos['pc']}")
    print(f"Empates: {puntos['empate']}")

    if puntos["jugador"] > puntos["pc"]:
        print("Ganaste el juego")
    elif puntos["jugador"] < puntos["pc"]:
        print("La compu te gano")
    else:
        print("Empataron");
jugar()





