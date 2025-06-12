# Piedra, Papel o Tijera

## Manual de Usuario

### Descripción

Juego interactivo en consola donde el usuario compite contra la computadora en rondas de piedra, papel o tijera. El objetivo es ganar más rondas que la computadora antes de salir del juego.

### Instrucciones de uso

1. **Inicio del juego:**
   Al ejecutar el programa, se mostrará un mensaje de bienvenida indicando que el juego ha comenzado.

2. **Realizar una jugada:**
   El programa solicitará que escribas una de las siguientes opciones:
   - `piedra`
   - `papel`
   - `tijera`
   - También puedes escribir `salir` para finalizar el juego.

   Si la opción ingresada no es válida, se mostrará un mensaje de error y se solicitará una nueva entrada.

3. **Resultado de la ronda:**
   Se mostrará lo que eligió el usuario y la computadora, seguido del resultado (ganaste, perdió o empate). Luego se actualizará y mostrará el puntaje acumulado.

4. **Finalización:**
   Al escribir `salir`, el programa mostrará el puntaje final y dirá si el jugador ganó, perdió o empató contra la computadora.

## Manual Técnico

### Requisitos

- Python 3.x
- Consola o entorno de desarrollo compatible con Python (por ejemplo: IDLE, VS Code, terminal)

### Librerías utilizadas

- `random`: usada para que la computadora elija su jugada de forma aleatoria.

### Estructura del proyecto


### Arquitectura del código

- **Lista `opc`**: contiene las opciones válidas (`piedra`, `papel`, `tijera`).
- **Diccionario `gana_a`**: define qué opción vence a cuál (por ejemplo, piedra gana a tijera).

#### Funciones principales

- `pedir_opcion()`:
  Solicita al usuario una opción y valida que sea correcta o permita salir.

- `ronda(jugador, pc)`:
  Compara las elecciones del jugador y la computadora y determina el resultado de la ronda.

- `jugar()`:
  Controla el flujo general del juego, gestiona el puntaje y finaliza cuando el usuario lo indica.

### Posibles mejoras

- Permitir mayúsculas o variantes comunes de entrada.
- Agregar interfaz gráfica con `tkinter`.
- Registrar estadísticas o historial de partidas.
- Añadir soporte multijugador.
