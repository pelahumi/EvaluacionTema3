from Ejercicios.Ejercicio1.lanzadorej1 import ejercicio1
from Ejercicios.Ejercicio2.lanzadorej2 import ejercicio2
from Ejercicios.Ejercicio3.lanzadorej3 import ejercicio3
from Ejercicios.Ejercicio4.lanzadorej4 import ejercicio4
from Ejercicios.Ejercicio5.lanzadorej5 import ejercicio5
from Ejercicios.helpers import limpiar_pantalla

def lanzadorppal():

     while True:
        limpiar_pantalla()
        print("========================") 
        print(" BIENVENIDO AL MENÚ") 
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
        
        if opcion == "1":
            print("Torres de Hanoi...\n")
            ejercicio1()
            break

        if opcion == "2":
            print("Cálculo de determinante...")
            ejercicio2()
            break

        if opcion == "3":
            print("Star Wars...")
            ejercicio3()
            break
        
        if opcion == "4":
            print("Polinomio...")
            ejercicio4()
            break

        if opcion == "5":
            print("Cifrado Hash...")
            ejercicio5()
            break
        
        if opcion == "6":
            print("Cerrando el menú...")
            break

        input("\nPresiona ENTER para continuar...")

