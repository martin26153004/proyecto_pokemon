# Simulador de Equipo Pokémon

## Descripción

Proyecto desarrollado en Python utilizando Programación Orientada a Objetos (POO). El sistema permite administrar un equipo Pokémon mediante un menú interactivo en consola.

## Funcionalidades

- Capturar Pokémon de tipo Fuego, Agua y Planta.
- Entrenar Pokémon para aumentar su nivel y estadísticas.
- Atacar a otros Pokémon considerando ventajas y desventajas de tipo.
- Consultar la información de todos los Pokémon capturados.
- Liberar Pokémon del equipo.
- Mostrar el total de Pokémon activos.

## Conceptos Utilizados

- Clases y objetos
- Herencia
- Polimorfismo
- Encapsulamiento
- Métodos de instancia
- Métodos de clase
- Métodos estáticos
- Constructores y destructores
- Manejo de excepciones

## Estructura del Proyecto

```text
pokemon_simulator/
│
├── main.py
│
└── clases/
    └── pokemon.py
```

## Tipos de Pokémon

- Fuego: fuerte contra Planta y débil contra Agua.
- Agua: fuerte contra Fuego y débil contra Planta.
- Planta: fuerte contra Agua y débil contra Fuego.

## Ejecución

Ubicarse en la carpeta del proyecto y ejecutar:

```bash
python main.py
```

## Menú Principal

```text
1. Capturar Pokémon
2. Entrenar Pokémon
3. Atacar
4. Ver información
5. Total de Pokémon
6. Liberar Pokémon
7. Salir
```
