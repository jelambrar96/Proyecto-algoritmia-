# 🏆 Simulador de Torneo Eliminatorio

Un simulador interactivo de torneo de fútbol eliminatorio que permite simular partidos con resultados aleatorios y determinar un campeón final.

## 📋 Descripción

Este programa simula un torneo eliminatorio clásico donde:
- Los equipos se enfrentan en partidos de ida
- El ganador avanza a la siguiente ronda
- En caso de empate, se aplica la regla del "gol de oro"
- El torneo continúa hasta determinar un campeón

## ✨ Características Principales

- ✅ Modo predeterminado con 8 equipos precargados
- ✅ Opción para ingresar equipos personalizados (4 u 8 equipos)
- ✅ Simulación automática de resultados aleatorios (0-5 goles por equipo)
- ✅ Resolución automática de empates con "gol de oro"
- ✅ Interfaz visual con emojis y separadores
- ✅ Muestra las rondas: Cuartos de Final → Semifinales → Gran Final
- ✅ Presentación destacada del campeón

## 💻 Requisitos

- Python 3.x
- Librería `random` (incluida en Python por defecto)

## 🚀 Cómo Usar

### Ejecución Básica

```bash
python Simular_partido.py
```

### Paso a Paso

1. **Elegir Equipos:**
   - Opción 1: Usar los 8 equipos predeterminados (Leones FC, Tigres SC, etc.)
   - Opción 2: Ingresar tus propios equipos (4 u 8 equipos)

2. **Ver Resultados:**
   - El programa muestra cada partido con su marcador
   - Indica automáticamente al ganador de cada encuentro
   - Continúa hasta determinar el campeón final

3. **Resultado Final:**
   - Se muestra el equipo campeón destacado con emojis

## 📖 Ejemplos de Funcionamiento

### Ejemplo 1: Usando Equipos Predeterminados

```
🏆
      TORNEO ELIMINATORIO
────────────────────────────────────────────────

¿Deseas usar los equipos predeterminados?
  [1] Sí, usar equipos predeterminados
  [2] No, ingresar mis propios equipos

→ Elige una opción: 1

────────────────────────────────────────────────
  Participantes (8 equipos):
    1. Leones FC
    2. Tigres SC
    3. Águilas CF
    4. Lobos United
    5. Zorros AC
    6. Osos FC
    7. Delfines SC
    8. Tiburones CF
────────────────────────────────────────────────

        CUARTOS DE FINAL
────────────────────────────────────────────────

  Tigres SC                 3 - 1                Delfines SC
  ✅ Avanza: Tigres SC

  Leones FC                 2 - 2                Osos FC
  ✅ Avanza: Osos FC

  Águilas CF                1 - 0                Lobos United
  ✅ Avanza: Águilas CF

  Zorros AC                 4 - 2                Tiburones CF
  ✅ Avanza: Zorros AC
────────────────────────────────────────────────

         SEMIFINALES
────────────────────────────────────────────────

  Tigres SC                 2 - 1                Osos FC
  ✅ Avanza: Tigres SC

  Águilas CF                3 - 2                Zorros AC
  ✅ Avanza: Águilas CF
────────────────────────────────────────────────

       ⭐ GRAN FINAL ⭐
────────────────────────────────────────────────

  Tigres SC                 2 - 1                Águilas CF
  ✅ Avanza: Tigres SC
────────────────────────────────────────────────

🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆
       🥇 CAMPEÓN DEL TORNEO
           TIGRES SC
🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆
```

### Ejemplo 2: Usando Equipos Personalizados (4 equipos)

