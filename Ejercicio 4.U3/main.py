import csv 
from Coleccion import Coleccion
from EContratado import EContratado
        
if __name__=='__main__':
    
    cant=int(input("ingrese la cantidad de empleados a registrar "))
    
    ManejaEmpleados=Coleccion(cant)
    ManejaEmpleados.cargaEmpleados()
    
    print("1.  Registrar Horas")
    print("2.  Total de Tareas")
    print("3.  Ayuda Economica")
    print("4.  Calcular Sueldo")
    
    op=int(input("ingrese la opcion a realizar: "))
    
    while op != 0:
        if op == 1:
            dni=int(input("ingrese dni del empleado "))
            horas=int(input("ingrese la cantidad de horas trabajadas: "))
            empleado=ManejaEmpleados.buscaDNI()
            if empleado != False and isinstance(empleado,EContratado):
                empleado.incrementoHoras(horas) 
        elif op == 2:
            tarea=input("ingrese la tarea a buscar: ")
            fecha=input("ingrese fecha actual: ")
            EmpleadoExterno=ManejaEmpleados.buscaTarea(tarea)
            confirmacion=ManejaEmpleados.verificaFecha(fecha,EmpleadoExterno)
            if EmpleadoExterno != False and confirmacion ==True:
                EmpleadoExterno.montoPagar()
        elif op == 3:
            ManejaEmpleados.ayudaSolidaria()
        elif op == 4:
            ManejaEmpleados.mostrarSueldo()
        else:
            print("opcion incorrecta. ")
            
        print("1.  Registrar Horas")
        print("2.  Total de Tareas")
        print("3.  Ayuda Economica")
        print("4.  Calcular Sueldo")    
        
        op=int(input("ingrese la opcion a realizar: "))
            
            
                