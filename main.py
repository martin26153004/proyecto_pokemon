import gc

from clases.pokemon import (
    Pokemon,
    PokemonFuego,
    PokemonAgua,
    PokemonPlanta
)


def leer_numero_positivo(mensaje):
    """
    Solicita un número positivo al usuario.

    El ciclo se repite hasta que el usuario
    escriba un valor correcto.
    """

    while True:
        try:
            valor = float(input(mensaje))

            if not Pokemon.validar_estadistica(valor):
                raise ValueError(
                    "El valor debe ser mayor que cero."
                )

            # Si el valor no tiene decimales,
            # se devuelve como número entero.
            if valor.is_integer():
                return int(valor)

            return valor

        except ValueError as error:
            print(
                f"Entrada no válida: {error}"
            )


def mostrar_lista(equipo):
    """
    Muestra los Pokémon que se encuentran
    actualmente en el equipo.
    """

    if len(equipo) == 0:
        print(
            "No hay Pokémon capturados."
        )
        return False

    print()
    print("Pokémon del equipo:")
    print("-" * 45)

    for indice, pokemon in enumerate(
        equipo,
        start=1
    ):
        print(
            f"{indice}. {pokemon.nombre} | "
            f"Tipo: {pokemon._tipo} | "
            f"Nivel: {pokemon.nivel} | "
            f"Salud: "
            f"{pokemon.salud}/{pokemon.salud_maxima}"
        )

    print("-" * 45)

    return True


def seleccionar_pokemon(
    equipo,
    mensaje="Selecciona un Pokémon: "
):
    """
    Permite seleccionar un Pokémon utilizando
    su número dentro de la lista.
    """

    if not mostrar_lista(equipo):
        return None

    try:
        opcion = int(input(mensaje))

        posicion = opcion - 1

        if posicion < 0:
            raise IndexError

        if posicion >= len(equipo):
            raise IndexError

        return equipo[posicion]

    except ValueError:
        print(
            "Debes escribir un número entero."
        )

    except IndexError:
        print(
            "La opción seleccionada no existe."
        )

    return None


def capturar_pokemon(equipo):
    """
    Solicita los datos necesarios y crea
    un Pokémon del tipo seleccionado.
    """

    print()
    print("=== CAPTURAR POKÉMON ===")

    nombre = input(
        "Nombre del Pokémon: "
    ).strip()

    if not nombre:
        raise ValueError(
            "El nombre no puede estar vacío."
        )

    tipo = input(
        "Tipo (Fuego/Agua/Planta): "
    ).strip().capitalize()

    if tipo not in [
        "Fuego",
        "Agua",
        "Planta"
    ]:
        raise ValueError(
            "El tipo debe ser Fuego, Agua o Planta."
        )

    ataque = leer_numero_positivo(
        "Puntos de ataque: "
    )

    defensa = leer_numero_positivo(
        "Puntos de defensa: "
    )

    salud = leer_numero_positivo(
        "Puntos de salud: "
    )

    if tipo == "Fuego":
        nuevo_pokemon = PokemonFuego(
            nombre,
            ataque,
            defensa,
            salud
        )

    elif tipo == "Agua":
        nuevo_pokemon = PokemonAgua(
            nombre,
            ataque,
            defensa,
            salud
        )

    else:
        nuevo_pokemon = PokemonPlanta(
            nombre,
            ataque,
            defensa,
            salud
        )

    equipo.append(nuevo_pokemon)

    print(
        f"{nuevo_pokemon.nombre} fue agregado "
        "correctamente al equipo."
    )


def entrenar_pokemon(equipo):
    """
    Selecciona un Pokémon y mejora
    sus estadísticas.
    """

    print()
    print("=== ENTRENAR POKÉMON ===")

    pokemon = seleccionar_pokemon(equipo)

    if pokemon is None:
        return

    if pokemon.salud == 0:
        print(
            f"{pokemon.nombre} está debilitado, "
            "pero puede entrenar para mejorar."
        )

    print()
    print("Selecciona cómo deseas entrenarlo:")
    print("1. Mejorar todas las estadísticas")
    print("2. Mejorar solamente el ataque")
    print("3. Mejorar solamente la defensa")
    print("4. Mejorar solamente la salud")
    print("5. Elegir varias estadísticas")

    opcion = input(
        "Selecciona una opción: "
    ).strip()

    if opcion == "1":
        # Usa los parámetros por defecto.
        pokemon.entrenar()

    elif opcion == "2":
        pokemon.entrenar("ataque")

    elif opcion == "3":
        pokemon.entrenar("defensa")

    elif opcion == "4":
        pokemon.entrenar("salud")

    elif opcion == "5":
        print()
        print(
            "Escribe hasta tres estadísticas "
            "separadas por comas."
        )

        print(
            "Puedes usar: ataque, defensa y salud."
        )

        entrada = input(
            "Estadísticas: "
        ).strip()

        if not entrada:
            raise ValueError(
                "Debes escribir al menos "
                "una estadística."
            )

        estadisticas = []

        for dato in entrada.split(","):
            dato_limpio = dato.strip().lower()

            if dato_limpio:
                estadisticas.append(
                    dato_limpio
                )

        if len(estadisticas) > 3:
            raise ValueError(
                "Solo puedes seleccionar "
                "hasta tres estadísticas."
            )

        argumentos = estadisticas.copy()

        while len(argumentos) < 3:
            argumentos.append(None)

        pokemon.entrenar(
            argumentos[0],
            argumentos[1],
            argumentos[2]
        )

    else:
        print(
            "Opción de entrenamiento no válida."
        )


