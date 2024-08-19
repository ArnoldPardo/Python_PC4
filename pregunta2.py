import random
from pyfiglet import Figlet

def main():
    # Inicializar Figlet
    figlet = Figlet()

    # Obtener lista de fuentes disponibles
    fuentes_disponibles = figlet.getFonts()
    
    # Solicitar al usuario el nombre de la fuente
    fuente_usuario = input("Ingrese el nombre de la fuente (deje en blanco para seleccionar aleatoriamente): ")
    
    # Si el usuario no proporciona una fuente, seleccionar una aleatoria
    if not fuente_usuario:
        fuente_usuario = random.choice(fuentes_disponibles)
    
    # Verificar si la fuente proporcionada es válida
    if fuente_usuario not in fuentes_disponibles:
        print(f"Fuente no válida. Se seleccionará una fuente aleatoria.")
        fuente_usuario = random.choice(fuentes_disponibles)
    
    # Establecer la fuente en Figlet
    figlet.setFont(font=fuente_usuario)
    
    # Solicitar al usuario el texto
    texto_usuario = input("Ingrese el texto que desea imprimir: ")
    
    # Imprimir el texto utilizando la fuente seleccionada
    texto_imprimido = figlet.renderText(texto_usuario)
    print(f"\nTexto impreso con la fuente '{fuente_usuario}':")
    print(texto_imprimido)

if __name__ == "__main__":
    main()