```
🏆
      TORNEO ELIMINATORIO
────────────────────────────────────────────────

¿Deseas usar los equipos predeterminados?
  [1] Sí, usar equipos predeterminados
  [2] No, ingresar mis propios equipos

→ Elige una opción: 2

¿Cuántos equipos participarán? (debe ser 4 u 8)
→ Cantidad de equipos: 4

Ingresa los 4 nombres de los equipos:

  Equipo 1: Real Madrid
  Equipo 2: Barcelona
  Equipo 3: Manchester City
  Equipo 4: Liverpool

────────────────────────────────────────────────
  Participantes (4 equipos):
    1. Barcelona
    2. Liverpool
    3. Real Madrid
    4. Manchester City
────────────────────────────────────────────────

         SEMIFINALES
────────────────────────────────────────────────

  Barcelona                 2 - 0                Liverpool
  ✅ Avanza: Barcelona

  Real Madrid               3 - 3                Manchester City
  ✅ Avanza: Manchester City
────────────────────────────────────────────────

       ⭐ GRAN FINAL ⭐
────────────────────────────────────────────────

  Barcelona                 1 - 0                Manchester City
  ✅ Avanza: Barcelona
────────────────────────────────────────────────

🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆
       🥇 CAMPEÓN DEL TORNEO
           BARCELONA
🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆
```

## 🔧 Descripción de Funciones

### `elegir_equipos()`
- Muestra un menú para elegir entre equipos predeterminados o personalizados
- Si elige personalizados, solicita la cantidad (4 u 8) y los nombres
- **Retorna:** Lista de equipos seleccionados

### `simular_partido(equipo_a, equipo_b)`
- Simula un partido entre dos equipos
- Genera goles aleatorios entre 0 y 5 para cada equipo
- Si hay empate, aplica "gol de oro" (suma 1 gol al primer equipo)
- **Parámetros:** `equipo_a`, `equipo_b` (nombres de equipos)
- **Retorna:** `(ganador, perdedor, goles_a, goles_b)`

### `nombre_ronda(equipos_restantes)`
- Devuelve el nombre formateado de la ronda actual
- 8 equipos → "CUARTOS DE FINAL"
- 4 equipos → "SEMIFINALES"
- 2 equipos → "⭐ GRAN FINAL ⭐"
- **Parámetro:** Cantidad de equipos restantes
- **Retorna:** Nombre de la ronda como string

### `simular_torneo(equipos)`
- Controla todo el flujo del torneo eliminatorio
- Mezcla aleatoriamente el orden de equipos
- Simula cada ronda hasta quedar un campeón
- Muestra toda la información en pantalla
- **Parámetro:** Lista de equipos
- **Retorna:** Nombre del equipo campeón

### `mostrar_campeon(campeon)`
- Muestra el equipo campeón de forma destacada
- Utiliza emojis de trofeo para una presentación visual
- **Parámetro:** Nombre del equipo campeón

## 📊 Flujo del Programa

```
Inicio
  ↓
Elegir Equipos (Predeterminados o Personalizados)
  ↓
Simular Torneo (Rondas sucesivas: Cuartos → Semifinales → Final)
  ↓
Mostrar Campeón
  ↓
Fin
```

## 🎲 Reglas de la Simulación

1. **Goles Aleatorios:** Cada equipo puede anotar entre 0 y 5 goles
2. **Gol de Oro:** Si el marcador termina empatado, el primer equipo suma 1 gol adicional
3. **Un Solo Partido:** No hay vuelta, es eliminatorio directo
4. **Avance:** Solo el ganador continúa en el torneo

## 💡 Casos de Uso

- **Educación:** Aprender sobre algoritmos de torneos y estructuras de datos
- **Entretenimiento:** Simular torneos imaginarios con tus equipos favoritos
- **Proyectos:** Base para expandir a torneos más complejos (round-robin, playoff, etc.)

## 📝 Notas

- Los resultados son completamente aleatorios, por lo que cada ejecución será diferente
- El torneo siempre comienza con 4 u 8 equipos (números potencia de 2)
- Los nombres de equipos no pueden repetirse al ingresar equipos personalizados
- Los equipos se mezclan aleatoriamente al inicio del torneo

## 🔮 Posibles Extensiones

- Agregue múltiples partidos (playoff)
- Implemente clasificación por puntos
- Agregue apuestas y predicciones
- Cree historial de torneos
- Implemente diferentes tipos de torneos (round-robin, suizo, etc.)

---

**Autor:** Proyecto Algoritmia  
**Lenguaje:** Python 3.x  
**Última actualización:** 2026
