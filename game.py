import colorise
import random
import time
#from termcolor import colored
from abc import ABC, abstractmethod

# Definir códigos de escape ANSI para colores
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"
YELLOW = '\033[0;33m'
GRIS = '\033[37m'


class Gestion(ABC):
    
    @abstractmethod #Hace que todas las clases que hereden de esta clase OBLIGATORIAMENTE tienen que tener defina este metodo
    def IntentosPrevios(self):
        pass
    
    @abstractmethod
    def ActualizarDatos(self):
        pass


class Retroalimentacion(Gestion):
    def __init__(self, tabla: list) -> None:
        self.__tabla = tabla
        self.__attempts = 0

    @property
    def tabla(self):
        return self.__tabla
    
    @property
    def attempts(self):
        return self.__attempts
    
    @attempts.setter
    def attempts(self, attempts:str):
        self.__attempts = attempts

    @tabla.setter
    def tabla(self, tabla:list):
        self.__tabla = tabla

    def Feedback(self, palabraDescubrir: str, intento: str):

        array1 = [_ for _ in intento]
        array2 = [_ for _ in palabraDescubrir]

        for i in range(len(array1)):
            if array1[i] == array2[i]:
                # print(f"La letra es {array2[o]} y el indice es {o}")
                array1[i] = array1[i].replace(array1[i], f"{GREEN}{array1[i]}{RESET}")
            for letra in array2:
                if array1[i] == letra :
                    array1[i] = array1[i].replace(array1[i], f"{YELLOW}{array1[i]}{RESET}")     

        Fila = self.IntentosPrevios()
        self.tabla[Fila] = array1 #Sobreescribe la fila por el array modificado.
        self.ActualizarDatos(self.tabla)
        return self.tabla
            

    def IntentosPrevios(self):
        if self.attempts == 5:
            pass     
        else:
            return self.attempts
            
    def ActualizarDatos(self, TablaModificda):
        self.attempts += 1
        self.tabla = TablaModificda


class Tablero(): #Aqui voy a verificar los ganes y errores

    def __init__(self, nombre: str, palabra: str, feedback: Retroalimentacion) -> None:
        self.__nombre = nombre
        self.__palabra = palabra
        self.__feedback = feedback
        pass

    @property
    def palabra(self):
        return self.__palabra
    
    @property
    def feedback(self):
        return self.__feedback
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre:str):
        self.__nombre = nombre

    @feedback.setter
    def feedback(self, feedback:list):
        self.__feedback = feedback

    @palabra.setter
    def palabra(self, palabra:str):
        self.__palabra = palabra

    def generar_palabra_aleatoria(self, lista_palabras):

        palabraAleatoria = "a"
        while len(palabraAleatoria) != len(self.palabra):
            palabraAleatoria = random.choice(lista_palabras)
            
        return palabraAleatoria
            
    
    def TablaMaquina(self, rol):

        #while self.feedback.attempts != 5:
            with open("palabras.txt", "r", encoding="utf-8") as archivo:
                palabras = [linea.strip() for linea in archivo]
            
            palabra_generada = self.generar_palabra_aleatoria(palabras)
            NuevaTabla = self.feedback.Feedback(self.palabra, palabra_generada)

            if NuevaTabla != False:
                self.MostrarTablero(NuevaTabla) #cositas
                self.WinVerific(palabra_generada, self.palabra, rol) #cositas
    
    
    def TablaJugador(self, rol):
        palabraElegida = "a"
        while len(palabraElegida) != len(self.palabra):
            colorise.cprint(f"La palabra tiene {len(self.palabra)} letras.",fg="green")
            palabraElegida = input("¿Con cual palabra va a intentar adivinar?: ").lower().strip()

            if len(palabraElegida) != len(self.palabra):
                colorise.cprint("Fuera del rango de la palabra, ingrese algo valido...\n", fg="red")

        NuevaTabla = self.feedback.Feedback(self.palabra, palabraElegida )

        if NuevaTabla != False:
            self.MostrarTablero(NuevaTabla) #cositas
            self.WinVerific(palabraElegida, self.palabra, rol) #cositas


    def WinVerific(self, Intento, palabra, rol):
        if Intento == palabra:
            colorise.cprint("\n!Descubriste la palabra!\n", fg="green")

        elif self.feedback.attempts != 5:
            colorise.cprint("!El juego sigue!\n", fg="blue")

            if rol == 1 or rol == 3:
                self.TablaJugador(rol)
            else:
                time.sleep(1.5)
                self.TablaMaquina(rol)
        else:
            colorise.cprint("!Fin del juego!\n", fg="blue")
            colorise.cprint(f"La palabra es: {palabra}\n", fg="yellow")


    def MostrarTablero(self, TableroActual):
        for fila in TableroActual: #cositas
            print("", end="     ")
            time.sleep(0.1)
            print("    ".join(fila))


