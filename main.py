from funciones import *
from funciones.division_guzman import division # type: ignore

if __name__ == "__main__":
 print("Ejecución de pruebas de las funciones del grupo")
 print("-" * 20)
 print("Pruebas de la función de división (Guzman):")
 print(f"Resultado (10 / 5): {division(10, 5)}")
 print(f"Resultado (10 / 0 - debe ser None): {division(10, 0)}")
 print("-" * 20)