import csv
import numpy as np 
from EContratado import EContratado
from EExterno import EExterno
from Empleado import Empleado
from EPlanta import EPlanta


class Coleccion:
    def __init__(self,cantidad):
        self.__empleados=np.empty(cantidad,dtype=Empleado)
        
    def cargaEmpleados(self):
        archivo=open('planta.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            planta=EPlanta(float(fila[0]),int(fila[1]))
            self.__empleados=np.append(self.__empleados,planta)
        archivo.close()
        
        archivo=open('contratados.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            contratado=EContratado(fila[0],fila[1],int(fila[2]),float(fila[3]))
            self.__empleados=np.append(self.__empleados,contratado)
        archivo.close()
        
        archivo=open('externos.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            externo=EExterno(fila[0],fila[1],fila[2],float(fila[3]),float(fila[4]),float(fila[5]))
            self.__empleados=np.append(self.__empleados,externo)
        archivo.close()
        
    def buscaDNI(self,dni):
        i=0
        while i<self.__empleados.size and self.__empleados[i].getDNI()!= dni:
            i+=1
        if i<self.__empleados.size:
            return self.__empleados[i]
        else:
            return False
        
    def buscarTarea(self,tarea):
        i=0
        while i<self.__empleados.size and self.__empleados[i].getTarea()!= tarea:
            i+=1
        if i<self.__empleados.size:
            return self.__empleados[i]
        else:
            return False
        
    def verificaFecha(fecha,Eexterno):
        if fecha < Eexterno.getFechFin():
            return True
        else:
            return False
        
    def ayudaSolidaria(self):
        for empleado in self.__empleados:
            if empleado.getSueldo()<150000:
                print(f"{empleado}")
                
    def mostrarSueldo(self):
        for empleado in self.__empleados:
            print(f"{empleado}")
            print(f"sueldo: {empleado.getSueldo()}")