class Roles():
    def __init__(self, nombre: str, rol: int) -> None:
        self.__validar_tipo(nombre, str)
        self.__validar_tipo(rol, int)
        self.__nombre = nombre
        self.__rol = rol
        #self.__reguex = r'^[a-zA-Z]+$' #Esto no se usa.

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def rol(self):
        return self.__rol
    
    @nombre.setter
    def nombre(self, nombre:str):
        self.__nombre = nombre
        
    @rol.setter
    def rol(self, rol:str):
        self.__rol = rol

    def __validar_tipo(self, elemento, tipo): #Valida si es de tipo de dato correcto
        if not isinstance(elemento, tipo):
            raise TypeError(f"Expected argument to be a {tipo}, got {type(elemento).__name__}")
    
    def Adivinador(self):
        palabrasAdivinar = ["casa","celular","cuaderno","maduro","biden","python"]
        chose = random.choice(palabrasAdivinar)
        
        tablero = self.TableroBase(len(chose))
        retro = Retroalimentacion(tablero)
        objtTablero = Tablero(self.nombre, chose, retro)
        objtTablero.TablaJugador(self.rol) 


    def Creador(self):
        
        print(f"¡Hola {self.__nombre}!")
        print("¿Cual palabra va a adivinar? :")
        word = input().lower().strip()
        validar = self.ValidarPalabra(word) 
        if validar:
            tablero = self.TableroBase(len(word))
            retro = Retroalimentacion(tablero)
            objtTablero = Tablero(self.nombre, word, retro)
            if self.rol == 2:
                objtTablero.TablaMaquina(self.rol)
            else:
                objtTablero.TablaJugador(self.rol) #cosita

    def TableroBase(self, key):
        tablero = [["☻" for _ in range(0,key)] for _ in range(0,5)] 
        return tablero


    def ValidarPalabra(self, word: str):
        if word.isalpha() != True:
            colorise.cprint("Palabra invalida. Vuelva a intentar...\n", fg="blue")
            self.Creador()
        else:
            return True


def main():

    Nombre = input("¿Cual es su nombre?: ").strip()
    while True:
        print("\nMenu: \n1: Adivinador.\n2: Creador.\n3: 1vs1.\n4: Salir.")
        Rol = int(input())

        if Rol == 1:
            objRol = Roles(nombre=Nombre, rol=Rol)
            objRol.Adivinador() 
        elif Rol == 2:
            objRol = Roles(nombre=Nombre, rol=Rol)
            objRol.Creador() #Diferenciar entre metodos
        elif Rol == 3:
            objRol = Roles(nombre=Nombre, rol=Rol)
            objRol.Creador()
        elif Rol == 4:
            print("Hasta luego.")
            break
        else:
            print("Opcion invalida...\n")

        
if __name__ == "__main__":
    main()


# y = Roles("Andres")
# y.Adivinador()


# matrix = [["☻" for _ in range(0,8)] for _ in range(0,12)]

# for o in matrix:
#     print("  ".join(o))

tablero = [["☻" for _ in range(0,9)] for _ in range(0,12)]
nombres = [item.replace("☻", "x") for item in tablero[0]]



# for p in range(len(tablero[0])):
#     if p == 0:
#         tablero[0][p] = tablero[0][p].replace("☻", f"{RED}x{RESET}")
        
# for k in tablero:
#     time.sleep(0.3)
#     print("  ".join(k))


intento = "maripepi"
palabraDescubrir = "mariposa"
array1 = [s for s in intento]
array2 = [a for a in palabraDescubrir]

# for i in range(len(array1)):
#     if array1[i] == array2[i]:
#         # print(f"La letra es {array2[o]} y el indice es {o}")
#         array1[i] =array1[i].replace(array1[i], f"{GREEN}{array1[i]}{RESET}")
#     for letra in array2:
#         if array1[i] == letra : #Esa segunda condicion es para que no me sobreescriba lo que esta en verde.
#             array1[i] =array1[i].replace(array1[i], f"{YELLOW}{array1[i]}{RESET}")
       
                    
# for o in range(len(array1)):
#     if array1[o] == array2[o]:
#         print(f"La letra es {array2[o]} y el indice es {o}")
#listas Anidadas

# for o in range(len(array1)):
#     if array1[o] == array2[o]:
#         # print(f"La letra es {array2[o]} y el indice es {o}")
#         array1[o] =array1[o].replace(array1[o], f"{GREEN}{array1[o]}{RESET}")


# for k in tablero:
#     print("", end="     ")
#     time.sleep(0.1)
#     print("    ".join(k))

#strip elimina los espacios al principio y al final.


