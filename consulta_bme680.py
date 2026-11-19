"""Consulta segura del mapa de registros del sensor BME680 (I2C)."""

MAPA_BME680 = {
    "0x60": {
        "nombre": "Configuración de Filtro",
        "status": True,
        "calib_val": 12,
        "limit": 100,
    },
    "0x61": {
        "nombre": "Control de Gas",
        "status": True,
        "calib_val": 55,
        "limit": 200,
    },
    "0x62": {
        "nombre": "Datos de Humedad",
        "status": False,
        "calib_val": 88,
        "limit": 90,
    },
}

MAX_INTENTOS = 5
MENSAJE_ENTRADA = (
    "Dirección hex (ej. 0x60) o nombre del registro "
    "('salir' para terminar): "
)


def buscar_registro(entrada):
    """Devuelve (dirección, datos) o (None, None) si no existe."""
    entrada = entrada.strip().lower()
    direccion = entrada if entrada.startswith("0x") else "0x" + entrada
    datos = MAPA_BME680.get(direccion)
    if datos is not None:
        return direccion, datos
    for direccion, datos in MAPA_BME680.items():
        if datos.get("nombre", "").lower() == entrada:
            return direccion, datos
    return None, None


def mostrar_registro(direccion, datos):
    """Imprime las especificaciones de un registro."""
    print(f"\nRegistro {direccion} - {datos.get('nombre', 'N/A')}")
    print(f"  status    : {datos.get('status', 'N/A')}")
    print(f"  calib_val : {datos.get('calib_val', 'N/A')}")
    print(f"  limit     : {datos.get('limit', 'N/A')}\n")


def main():
    """Ciclo de consulta limitado a MAX_INTENTOS búsquedas."""
    intentos = 0
    while intentos < MAX_INTENTOS:
        consulta = input(MENSAJE_ENTRADA)
        if consulta.strip().lower() == "salir":
            break
        intentos += 1
        direccion, datos = buscar_registro(consulta)
        if datos is None:
            print(f"[Error] Registro '{consulta}' no existe. "
                  f"Intento {intentos}/{MAX_INTENTOS}\n")
        else:
            mostrar_registro(direccion, datos)
    else:
        print("Se alcanzó el máximo de intentos. Programa finalizado.")


if __name__ == "__main__":
    main()
