import random

def elegir_personaje():
    print("|SELECCIONA UN PERSONAJE|")
    print("Guerrero | Estadísticas equilibradas")
    print("Asesino  | Mucho ataque pero poca defensa")
    print("Tanque   | Defensa alta pero poco ataque")

    while True:
        eleccion = input("Elige un personaje: ").lower()

        if eleccion == "guerrero":
            print("\nHas elegido Guerrero\n")
            return {
                "nivel": 1,
                "experiencia": 0,
                "vida maxima": 100,
                "vida": 100,
                "fuerza": 7,
                "defensa": 7,
                "velocidad": 10,
                "critico": 5,
            }

        elif eleccion == "asesino":
            print("\nHas elegido Asesino\n")
            return {
                "nivel": 1,
                "experiencia": 0,
                "vida maxima": 75,
                "vida": 75,
                "fuerza": 10,
                "defensa": 5,
                "velocidad": 15,
                "critico": 10,
            }

        elif eleccion == "tanque":
            print("\nHas elegido Tanque\n")
            return {
                "nivel": 1,
                "experiencia": 0,
                "vida maxima": 125,
                "vida": 125,
                "fuerza": 5,
                "defensa": 10,
                "velocidad": 7,
                "critico": 5,
            }

        else:
            print("Opción no válida, intenta otra vez.\n")

personaje = elegir_personaje()
print(personaje, "\n")

dron = {
    "nivel": 1,
    "vida": 50,
    "fuerza": 5,
    "defensa": 5,
    "velocidad": 10,
    "critico": 5,
}

monedas = {
    "monedas":0,
}

def subir_nivel(exp):

    personaje["experiencia"] += exp

    while personaje["experiencia"] >= 100:
        personaje["nivel"] += 1
        personaje["experiencia"] -= 100
        print("\n¡Has subido de nivel!")

        print("\nEstadísticas actuales:")
        print(personaje, "\n")

        puntos = 3

        while puntos > 0:
            elegir = input(f"Tienes {puntos} punto/s para subir estadísticas, elige la estadística a la que sumarle 3 puntos (Vida/Fuerza/Defensa/Velocidad/Critico): ").lower()

            while elegir not in personaje:
                elegir = input(f"No has elegido una estadística válida, elige otra nueva, te quedan {puntos} punto/s: ")

            if elegir == "vida":
                personaje["vida maxima"] += 10
            else:
                personaje[elegir] += 3

            puntos -= 1

        print("\nEstadísticas finales:")
        print(personaje)
        print(f"\nMonedas: {monedas}")

def escalado_nivel(nivel):
    if nivel > 1:
        vida = dron["vida"] + (nivel * 10)
        fuerza = dron["fuerza"] + (nivel * 2)
        defensa = dron["defensa"] + (nivel * 2)
        velocidad = dron["velocidad"] + nivel
        critico = dron["critico"]
    else:
        vida = dron["vida"]
        fuerza = dron["fuerza"]
        defensa = dron["defensa"]
        velocidad = dron["velocidad"]
        critico = dron["critico"]

    return {
        "vida": vida,
        "fuerza": fuerza,
        "defensa": defensa,
        "velocidad": velocidad,
        "critico": critico
    }

def ataque_personaje():
    dado = random.randint(1,10)
    dado_critico_pj = random.randint(1, 100)

    if dado == 1:
        fuerza_p = personaje["fuerza"]
        if 1 <= dado_critico_pj <= personaje["critico"]:
            fuerza_p *= 2
            print("¡Ataque crítico!")
            return fuerza_p
        else:
            return fuerza_p
    elif 2 <= dado <= 6:
        fuerza_p = personaje["fuerza"] + 1
        if 1 <= dado_critico_pj <= personaje["critico"]:
            fuerza_p *= 2
            print("¡Ataque crítico!")
            return fuerza_p
        else:
            return fuerza_p
    elif 7 <= dado <= 9:
        fuerza_p = personaje["fuerza"] + 3
        if 1 <= dado_critico_pj <= personaje["critico"]:
            fuerza_p *= 2
            print("¡Ataque crítico!")
            return fuerza_p
        else:
            return fuerza_p
    else:
        fuerza_p = personaje["fuerza"] + 5
        if 1 <= dado_critico_pj <= personaje["critico"]:
            fuerza_p *= 2
            print("¡Ataque crítico!")
            return fuerza_p
        else:
            return fuerza_p

