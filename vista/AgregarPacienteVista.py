from PyQt6.Qtwidgets import QWidget,QPushButton,QHBoxLayout

class AgregarPacienteVista(QWidget):

    def __init__(self,controladorAgregarPaciente):
        self.setGeometry(100,100,250,250)
        self.setWindowTitle("Agregar Paciente")
        self.__boton = QPushButton("Agregar")
        self.__layout =QHBoxLayout()
        self.__boton.clicked.connect(controladorAgregarPaciente)
        self.__layout.addWidget(self.__boton)
        self.setLayout(self.__layout) 


