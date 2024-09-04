import openai

# Configura tu clave de API de OpenAI
openai.api_key = ""

def leer_pregunta_de_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            pregunta = archivo.read().strip()
        return pregunta
    except Exception as e:
        return f"Error al leer el archivo: {str(e)}"

def escribir_respuesta_a_archivo(ruta_archivo, respuesta):
    try:
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(respuesta)
    except Exception as e:
        print(f"Error al escribir en el archivo: {str(e)}")

def preguntar_a_openai(pregunta):
    try:
        # Envía la pregunta a la API de OpenAI usando el endpoint de chat
        respuesta = openai.ChatCompletion.create(
            model="gpt-4o",  # Elige el modelo adecuado
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": pregunta}
            ]
        )
        # Retorna la respuesta generada
        return respuesta.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Rutas de los archivos de entrada y salida
ruta_archivo_entrada = 'Pregunta.txt'
ruta_archivo_salida = 'Respuesta.txt'

# Lee la pregunta desde el archivo
pregunta = leer_pregunta_de_archivo(ruta_archivo_entrada)

if not pregunta.startswith("Error"):
    # Genera la respuesta usando OpenAI
    respuesta = preguntar_a_openai(pregunta)

    # Escribe la respuesta en un archivo
    escribir_respuesta_a_archivo(ruta_archivo_salida, respuesta)
    print(f"Respuesta guardada en {ruta_archivo_salida}")
else:
    print(pregunta)