BLACK   = '\033[30m'
ROJO  = '\033[31m'
VERDE   = '\033[32m'
AMARILLO  = '\033[33m'
AZUL  = '\033[34m'
MAGENTA = '\033[35m'
CYAN  = '\033[36m'
BLANCO  = '\033[37m'
RESET  = '\033[39m'

import random
import time
import os

reinicio_trivia = True
intentos = 0
turnos = []
#trivia 1
print (MAGENTA+"Bienvenido a mi trivia sobre cultura general, comenzaras por algo basico\n"+RESET)
time.sleep(1)
nombre = input(AMARILLO+"Antes escribe tu nombre: \033[39m")
print("\n ¿cómo estas?", AZUL+nombre+RESET ,"escribe solo la letra a la opcion de tu respuesta\n")
while reinicio_trivia==True:
  correcta=0
  incorrecta=0
  puntaje=random.randint(0,10)
  intentos+=1
  print("\nIntento número: ",intentos)
  input("Presione enter para continuar")
  print(VERDE+"Comenzarás con:",puntaje,"puntos"+RESET)
  for numero_carga in range(5,-1,-1):
    if numero_carga == 0:
      print(CYAN+"ya!"+RESET)
      time.sleep(1)
    elif numero_carga == 5:
        print(AMARILLO+"¿PREPARADO?"+RESET)
        time.sleep(1)
    else:
      print(numero_carga)
      time.sleep(1)  

# Pregunta 1
  print (VERDE+"\n1) ¿En que año fue la independencia del Peru?"+RESET)
  time.sleep(1)
  print ("a) 1921")
  print ("b) 1821")
  print ("c) 1801")
  print ("d) 1901")
  
  
  respuesta_1 = input("\nTu respuesta: ").lower()

  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input("Solo reponde con a, b, c o d. \nIngresa de nuevo tu respuesta: ")
  
  if respuesta_1 == "a":
      print(ROJO+"Incorrecto!", nombre, "No estas cerca del año"+RESET)
      puntaje -= random.randint(1, 5)
      incorrecta += 1
  elif respuesta_1 == "c":
      print(ROJO+"Incorrecto!", nombre, "Intenta de nuevo"+RESET)
      puntaje -= random.randint(1, 5)
      incorrecta += 1
  elif respuesta_1 == "d":
      print(ROJO+"Incorrecto!", nombre, "Ojo, estamos en el bicentenario"+RESET)
      puntaje -= random.randint(1, 5)
      incorrecta += 1
  else:
    puntaje += random.randint(5, 10)
    correcta += 1
    print("Muy bien", nombre, "!")
  time.sleep(1)
  print(VERDE+nombre, "llevas", puntaje, "puntos." + RESET)
  time.sleep(2)
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
    puntaje -= random.randint(1, 5)
    incorrecta += 1
  elif respuesta_2 == "c":
    print("Incorrecto!", nombre, "son muchos litros")
    puntaje -= random.randint(1, 5)
    incorrecta += 1
  elif respuesta_2 == "d":
    print("Incorrecto!", nombre, "tenemos casi la mitad")
    puntaje -= random.randint(1, 5)
    incorrecta += 1
  else:
    print("Muy bien\033[34m", nombre, "\033[39m!")
    puntaje += random.randint(5, 10)
    correcta += 1
  time.sleep(1)
  print(VERDE+nombre, "llevas", puntaje, "puntos." + RESET)
  time.sleep(2)
  input("Presione enter para continuar")
  os.system('clear')
  print("\nCantidad de respuestas correctas: ", correcta)
  time.sleep(1)
  print("Cantidad de respuestas incorrectas: ", incorrecta)
  time.sleep(1)