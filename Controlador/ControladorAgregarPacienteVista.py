#from Vista.AgregarPacienteVista import AgregarPacienteVista   | nombres a definir
from modelo.BaseDeDatos import BaseDeDatos
from modelo.Paciente import Paciente


class ControladorAgregarPacienteVista:

    def __init__(self):
        #self.__vista = AgregarPacienteVista(self)
        #self.__vista.show()
        self.__base = BaseDeDatos()
        pass

    def _guardar_datos_paciente(self):
        #-- ¿las validaciones de datos las hace el controlador?
        # nombre = self.__vista.get_nombre()
        # if nombre etcetc:
        #     no guarda y muestra un dialog indicando el error
        # else
        #     guarda en la bd
        #     self.__base.agregar_paciente()
        # ¿manda los datos como tupla? 
        pass

    def _muestra_dialog_guardar(self):
        #diaglog
        # guardar TRUE entonces self._guardar_datos_paciente()
        # guardar FALSE no pasa nada, la ventana no se cierra
        pass
    

    def _muestra_dialog_cancelar(self):
        #diaglog
        # cancelar TRUE entonces se cierra la ventana
        # cancelar FALSE no pasa nada, la ventana no se cierra
        pass