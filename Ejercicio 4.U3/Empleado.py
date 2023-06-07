

class Empleado: 
    def __init__(self,DNI,nombre,direccion,telefono):
        self.__DNI=DNI
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono
        
    def getDNI(self):
        return self.__DNI
    
    def __str__(self):
        return f"{self.__DNI}  {self.__nombre}  {self.__direccion}"