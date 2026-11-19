"""Control de temperatura en autoclave de alimentos (sensor MAX31855)."""

TEMPERATURA_INICIAL = 110
MAX_MUESTRAS = 20  # límite de ciclos de muestreo (evita bucle infinito)
UMBRAL_CRITICO = 130
UMBRAL_MINIMO = 115
UMBRAL_ESTABLE = 121


def simular_autoclave():
    """Simula el ciclo de control hasta una alerta o el límite de muestras."""
    temperatura = TEMPERATURA_INICIAL
    sistema_activo = True
    muestras = 0
    while sistema_activo and muestras < MAX_MUESTRAS:
        if temperatura > UMBRAL_CRITICO:
            print("ALERTA CRÍTICA: Parada de emergencia")
            sistema_activo = False
        elif temperatura < UMBRAL_MINIMO:
            print("Estado: Calentando autoclave")
            temperatura += 2
        elif UMBRAL_MINIMO <= temperatura <= UMBRAL_ESTABLE:
            print("Estado: Fase estable de esterilización")
            temperatura += 0  # en fase estable la temperatura se mantiene
        else:
            print("Estado: Enfriamiento activo")
            temperatura -= 3
        muestras += 1
    if muestras >= MAX_MUESTRAS:
        print("Límite de muestreo alcanzado, "
              "ciclo finalizado por control de tiempo")


if __name__ == "__main__":
    simular_autoclave()
