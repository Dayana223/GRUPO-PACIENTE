import sys
from PyQt6.QtWidgets import QApplication 
from controlador.ControladorAgregarPacienteVista import ControladorAgregarPacienteVista
from controlador.ControladorListaPacienteVista import ControladorListarPacientesVista



app = QApplication(sys.argv)
var =ControladorAgregarPacienteVista()
var2=ControladorListarPacientesVista()
app.exc()