def realizar_ataque(equipo):
    """
    Selecciona un Pokémon atacante y otro
    Pokémon como objetivo.
    """

    print()
    print("=== ATAQUE POKÉMON ===")

    if len(equipo) < 2:
        print(
            "Se necesitan al menos dos Pokémon "
            "para realizar un ataque."
        )
        return

    atacante = seleccionar_pokemon(
        equipo,
        "Selecciona al Pokémon atacante: "
    )

    if atacante is None:
        return

    if atacante.salud == 0:
        print(
            f"{atacante.nombre} está debilitado "
            "y no puede atacar."
        )
        return

    objetivo = seleccionar_pokemon(
        equipo,
        "Selecciona al Pokémon objetivo: "
    )

    if objetivo is None:
        return

    if atacante is objetivo:
        print(
            "Un Pokémon no puede atacarse "
            "a sí mismo."
        )
        return

    if objetivo.salud == 0:
        print(
            f"{objetivo.nombre} ya está debilitado."
        )
        return

    atacante.atacar(objetivo)


def ver_informacion(equipo):
    """
    Muestra la información de todos los Pokémon.

    Aquí se aplica polimorfismo porque cada objeto
    ejecuta su propia versión de mostrar_info().
    """

    print()
    print("=== INFORMACIÓN DEL EQUIPO ===")

    if len(equipo) == 0:
        print(
            "No hay Pokémon capturados."
        )
        return

    for pokemon in equipo:
        pokemon.mostrar_info()

    print("-" * 40)


def mostrar_total_pokemons():
    """
    Muestra el total de Pokémon activos
    utilizando el método de clase.
    """

    total = Pokemon.total_pokemons()

    print()
    print("=== ESTADÍSTICAS GLOBALES ===")

    print(
        f"Total de Pokémon activos: {total}"
    )


def liberar_pokemon(equipo):
    """
    Elimina un Pokémon del equipo.
    """

    print()
    print("=== LIBERAR POKÉMON ===")

    pokemon = seleccionar_pokemon(equipo)

    if pokemon is None:
        return

    nombre = pokemon.nombre

    confirmacion = input(
        f"¿Seguro que deseas liberar a "
        f"{nombre}? (s/n): "
    ).strip().lower()

    if confirmacion != "s":
        print(
            "La liberación fue cancelada."
        )
        return

    posicion = equipo.index(pokemon)

    # Se elimina la referencia local.
    del pokemon

    # Se elimina el objeto de la lista.
    pokemon_eliminado = equipo.pop(posicion)

    # Se elimina la última referencia.
    del pokemon_eliminado

    # Fuerza al recolector de basura para intentar
    # ejecutar inmediatamente el destructor.
    gc.collect()

    print(
        f"{nombre} fue eliminado del equipo."
    )


def mostrar_menu():
    """Muestra el menú principal."""

    print()
    print("=" * 45)
    print("        SIMULADOR DE EQUIPO POKÉMON")
    print("=" * 45)
    print("1. Capturar Pokémon")
    print("2. Entrenar Pokémon")
    print("3. Atacar")
    print("4. Ver información")
    print("5. Total de Pokémon")
    print("6. Liberar Pokémon")
    print("7. Salir")
    print("=" * 45)


def main():
    """
    Función principal del programa.
    """

    equipo = []

    while True:
        mostrar_menu()

        opcion = input(
            "Selecciona una opción: "
        ).strip()

        try:
            if opcion == "1":
                capturar_pokemon(equipo)

            elif opcion == "2":
                entrenar_pokemon(equipo)

            elif opcion == "3":
                realizar_ataque(equipo)

            elif opcion == "4":
                ver_informacion(equipo)

            elif opcion == "5":
                mostrar_total_pokemons()

            elif opcion == "6":
                liberar_pokemon(equipo)

            elif opcion == "7":
                print()
                print(
                    "¡Gracias por utilizar el "
                    "simulador Pokémon!"
                )
                break

            else:
                print(
                    "Opción no válida. "
                    "Selecciona un número del 1 al 7."
                )

        except ValueError as error:
            print(
                f"No se pudo realizar la operación: "
                f"{error}"
            )

        except TypeError as error:
            print(
                f"El tipo de dato no es correcto: "
                f"{error}"
            )

        except Exception as error:
            print(
                f"Ocurrió un error inesperado: "
                f"{error}"
            )


if __name__ == "__main__":
    main()