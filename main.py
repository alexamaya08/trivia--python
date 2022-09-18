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
print(CYAN+"Te explicare las reglas del juego\n"+RESET)
print(MAGENTA+"1)Comenzaras con un puntaje al azar de 1 a 10, la cual puedes ir sumando hasta el final")
print("2)Por cada respuesta incorrecta se te resta aleatoriamente de 1 a 5 puntos")
print("3)por cada respuesta correcta se te suamara aleatoriamente de 5 a 10 puntos\n"+RESET)
nombre = input(AMARILLO+"Antes escribe tu nombre:"+RESET)
print("\n ¿cómo estas?", AZUL+nombre+RESET ,"escribe solo la letra a la opcion de tu respuesta\n")
while reinicio_trivia==True:
  correcta=0
  incorrecta=0
  puntaje=random.randint(0,10)
  intentos+=1
  print("\nIntento número: ",intentos)
  input("Presione enter para continuar\n")
  print(VERDE+"Comenzarás con:",puntaje,"puntos"+RESET)
  for numero_carga in range(5,-1,-1):
    if numero_carga == 0:
      print(ROJO+"ya!"+RESET)
      time.sleep(1)
    elif numero_carga == 3:
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
    respuesta_1 = input(ROJO+"Solo reponde con a, b, c o d. \nIngresa de nuevo tu respuesta: "+RESET)
  
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
    print(VERDE+"Muy bien", nombre, "!"+RESET)
  time.sleep(1)
  print(VERDE+nombre, "llevas", puntaje, "puntos." + RESET)
  time.sleep(1)
# Pregunta 2
  print(VERDE+"\n2) ¿Cuántos litros de sangre tiene una persona adulta?"+RESET)
  print("a) Tiene entre 2 y 4 litros")
  print("b) Tiene entre 4 y 6 litros")
  print("c) Tiene 10 litros")
  print("d) Tiene 7 litros")

  respuesta_2 = input("\nTu respuesta: ").lower()
  
  while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input(ROJO+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET)
  
  if respuesta_2 == "a":
    print(ROJO+"Incorrecto!", nombre, "estuviste cerca"+RESET)
    puntaje -= random.randint(1, 5)
    incorrecta += 1
  elif respuesta_2 == "c":
    print(ROJO+"Incorrecto!", nombre, "son muchos litros"+RESET)
    puntaje -= random.randint(1, 5)
    incorrecta += 1
  elif respuesta_2 == "d":
    print(ROJO+"Incorrecto!", nombre, "tenemos casi la mitad"+RESET)
    puntaje -= random.randint(1, 5)
    incorrecta += 1
  else:
    print("Muy bien",AZUL+ nombre, "!"+RESET)
    puntaje += random.randint(5, 10)
    correcta += 1
    time.sleep(1)
  print(VERDE+nombre, "llevas", puntaje, "puntos." + RESET)
  time.sleep(1)

  #pregunta 3
  print(VERDE+"\n3) ¿Cuál es el lugar más frío de la tierra?"+RESET)
  print("a) La antartida")
  print("b) Oceania")
  print("c) Rusia")
  print("d) Ticlio")

  respuesta_3 = input("\nTu respuesta: ").lower()
  
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input(ROJO+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET)
  
  if respuesta_3 == "b":
    print(ROJO+"Incorrecto!", nombre, "es una pregunta facil"+RESET)
    puntaje -= random.randint(1, 5)
    incorrecta += 1
  elif respuesta_3 == "c":
    print(ROJO+"Incorrecto!", nombre, "En Rusia hace frio pero no"+RESET)
    puntaje -= random.randint(1, 5)
    incorrecta += 1
  elif respuesta_3 == "d":
    print(ROJO+"Incorrecto!", nombre, "para nada cerca"+RESET)
    puntaje -= random.randint(1, 5)
    incorrecta += 1
  else:
    print("Muy bien",AZUL+ nombre, "!"+RESET)
    puntaje += random.randint(5, 10)
    correcta += 1
    time.sleep(1)
  print(VERDE+nombre, "llevas", puntaje, "puntos." + RESET)
  time.sleep(1)
  input(AMARILLO+"Presione enter para ver resultados"+RESET)
  os.system('clear')
  print("\nCantidad de respuestas correctas: ", correcta)
  time.sleep(1)
  print("\nCantidad de respuestas incorrectas: ", incorrecta)
  time.sleep(1)
  print(VERDE + "\nGracias", nombre, "por jugar mi trivia, alcanzaste",puntaje, "puntos." + RESET)
  turnos.append(puntaje)
  print(MAGENTA + "\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input(
        "Ingresa 'si' para repetir, o cualquier tecla para finalizar: " +
        RESET).lower()
  if repetir_trivia != "si": 
    print(AMARILLO + "\nSecuencia de puntaje por cada turno: ",turnos)
    print("\nEspero", nombre, "que lo hayas pasado bien, hasta pronto!")
    reinicio_trivia = False