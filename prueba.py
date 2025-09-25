import requests
import json

# --- Configuración ---
# Reemplaza 'TU_CLAVE_API' con tu clave real
API_KEY = '4f66e02200c51e1a2466e66d1c7d8099'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def obtener_clima(ciudad):
    """
    Obtiene los datos del clima de una ciudad específica usando la API de OpenWeatherMap.
    """
    try:
        # Parámetros para la solicitud a la API
        parametros = {
            'q': ciudad,
            'appid': API_KEY,
            'units': 'metric',  # 'metric' para Celsius, 'imperial' para Fahrenheit
            'lang': 'es'      # Idioma de la descripción del clima
        }

        # Realiza la solicitud GET a la API
        print(f"Buscando el clima para '{ciudad}'...")
        respuesta = requests.get(BASE_URL, params=parametros)

        # Verifica si la solicitud fue exitosa (código de estado 200)
        if respuesta.status_code == 200:
            # Convierte los datos JSON a un diccionario de Python
            datos = respuesta.json()
            
            # Extrae la información relevante
            nombre_ciudad = datos['name']
            pais = datos['sys']['country']
            temperatura = datos['main']['temp']
            humedad = datos['main']['humidity']
            descripcion = datos['weather'][0]['description']

            print("\n--- Resultados ---")
            print(f"Ciudad: {nombre_ciudad}, {pais}")
            print(f"Temperatura: {temperatura}°C")
            print(f"Humedad: {humedad}%")
            print(f"Descripción: {descripcion.capitalize()}")
            print("------------------\n")
            
        else:
            # Maneja los errores de la API (por ejemplo, ciudad no encontrada)
            print(f"Error: No se pudo obtener el clima para '{ciudad}'.")
            print(f"Código de estado: {respuesta.status_code}. Mensaje: {respuesta.json().get('message', 'Desconocido')}")
            
    except requests.exceptions.RequestException as e:
        # Maneja los errores de conexión de red
        print(f"Error de conexión: No se pudo conectar a la API. Verifica tu conexión a internet. Detalles: {e}")
    except KeyError:
        # Maneja si la estructura de los datos JSON es inesperada
        print("Error: Los datos recibidos de la API no son válidos. Es posible que el nombre de la ciudad sea incorrecto.")

if __name__ == "__main__":
    while True:
        entrada_ciudad = input("Ingresa el nombre de la ciudad (o 'salir' para terminar): ")
        if entrada_ciudad.lower() == 'salir':
            print("Programa finalizado. ¡Hasta pronto!")
            break
        
        obtener_clima(entrada_ciudad)