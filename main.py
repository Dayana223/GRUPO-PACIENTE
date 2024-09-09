import sys
from PyQt6.QtWidgets import QApplication 
from Controlador.ControladorAgregarPacienteVista import ControladorAgregarPacienteVista
from Controlador.ControladorListaPacientesVista import ControladorListaPacientesVista



app = QApplication(sys.argv)
var =ControladorAgregarPacienteVista()
var2=ControladorListaPacientesVista()
app.exc()