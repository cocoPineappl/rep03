# comment
import time
import sys
#animacion de carga 2.0, mas eficiente que imprimir char x char.
def loadScreen(texto,delay_ms=200):
    delay = delay_ms/1000
    for i in range(1, len(texto) +1):
        sys.stdout.write('\r' + texto[:i])
        sys.stdout.flush()
        time.sleep(delay)
    print()
#menu de opciones
def menu_calc():
    print("\n"+"="*40)
    print("\nMENU PRINCIPAL".center(40))
    print("1. Calculadora Basica (Ed basica-Media)")
    print("2. Calculadora de Distancias")
    print("3. Calculadora Avanzada (Ed Media Superior)")
    print("0. Salir")
    print("\n"+"="*40)

def main():
    while True:
        menu_calc()
        opcion = input("\nSelecciona una opción (0-3): ")
        
        if opcion == "1":
            loadScreen(". . . Cargando Calculadora . . .", 50)
            start_calculadora()  # Llama a la calculadora completa
        elif opcion == "2":
            loadScreen(". . . Cargando Calculadora de Distancias . . .", 50)
            start_Distancia() #Llamamos a la calculadora de distancias
        elif opcion == "3":
            loadScreen(". . . Cargando Calculadora Avanzada . . .", 50)
            start_calculadora_avanzada
        elif opcion == "0": #nuevo: Funcion salir == 0
            print("\n")  # Espacio antes del mensaje
            loadScreen(". . . Saliendo del programa . . .", 50)
            loadScreen(" ¡Gracias por utilizar este proyecto! Vuelve pronto :) ", 50)
            print("\n")  # Espacio final
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

if __name__ == "__main__":
    main()