BLACK   = '\033[30m'
ROJO     = '\033[31m'
VERDE   = '\033[32m'
AMARILLO  = '\033[33m'
AZUL= '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
BLANCO   = '\033[37m'
RESET   = '\033[39m'

import time
#trivia 1
print ("Bienvenido a mi trivia sobre cultura general, comenzaras por algo basico\n")
time.sleep(1)
nombre = input("\033[33mAntes escribe tu nombre: \033[39m")

print("\n ¿como estas?\033[34m", nombre, "\033[39mescribe solo la letra a la opcion de tu respuesta\n")

# Pregunta 1
print ("\033[32m1) ¿En que año fue la independencia del Peru?\033[39m")
time.sleep(1)
print ("a) 1921")
print ("b) 1821")
print ("c) 1801")
print ("d) 1901")


respuesta_1 = input("\nTu respuesta: ")

while respuesta_1 not in ("a", "b", "c", "d"):
  respuesta_1 = input("Solo reponde con a, b, c o d. \nIngresa de nuevo tu respuesta: ")

if respuesta_1 == "a":
    print("\033[31mIncorrecto!", nombre, "Estudia un poco mas\033[39m")
elif respuesta_1 == "c":
    print("\033[31mIncorrecto!", nombre, "parece que no eres peruano\033[39m")
elif respuesta_1 == "d":
    print("\033[31mIncorrecto!", nombre, "casi, pero no\033[39m")
else:
  print("Muy bien\033[34m", nombre, "\033[39m!")

time.sleep(1)
# Pregunta 2
print("\n\033[32m1) ¿Cuántos litros de sangre tiene una persona adulta?\033[39m")
print("a) Tiene entre 2 y 4 litros")
print("b) Tiene entre 4 y 6 litros")
print("c) Tiene 10 litros")
print("d) Tiene 7 litros")

respuesta_2 = input("\nTu respuesta: ")

while respuesta_2 not in ("a", "b", "c", "d"):
  respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_2 == "a":
  print("Incorrecto!", nombre, "estuviste cerca")
elif respuesta_2 == "c":
  print("Incorrecto!", nombre, "son muchos litros")
elif respuesta_2 == "d":
  print("Incorrecto!", nombre, "tenemos casi la mitad")
else:
  print("Muy bien\033[34m", nombre, "\033[39m!")

 