def enemigo_dron():

    dado2 = random.randint(1, 5)

    if dado2 in (1,2,3,4):
        nivel = 1
    else:
        nivel = 2

    print(f"Te enfrentas a un dron de nivel {nivel}\n")

    dron_escalado = escalado_nivel(nivel)

    while True:
        print("|MENÚ DE COMBATE|")
        print("1. Atacar")
        print("2. Objetos")

        dado = random.randint(1,10)
        dado_critico_dron = random.randint(1, 100)

        opcion = input("Elige que hacer: ")
        print()

        if opcion == "1":
            print("1. Ataque físico")
            print("2. Habilidades")

            opcion = input("Elige que hacer: ")

            if opcion == "1":

                if personaje["velocidad"] > dron_escalado["velocidad"]:
                    turno = "pj"
                elif personaje["velocidad"] < dron_escalado["velocidad"]:
                    turno = "dron"
                else:
                    turno = random.choice(["pj", "dron"])

                if turno == "pj":

                    print("Atacas primero")

                    ataque_p = ataque_personaje()

                    dron_escalado["vida"] -= ataque_p

                    print(f"Le haces {ataque_p} de daño al dron")
                    print(f"Vida del dron: {dron_escalado["vida"]}\n")

                    if dron_escalado["vida"] <= 0:
                        print("Has derrotado al dron\n")

                        exp = 0
                        exp += random.randint(100, 110)
                        print(f"El dron te da {exp} de experiencia\n")

                        monedas_dron = random.randint(15, 20)
                        monedas["monedas"] += monedas_dron
                        print(f"El dron ha soltado {monedas_dron} monedas")

                        return exp

                    if dado == 1:
                        fuerza_d = dron_escalado["fuerza"]
                        if 1 <= dado_critico_dron <= dron_escalado["critico"]:
                            fuerza_d *= 2
                            ataque_d = fuerza_d - personaje["defensa"]
                            print("¡Ataque crítico!")
                            print(f"El dron enemigo te hace {ataque_d} de daño")
                        else:
                            ataque_d = fuerza_d - personaje["defensa"]
                            print(f"El dron enemigo te hace {ataque_d} de daño")
                    elif 2 <= dado <= 6:
                        fuerza_d = dron_escalado["fuerza"] + 1
                        if 1 <= dado_critico_dron <= dron_escalado["critico"]:
                            fuerza_d *= 2
                            ataque_d = fuerza_d - personaje["defensa"]
                            print("¡Ataque crítico!")
                            print(f"El dron enemigo te hace {ataque_d} de daño")
                        else:
                            ataque_d = fuerza_d - personaje["defensa"]
                            print(f"El dron enemigo te hace {ataque_d} de daño")
                    elif 7 <= dado <= 9:
                        fuerza_d = dron_escalado["fuerza"] + 3
                        if 1 <= dado_critico_dron <= dron_escalado["critico"]:
                            fuerza_d *= 2
                            ataque_d = fuerza_d - personaje["defensa"]
                            print("¡Ataque crítico!")
                            print(f"El dron enemigo te hace {ataque_d} de daño")
                        else:
                            ataque_d = fuerza_d - personaje["defensa"]
                            print(f"El dron enemigo te hace {ataque_d} de daño")
                    else:
                        fuerza_d = dron_escalado["fuerza"] + 5
                        if 1 <= dado_critico_dron <= dron_escalado["critico"]:
                            fuerza_d *= 2
                            ataque_d = fuerza_d - personaje["defensa"]
                            print("¡Ataque crítico!")
                            print(f"El dron enemigo te hace {ataque_d} de daño")
                        else:
                            ataque_d = fuerza_d - personaje["defensa"]
                            print(f"El dron enemigo te hace {ataque_d} de daño")

                    personaje["vida"] -= ataque_d

                    print(f"Tu vida: {personaje["vida"]}\n")

                    if personaje["vida"] <= 0:
                        print("Has muerto")

                        return 0

                if turno == "dron":

                    print("El dron ataca primero")

                    if dado == 1:
                        fuerza_d = dron_escalado["fuerza"]
                        if 1 <= dado_critico_dron <= dron_escalado["critico"]:
                            fuerza_d *= 2
                            ataque_d = fuerza_d - personaje["defensa"]
                            print("¡Ataque crítico!")
                            print(f"El dron enemigo te hace {ataque_d} de daño")
                        else:
                            ataque_d = fuerza_d - personaje["defensa"]
                            print(f"El dron enemigo te hace {ataque_d} de daño")
                    elif 2 <= dado <= 6:
                        fuerza_d = dron_escalado["fuerza"] + 1
                        if 1 <= dado_critico_dron <= dron_escalado["critico"]:
                            fuerza_d *= 2
                            ataque_d = fuerza_d - personaje["defensa"]
                            print("¡Ataque crítico!")
                            print(f"El dron enemigo te hace {ataque_d} de daño")
                        else:
                            ataque_d = fuerza_d - personaje["defensa"]
                            print(f"El dron enemigo te hace {ataque_d} de daño")
                    elif 7 <= dado <= 9:
                        fuerza_d = dron_escalado["fuerza"] + 3
                        if 1 <= dado_critico_dron <= dron_escalado["critico"]:
                            fuerza_d *= 2
                            ataque_d = fuerza_d - personaje["defensa"]
                            print("¡Ataque crítico!")
                            print(f"El dron enemigo te hace {ataque_d} de daño")
                        else:
                            ataque_d = fuerza_d - personaje["defensa"]
                            print(f"El dron enemigo te hace {ataque_d} de daño")
                    else:
                        fuerza_d = dron_escalado["fuerza"] + 5
                        if 1 <= dado_critico_dron <= dron_escalado["critico"]:
                            fuerza_d *= 2
                            ataque_d = fuerza_d - personaje["defensa"]
                            print("¡Ataque crítico!")
                            print(f"El dron enemigo te hace {ataque_d} de daño")
                        else:
                            ataque_d = fuerza_d - personaje["defensa"]
                            print(f"El dron enemigo te hace {ataque_d} de daño")

                    personaje["vida"] -= ataque_d

                    print(f"Tu vida: {personaje["vida"]}\n")

                    if personaje["vida"] <= 0:
                        print("Has muerto")

                        return 0

                    ataque_p = ataque_personaje()

                    dron_escalado["vida"] -= ataque_p

                    print(f"Le haces {ataque_p} de daño al dron")
                    print(f"Vida del dron: {dron_escalado["vida"]}\n")

                    if dron_escalado["vida"] <= 0:
                        print("Has derrotado al dron\n")

                        exp = 0
                        exp += random.randint(100, 110)
                        print(f"El dron te da {exp} de experiencia\n")

                        monedas_dron = random.randint(15, 20)
                        monedas["monedas"] += monedas_dron
                        print(f"El dron ha soltado {monedas_dron} monedas")

                        return exp

            elif opcion == "2":
                print()

        elif opcion == "2":
            print()



exp = enemigo_dron()
subir_nivel(exp)
