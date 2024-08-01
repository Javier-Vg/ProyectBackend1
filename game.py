import colorise
import random
from abc import ABC, abstractmethod

#colorise.cprint(self.__nombre, fg="green")



class Tablero(ABC): #Aqui voy a verificar los ganes y errores

    def __init__(self, tabla: list, palabra: str) -> None:
        self.__tabla = tabla
        self.__palabra = palabra
        pass
    
    def TablaMaquina(self):
        
        pass

    def TablaJugador(self):
        

        pass

    @abstractmethod #Hace que todas las clases que hereden de esta clase OBLIGATORIAMENTE tienen que tener defina este metodo
    def Intentos(self):
        pass


class Roles(Tablero):
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

    def __validar_tipo(self, elemento, tipo): #Valida si es de tipo de dato correcto
        if not isinstance(elemento, tipo):
            raise TypeError(f"Expected argument to be a {tipo}, got {type(elemento).__name__}")
    
    def Adivinador(self):
        palabrasAdivinar = ["casa","celular","cuaderno","maduro","biden","python"]
        chose = random.choice(palabrasAdivinar)
        return chose


    def Creador(self):
        print(f"¡Hola {self.__nombre}!")
        print("¿En que palabra piensa? :")
        word = input()
        validar = self.ValidarPalabra(word) 
        if validar:
            tablero = [["☻" for _ in range(0,len(word))] for _ in range(0,12)]

            # for o in tablero:
            #     print("  ".join(o))

            retro = Retroalimentacion(tablero)

            colorise.cprint(f"La palabra tiene {len(word)} letras.",fg="green")
        

    def ValidarPalabra(self, word):
        
        if word.isalpha() != True:
            print("Palabra invalida. Vuelva a intentar...\n")
            self.Creador()
        else:
            return True
        
    def Intentos(self):
        pass


class Retroalimentacion(Tablero):
    def __init__(self, tabla) -> None:
        self.__tabla = tabla
        pass

    def Intentos(self):
        pass



def main():
    print("<--------------->")
    print("- - - Wordl - - -")
    print("<--------------->\n")
    Rol = 0

    while Rol != 1 or Rol != 2:
        print("¿Que rol quiere elegir?´\n1: Adivinador\n2: Creador\n")
        Rol = int(input())

        if Rol == 1 or Rol == 2:
            break
        else:
            print("Opcion invalida...\n")

    Nombre = input("¿Cual es su nombre?: \n")

    objRol = Roles(nombre=Nombre, rol=Rol)

    print(objRol.Creador())


if __name__ == "__main__":
    main()


# y = Roles("Andres")
# y.Adivinador()



# matrix = [["☻" for _ in range(0,8)] for _ in range(0,12)]

# for o in matrix:
#     print("  ".join(o))
