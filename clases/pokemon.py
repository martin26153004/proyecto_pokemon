class Pokemon:
    """Clase base para representar un Pokémon."""

    # Atributo de clase para contar los Pokémon activos.
    _contador_pokemons = 0

    def __init__(self, nombre, ataque, defensa, salud):
        """
        Constructor de la clase Pokemon.

        Recibe el nombre, ataque, defensa y salud.
        El nivel inicia automáticamente en 1.
        """

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError(
                "El nombre del Pokémon no puede estar vacío."
            )

        if not self.validar_estadistica(ataque):
            raise ValueError(
                "El ataque debe ser un número positivo."
            )

        if not self.validar_estadistica(defensa):
            raise ValueError(
                "La defensa debe ser un número positivo."
            )

        if not self.validar_estadistica(salud):
            raise ValueError(
                "La salud debe ser un número positivo."
            )

        self.nombre = nombre.strip()
        self.nivel = 1
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud
        self.salud_maxima = salud

        # Atributo protegido.
        self._tipo = "Sin tipo"

        # Ayuda a evitar que el contador disminuya dos veces.
        self._contabilizado = True

        Pokemon._contador_pokemons += 1

        print(
            f"¡{self.nombre} ha sido capturado! 🎉"
        )

    def __del__(self):
        """
        Destructor.

        Se ejecuta cuando el objeto deja de existir.
        """

        if getattr(self, "_contabilizado", False):
            print(
                f"{self.nombre} ha sido liberado ✨"
            )

            Pokemon._contador_pokemons -= 1
            self._contabilizado = False

    @staticmethod
    def validar_estadistica(valor):
        """
        Método estático que valida que una estadística
        sea un número positivo.
        """

        es_numero = isinstance(valor, (int, float))
        no_es_booleano = not isinstance(valor, bool)

        return es_numero and no_es_booleano and valor > 0

    @classmethod
    def total_pokemons(cls):
        """
        Método de clase que devuelve el total
        de Pokémon activos.
        """

        return cls._contador_pokemons

    def subir_nivel(self):
        """
        Aumenta el nivel y mejora las estadísticas base.
        """

        self.nivel += 1

        # Mejoras básicas por subir de nivel.
        self.ataque += 2
        self.defensa += 2
        self.salud_maxima += 5

        # También recupera cinco puntos de salud.
        self.salud += 5

        if self.salud > self.salud_maxima:
            self.salud = self.salud_maxima

    def entrenar(
        self,
        stat1=None,
        stat2=None,
        stat3=None
    ):
        """
        Entrena al Pokémon.

        Si no se mandan argumentos, mejora ataque,
        defensa y salud.

        Ejemplos:

        pokemon.entrenar()

        pokemon.entrenar("ataque")

        pokemon.entrenar("ataque", "defensa")
        """

        estadisticas = []

        if stat1 is not None:
            estadisticas.append(
                str(stat1).strip().lower()
            )

        if stat2 is not None:
            estadisticas.append(
                str(stat2).strip().lower()
            )

        if stat3 is not None:
            estadisticas.append(
                str(stat3).strip().lower()
            )

        # Si no se enviaron argumentos,
        # se mejoran todas las estadísticas.
        if not estadisticas:
            estadisticas = [
                "ataque",
                "defensa",
                "salud"
            ]

        estadisticas_permitidas = {
            "ataque",
            "defensa",
            "salud"
        }

        for estadistica in estadisticas:
            if estadistica not in estadisticas_permitidas:
                raise ValueError(
                    "La estadística debe ser "
                    "'ataque', 'defensa' o 'salud'."
                )

        # Primero sube el nivel y recibe las mejoras base.
        self.subir_nivel()

        # Las estadísticas seleccionadas reciben
        # una mejora adicional.
        for estadistica in set(estadisticas):

            if estadistica == "ataque":
                self.ataque += 3

            elif estadistica == "defensa":
                self.defensa += 3

            elif estadistica == "salud":
                self.salud_maxima += 5
                self.salud += 5

                if self.salud > self.salud_maxima:
                    self.salud = self.salud_maxima

        print(
            f"{self.nombre} subió al nivel "
            f"{self.nivel}. ⭐"
        )

        print(
            "Estadísticas mejoradas: "
            + ", ".join(estadisticas)
        )

    def calcular_dano_base(self, objetivo):
        """
        Calcula el daño básico.

        El daño mínimo siempre será 1.
        """

        dano = self.ataque - objetivo.defensa

        if dano < 1:
            dano = 1

        return dano

    def validar_ataque(self, objetivo):
        """
        Verifica que el ataque pueda realizarse.
        """

        if not isinstance(objetivo, Pokemon):
            raise TypeError(
                "El objetivo debe ser un Pokémon."
            )

        if self.salud == 0:
            raise ValueError(
                f"{self.nombre} está debilitado "
                "y no puede atacar."
            )

        if objetivo.salud == 0:
            raise ValueError(
                f"{objetivo.nombre} ya está debilitado."
            )

        if self is objetivo:
            raise ValueError(
                "Un Pokémon no puede atacarse "
                "a sí mismo."
            )

    def atacar(self, objetivo):
        """
        Simula un ataque básico contra otro Pokémon.

        Este método será redefinido por las
        clases derivadas.
        """

        self.validar_ataque(objetivo)

        dano = self.calcular_dano_base(objetivo)

        print(
            f"{self.nombre} ataca a "
            f"{objetivo.nombre}."
        )

        print(
            f"El ataque causa {dano} puntos de daño."
        )

        objetivo.recibir_dano(dano)

        return dano

    def recibir_dano(self, cantidad):
        """
        Reduce la salud del Pokémon.
        """

        if not isinstance(cantidad, (int, float)):
            raise TypeError(
                "La cantidad de daño debe ser numérica."
            )

        if cantidad < 0:
            raise ValueError(
                "El daño no puede ser negativo."
            )

        self.salud -= cantidad

        if self.salud < 0:
            self.salud = 0

        print(
            f"Salud restante de {self.nombre}: "
            f"{self.salud}/{self.salud_maxima}"
        )

        if self.salud == 0:
            print(
                f"¡{self.nombre} se ha debilitado! 💫"
            )

    def mostrar_info(self):
        """
        Muestra toda la información del Pokémon.
        """

        if self.salud == 0:
            estado = "Debilitado"
        else:
            estado = "Activo"

        print("-" * 40)
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self._tipo}")
        print(f"Nivel: {self.nivel}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")

        print(
            f"Salud: "
            f"{self.salud}/{self.salud_maxima}"
        )

        print(f"Estado: {estado}")

    def atacar_con_ventaja(
        self,
        objetivo,
        tipo_fuerte,
        tipo_debil
    ):
        """
        Método auxiliar para aplicar las ventajas
        y desventajas de tipo.
        """

        self.validar_ataque(objetivo)

        dano = self.calcular_dano_base(objetivo)

        mensaje = "El ataque tiene efectividad normal."

        if objetivo._tipo == tipo_fuerte:
            dano *= 2
            mensaje = "¡Es muy efectivo!"

        elif objetivo._tipo == tipo_debil:
            dano = dano / 2

            # Si el resultado tiene decimales,
            # se convierte hacia abajo.
            dano = int(dano)

            if dano < 1:
                dano = 1

            mensaje = "No es muy efectivo..."

        print()
        print(
            f"{self.nombre} ataca a "
            f"{objetivo.nombre}."
        )

        print(mensaje)
        print(f"Daño causado: {dano}")

        objetivo.recibir_dano(dano)

        return dano


