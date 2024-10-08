import colorise
import random
import time
from abc import ABC, abstractmethod

class Gestion(ABC): #Clase con metodos abstractos
    
    @abstractmethod #Hace que todas las clases que hereden de esta clase obligatoriamente tienen que tener defina este metodo
    def IntentosPrevios(self):
        pass
    
    @abstractmethod
    def ActualizarDatos(self):
        pass

class Palabras:
    def generar_palabra_aleatoria(self, palabra: str, uso: int): #Metodo que retorna una palabra random de un array de palabras, que es recibido como parametro.

        #Esto lee todas las lineas del archivo llamado "palabras.txt", y los almacena en un array.
        with open("palabras.txt", "r", encoding="utf-8") as archivo: 
            palabras = [linea.strip() for linea in archivo]
            
        if uso == 1:
            palabraAleatoria = "a"
            while len(palabraAleatoria) != len(palabra): #Bucle que no permite que retorne una palabra con diferente longitud de la palabra a adivinar.
                palabraAleatoria = random.choice(palabras)
            return palabraAleatoria
        
        else:
            Aleatorio = random.choice(palabras)
            return Aleatorio

class Retroalimentacion(Gestion): #Clase que retorna la tabla ya con su retroalimentacion.
    def __init__(self, tabla: list) -> None:
        self.__validar_tipo(tabla, list)
        self.__tabla = tabla
        self.__attempts = 0
        self.__yellow = '\033[0;33m'  # Códigos de escape ANSI para colores
        self.__green = "\033[32m"
        self.__reset = "\033[0m"

    @property
    def tabla(self):
        return self.__tabla
    
    @property
    def yellow(self):
        return self.__yellow
    
    @property
    def green(self):
        return self.__green
    
    @property
    def reset(self):
        return self.__reset
    
    @property
    def attempts(self):
        return self.__attempts
    
    @attempts.setter
    def attempts(self, attempts:str):
        self.__attempts = attempts

    @tabla.setter
    def tabla(self, tabla:list):
        self.__tabla = tabla
    
    def __validar_tipo(self, elemento, tipo): #Valida si es de tipo de dato correcto
        if not isinstance(elemento, tipo):
            raise TypeError(f"Expected argument to be a {tipo}, got {type(elemento).__name__}")

    def Feedback(self, palabraDescubrir: str, intento: str): #Metodo que recibe la palabra a buscar y la palabra que ingreso para adivinar.

        #Vuelve la 2 palabras en arrays para poder compararlas luego
        array1 = [_ for _ in intento]
        array2 = [_ for _ in palabraDescubrir]

        #Inicia la comparativa de las palabras y asignando el color correspondiente, usando los codigos ANSI.
        for i in range(len(array1)):
            if array1[i] == array2[i]:
                array1[i] = array1[i].replace(array1[i], f"{self.green}{array1[i]}{self.reset}")
            for letra in array2:
                if array1[i] == letra :
                    array1[i] = array1[i].replace(array1[i], f"{self.yellow}{array1[i]}{self.reset}")     

        Fila = self.IntentosPrevios()
        self.tabla[Fila] = array1 #Sobreescribe la fila por el array modificado.
        self.ActualizarDatos(self.tabla)
        return self.tabla
            
    def IntentosPrevios(self): #Metodo que devuelve el intento o por el contrario, no lo manda, ya que terminaron los intentos.
        if self.attempts == 12:
            pass     
        else:
            return self.attempts
            
    def ActualizarDatos(self, TablaModificada): #Metodo que actualiza los datos, como la nueva tabla y aumento de intentos perdidos.
        self.attempts += 1
        self.tabla = TablaModificada

