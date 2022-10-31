from Ejercicio3.lanzadorej3 import ejercicio3
from Ejercicio4.lanzadorej4 import ejercicio4
from Ejercicio5.lanzadorej5 import ejercicio5
from helpers import limpiar_pantalla

def lanzadorppal():
     while True:
        limpiar_pantalla()
        print("========================") 
        print(" BIENVENIDO AL MENÚr ") 
        print("========================") 
        print("[1] Torres de Hanoi ") 
        print("[2] Cálculo de determinante ") 
        print("[3] Star Wars ") 
        print("[4] Polinomio ")
        print("[5] Cifrado Hash ") 
        print("[6] Cerrar el menú ")
        print("========================")

        opcion = input("> ")
        limpiar_pantalla()

        if opcion == 1:
            print("Torres de Hanoi...\n")

        if opcion == 2:
            print("Cálculo de determinante...")

        if opcion == 3:
            print("Star Wars...")
            ejercicio3()
        
        if opcion == 4:
            print("Polinomio...")
            ejercicio4()

        if opcion == 5:
            print("Cifrado Hash...")
            ejercicio5()
        
        if opcion == 6:
            print("Cerrando el menú...")
            break

        input("\nPresiona ENTER para continuar...")
