
#from Vista.ListaPacientesVista import ListaPacientesVista   | nombres a definir
#from Controlador.ControladorAgregarPaciente import ControladorAgregarPaciente
from modelo.BaseDeDatos import BaseDeDatos


class ControladorListaPacientesVista:

    def __init__(self):
        #self.__vista: ListaPacientesVista(self)
        #self.__vista.show()
        self.__base = BaseDeDatos()
        pass

    def _agregar_persona(self):
        #self.var = ControladorAgregarPaciente()
        #self.__vista.close() <-- cerrar la lista de pacientes? creo que queaaría mejor dejarla abierta pero no accesible hasta que la nueva ventana se cierre
        pass

    def _get_datos_tabla(self):
        datos = self.__base.getAll("SELECT dni_paciente, nombre_paciente, turno_prox_paciente FROM public.paciente") #un método que traiga todas las tuplas de las columnas expecificadas de la tabla PACIENTE de la BD
        return datos

    def _buscar_paciente_nombre(self,dato): #creo que tendríamos otros de este tipo para cada dato del paciente que se pueda usar como busqueda
        datos = self.__base.getAll("SELECT dni_paciente, nombre_paciente, turno_prox_paciente FROM public.paciente WHERE nombre_paciente = '{}'".format(dato))
        return datos


    def _filtra_turnos_hoy(self,dato):
        datos = self.__base.getAll("SELECT dni_paciente, nombre_paciente, turno_prox_paciente FROM public.paciente WHERE turno_prox_paciente = '{}'".format(dato))
        return datos
