from Empleado import Empleado

class EContratado(Empleado):
    def __init__(self,fecha_inicio,finalizacion_contrato,cant_trabajadas,valor_hora):
        Empleado.__init__(self,DNI,nombre,direccion,telefono)
        self.__fecha_inicio=fecha_inicio
        self.__finalizacion_contrato=finalizacion_contrato
        self.__cant_trabajadas=cant_trabajadas
        self.__valor_hora=valor_hora
        
    def incrementarHoras(self,horas):
        self.__cant_trabajadas+=horas     
        
    def getSueldo(self):
        return self.__cant_trabajadas * self.__valor_hora
        