import psycopg2
#from psycopg2 import Pacientes

class BaseDeDatos:
    def __init__(self):
        self.__conexion =psycopg2.connect(
            nombre ="Pacientes",
            user = "postgres",
            password = "2323",
            host = "localhost",
            port ="5432"
            
        )        
        self._cursor =self.__conexion.cursor()
        
    def obtener_paciente():
        pass

    def agregar_paciente(self,dni,nombre,apellido):
        try:
            consulta="""
                INSERT INTO Pacientes (dni_paciente,nombre_paciente,apellido_paciente) 
                VALUES(%s,%s,%s);
            """
            self.__cursor.execute(consulta,(dni,nombre,apellido))
            self.__conexion.commit()
            return True
        except Exception as e:
            self.__conexion.rollback()
            return False
    def modificar_paciente():
        pass

    def eliminar_paciente():#De este no estoy segura..
        pass