class PokemonFuego(Pokemon):
    """Clase derivada para Pokémon de tipo Fuego."""

    def __init__(
        self,
        nombre,
        ataque,
        defensa,
        salud
    ):
        super().__init__(
            nombre,
            ataque,
            defensa,
            salud
        )

        self._tipo = "Fuego"

    def atacar(self, objetivo):
        """
        Fuego es fuerte contra Planta
        y débil contra Agua.
        """

        return self.atacar_con_ventaja(
            objetivo,
            "Planta",
            "Agua"
        )

    def mostrar_info(self):
        """
        Muestra primero la información de la clase
        base y después el mensaje del tipo Fuego.
        """

        super().mostrar_info()
        print("🔥 ¡Arde con pasión!")


class PokemonAgua(Pokemon):
    """Clase derivada para Pokémon de tipo Agua."""

    def __init__(
        self,
        nombre,
        ataque,
        defensa,
        salud
    ):
        super().__init__(
            nombre,
            ataque,
            defensa,
            salud
        )

        self._tipo = "Agua"

    def atacar(self, objetivo):
        """
        Agua es fuerte contra Fuego
        y débil contra Planta.
        """

        return self.atacar_con_ventaja(
            objetivo,
            "Fuego",
            "Planta"
        )

    def mostrar_info(self):
        """
        Muestra primero la información de la clase
        base y después el mensaje del tipo Agua.
        """

        super().mostrar_info()
        print("💧 ¡Fluye como el río!")


class PokemonPlanta(Pokemon):
    """Clase derivada para Pokémon de tipo Planta."""

    def __init__(
        self,
        nombre,
        ataque,
        defensa,
        salud
    ):
        super().__init__(
            nombre,
            ataque,
            defensa,
            salud
        )

        self._tipo = "Planta"

    def atacar(self, objetivo):
        """
        Planta es fuerte contra Agua
        y débil contra Fuego.
        """

        return self.atacar_con_ventaja(
            objetivo,
            "Agua",
            "Fuego"
        )

    def mostrar_info(self):
        """
        Muestra primero la información de la clase
        base y después el mensaje del tipo Planta.
        """

        super().mostrar_info()
        print("🌿 ¡Crece con fuerza!")