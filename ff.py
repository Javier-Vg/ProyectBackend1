from abc import ABC, abstractmethod

class Tablero:
    def __init__(self, Tabla: list) -> None:
        self.__Tabla = Tabla

    @property
    def Tabla(self):
        return self.__Tabla
    
    @Tabla.setter
    def Tabla(self, Tabla:str):
        self.__Tabla = Tabla

    def actualizar(self):
        self.Tabla = ["mamaguevos"]

    def most(self):
        print("Array: ",self.Tabla)

class kk(ABC):

    @abstractmethod
    def metodo(self):
        print("AHH")

class rosas(kk):
    def __init__(self, tabla: Tablero) -> None:
        self.__tabla= tabla
        pass

    @property
    def tabla(self):
        return self.__tabla
    
    @tabla.setter
    def tabla(self, tabla:str):
        self.__tabla = tabla

    def llamarActu(self):
        self.tabla.actualizar()

    def mostrar(self):
        print("Array: ",self.tabla.Tabla)
        
    def metodo(self):
            print("AHH")

h = ["Buenos dias", "Que?"]
obtTablero = Tablero(h)
objRosas = rosas(obtTablero)

objRosas.llamarActu()
objRosas.mostrar()
obtTablero.most()