class Tablero( Palabras ): #Clase que contiene los procesos de los intentos dentro de la tabla.

    def __init__(self, nombre: str, palabra: str, feedback: Retroalimentacion) -> None: #Metodo constructor
        self.__validar_tipo(nombre, str)
        self.__validar_tipo(palabra, str)
        self.__validar_tipo(feedback, Retroalimentacion)
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
        
    def __validar_tipo(self, elemento, tipo): #Valida si es de tipo de dato correcto
        if not isinstance(elemento, tipo):
            raise TypeError(f"Expected argument to be a {tipo}, got {type(elemento).__name__}")

    def TablaMaquina(self, rol: int):
        
        palabra_generada = self.generar_palabra_aleatoria(self.palabra, 1)
        NuevaTabla = self.feedback.Feedback(self.palabra, palabra_generada) #Tabla ya con su retroalimentacion.
    
        if NuevaTabla != False:
            self.MostrarTablero(NuevaTabla) #Llama al metodo "MostrarTablero", y se envia por parametro el nuevo tablero.
            self.WinVerific(palabra_generada, self.palabra, rol) 
    
    def TablaJugador(self, rol:int): #Metodo que pide al usuario imgresar una palabra para usarla como intento.
        palabraElegida = "a"
        while len(palabraElegida) != len(self.palabra): #Repite si la longitud de las plabras son diferentes.
            colorise.cprint(f"La palabra tiene {len(self.palabra)} letras.",fg="green")
            palabraElegida = input("¿Con cual palabra va a intentar adivinar?: ").lower().strip()

            if len(palabraElegida) != len(self.palabra):
                colorise.cprint("Fuera del rango de la palabra, ingrese algo valido...\n", fg="red")

        NuevaTabla = self.feedback.Feedback(self.palabra, palabraElegida ) #Array ya modificado con su feedback

        if NuevaTabla != False:
            self.MostrarTablero(NuevaTabla)  #Se llama al metodo "MostrarTablero", y se envia por parametro el nuevo tablero.
            self.WinVerific(palabraElegida, self.palabra, rol)

    def WinVerific(self, Intento: str, palabra: str, rol: int): #Metodo que verifica si la palabra es igual o diferente a la palabra a adivinar.
        if Intento == palabra:                   #Tambien es la que finaliza el juego
            colorise.cprint("\n!Descubriste la palabra!\n", fg="green")

        elif self.feedback.attempts != 12:
            colorise.cprint("!El juego sigue!\n", fg="blue")

            if rol == 1 or rol == 3:
                self.TablaJugador(rol)
            else:
                time.sleep(1)
                self.TablaMaquina(rol)
        else:
            colorise.cprint("!Fin del juego!\n", fg="blue")
            colorise.cprint(f"La palabra es: {palabra}\n", fg="yellow")

    def MostrarTablero(self, TableroActual): #Muestra el tablero actulizado.
        for fila in TableroActual: 
            print("", end="     ")
            time.sleep(0.1)
            print("   ".join(fila))

class Roles( Palabras ):  #Metodo que divide los roles de adivinador y creador de la palabra.
    def __init__(self, nombre: str, rol: int) -> None:
        self.__validar_tipo(nombre, str)
        self.__validar_tipo(rol, int)
        self.__nombre = nombre
        self.__rol = rol
        
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
    
    def Adivinador(self): #Metodo donde la palabra impuesta a adivinar va a ser por parte de la computadora.
        palabrasAdivinar = self.generar_palabra_aleatoria("",2) #LLamo al metodo de la clase 
        
        tablero = self.TableroBase(len(palabrasAdivinar))
        retro = Retroalimentacion(tablero)
        objtTablero = Tablero(self.nombre, palabrasAdivinar, retro) #Se aplica la composicion.
        objtTablero.TablaJugador(self.rol) 

    def Creador(self): #Metodo donde la palabra impuesta a adivinar va a ser por parte del jugador.
        
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
                objtTablero.TablaJugador(self.rol) 

    def TableroBase(self, key: int): #Metodo que retorna la base del tablero:
        tablero = [["○" for _ in range(0,key)] for _ in range(0,12)] 
        return tablero

    def ValidarPalabra(self, word: str): #validacion de la palabra integrada.
        if word.isalpha() != True:
            colorise.cprint("Palabra invalida. Vuelva a intentar...\n", fg="blue")
            self.Creador()
        else:
            return True

def main(): #Funcion donde se establecera el menu y comienzo del juego:

    Nombre = input("¿Cual es su nombre?: ").strip()
    while True:
        print("\n-Digite el numero que desee: \n1: Adivinador.\n2: Creador.\n3: 1vs1.\n4: Salir.")
        Rol = int(input())

        if Rol == 1:
            objRol = Roles(nombre=Nombre, rol=Rol)
            objRol.Adivinador() 
        elif Rol == 2 or Rol == 3:
            objRol = Roles(nombre=Nombre, rol=Rol)
            objRol.Creador() 
        elif Rol == 4:
            print("Hasta luego.")
            break
        else:
            print("Opcion invalida...\n")
        
if __name__ == "__main__":
    main()