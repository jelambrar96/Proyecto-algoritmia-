import random

# ============================================================
#   🏆  SIMULADOR DE TORNEO ELIMINATORIO
# ============================================================

EQUIPOS_DEFAULT = [
    "Leones FC", "Tigres SC", "Águilas CF", "Lobos United",
    "Zorros AC",  "Osos FC",   "Delfines SC", "Tiburones CF"
]

SEPARADOR = "─" * 52

def elegir_equipos():
    print(f"\n{'🏆':^52}")
    print(f"{'TORNEO ELIMINATORIO':^52}")
    print(SEPARADOR)
    print("\n¿Deseas usar los equipos predeterminados?")
    print("  [1] Sí, usar equipos predeterminados")
    print("  [2] No, ingresar mis propios equipos")

    opcion = input("\n→ Elige una opción: ").strip()

    if opcion == "2":
        print("\n¿Cuántos equipos participarán? (debe ser 4 u 8)")
        while True:
            try:
                n = int(input("→ Cantidad de equipos: ").strip())
                if n in (4, 8):
                    break
                print("  ⚠ Solo se permiten 4 u 8 equipos.")
            except ValueError:
                print("  ⚠ Ingresa un número válido.")

        equipos = []
        print(f"\nIngresa los {n} nombres de los equipos:\n")
        for i in range(n):
            while True:
                nombre = input(f"  Equipo {i+1}: ").strip()
                if nombre and nombre not in equipos:
                    equipos.append(nombre)
                    break
                print("  ⚠ Nombre inválido o repetido, intenta de nuevo.")
    else:
        equipos = EQUIPOS_DEFAULT[:]

    return equipos


def simular_partido(equipo_a, equipo_b):
    goles_a = random.randint(0, 5)
    goles_b = random.randint(0, 5)
    if goles_a == goles_b:          # Gol de oro en caso de empate
        goles_a += 1
    ganador  = equipo_a if goles_a > goles_b else equipo_b
    perdedor = equipo_b if goles_a > goles_b else equipo_a
    return ganador, perdedor, goles_a, goles_b


def nombre_ronda(equipos_restantes):
    nombres = {8: "CUARTOS DE FINAL", 4: "SEMIFINALES", 2: "⭐ GRAN FINAL ⭐"}
    return nombres.get(equipos_restantes, f"RONDA ({equipos_restantes} equipos)")


def simular_torneo(equipos):
    random.shuffle(equipos)
    ronda = 1

    print(f"\n{SEPARADOR}")
    print(f"  Participantes ({len(equipos)} equipos):")
    for i, e in enumerate(equipos, 1):
        print(f"    {i:>2}. {e}")
    print(SEPARADOR)

    while len(equipos) > 1:
        print(f"\n  {nombre_ronda(len(equipos)):^48}")
        print(SEPARADOR)
        ganadores = []

        for i in range(0, len(equipos), 2):
            a, b = equipos[i], equipos[i + 1]
            ganador, _, ga, gb = simular_partido(a, b)

            marcador = f"{ga} - {gb}"
            print(f"\n  {a:<20} {marcador:^7} {b:>20}")
            print(f"  {'✅ Avanza: ' + ganador:^52}")
            ganadores.append(ganador)

        equipos = ganadores
        ronda += 1
        print(SEPARADOR)

    return equipos[0]


def mostrar_campeon(campeon):
    print(f"\n{'🏆' * 26}")
    print(f"  {'🥇 CAMPEÓN DEL TORNEO':^48}")
    print(f"  {campeon.upper():^48}")
    print(f"{'🏆' * 26}\n")


# ── Punto de entrada ─────────────────────────────────────────
if __name__ == "__main__":
    equipos = elegir_equipos()
    campeon = simular_torneo(equipos)
    mostrar_campeon(campeon)
