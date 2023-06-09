"""
Generación de Contenido y Resúmenes Automáticos con Python + ChatGPT
"""

import os
import openai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# Función para generar contenido
def crear_contenido(tema, tokens, temperatura, modelo="text-davinci-002"):
    """Función para generar contenido"""
    prompt = f"Por favor, escribe un articulo corto sobre el tema: {tema}\n\n"
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        max_tokens=tokens,
        temperature=temperatura
    )
    return respuesta.choices[0].text.strip()

# Función para crear resúmenes
def resumir_texto(texto, tokens, temperatura, modelo="text-davinci-002"):
    """Función para crear resúmenes"""
    prompt = f"Por favor, resume el siguiente texto en español: {texto}\n\n"
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        max_tokens=tokens,
        temperature=temperatura
    )
    return respuesta.choices[0].text.strip()

# Función Inicio de APP
def app():
    """APP"""

    opciones = [
        "[0] - ¿Quieres generar un artículo?",
        "[1] - ¿Quieres resumir un artículo",
        "[q] - Salir"
    ]

    while True:
        os.system("clear" or "cls")
        print("------------------------------------------------------------------------")
        print("     Bienvenido al Generador de Contenido y/o Resúmenes del El Neto     ")
        print("------------------------------------------------------------------------")

        for opcion in opciones:
            print(opcion)

        print("\n")
        entrada_usuario = input("Escoge una opción: ")

        match entrada_usuario:
            case "0":
                os.system("clear" or "cls")
                print("-----------------------------------------------------------------------")
                print("                          Generar un Artículo                          ")
                print("-----------------------------------------------------------------------")
                print("\n")
                tema = input("Elije un tema para tu artículo: ")
                tokens = int(input("¿Cuantos tokens máximos tendrá tu artículo?: "))
                temperatura = int(input("Del 1 al 10, ¿qué tan creativo quieres que sea tu artículo?: ")) / 10
                articulo_creado = crear_contenido(tema, tokens, temperatura)
                print("\n")
                print(articulo_creado)
                print("\n")
                input("\nEnter para continuar")

            case "1":
                os.system("clear" or "cls")
                print("-----------------------------------------------------------------------")
                print("                          Resumir un Artículo                          ")
                print("-----------------------------------------------------------------------")
                print("\n")
                original = input("\nPega aquí el articulo que quieras resumir: ").rstrip("\n")
                tokens = int(input("¿Cuantos tokens máximos tendrá tu artículo?: "))
                temperatura = int(input("Del 1 al 10, ¿qué tan creativo quieres que sea tu artículo?: ")) / 10
                resumen = resumir_texto(original, tokens, temperatura)
                print("\n")
                print(resumen)
                print("\n")
                input("\nEnter para continuar")

            case "q":
                os.system("clear" or "cls")
                print("-----------------------------------------------------------------------")
                print("  Gracias por usar el Generador de Contenido y/o Resúmenes de El Neto  ")
                print("-----------------------------------------------------------------------")
                break

            case otra:
                print(f"{otra} no es valido")
                input("\nEnter para continuar")

def inicio():
    """Inicio de APP"""
    app()

inicio()
