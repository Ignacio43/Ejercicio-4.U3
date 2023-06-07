from Empleado import Empleado

class EExterno(Empleado):
    def __init__(self,tarea,fecha_In,fecha_fin,monto_viatico,costo_obra,seguro_vida):
        Empleado.__init__(self,DNI,nombre,direccion,telefono)
        self.__tarea=tarea
        self.__fecha_In=fecha_In
        self.__fecha_fin=fecha_fin
        self.__monto_viatico=monto_viatico
        self.__costo_obra=costo_obra
        self.__seguro_vida=seguro_vida
        
    def getTarea(self):
        return self.__tarea
    
    def getFechFin(self):
        return self.__fecha_fin
    
    def montoPagar(self):
        print(f"el monto a pagar por la tarea es de: {self.__costo_obra} ")
        
        
    def getSueldo(self):
        return self.__costo_obra - self.__monto_viatico - self.__seguro_vida