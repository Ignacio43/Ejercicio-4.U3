from Empleado import Empleado


class EPlanta(Empleado):
    def __init__(self,sueldo_basico,antiguedad):
        Empleado.__init__(self,DNI,nombre,direccion,telefono)
        self.__sueldo_basico=sueldo_basico
        self.__antiguedad=antiguedad
        
    def getSueldo(self):
        return self.__sueldo_basico + ((1*self.__sueldo_basico)/100)*self.__antiguedad
        