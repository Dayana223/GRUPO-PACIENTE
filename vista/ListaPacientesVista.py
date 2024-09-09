from PyQt6.Qtwidgets import QWidget,QPushButton,QHBoxLayout

class ListarPacienteVista(QWidget):

    def __init__(self,controladorListarPacienteVista):
        self.setGeometry(100,100,250,250)
        self.setWindowTitle("Detalle Paciente")
        self.__boton = QPushButton("Modificar Paciente")
        self.__layout =QHBoxLayout()
        self.__boton.clicked.connect(controladorListarPacienteVista)
        self.__layout.addWidget(self.__boton)
        self.setLayout(self.__layout) 


