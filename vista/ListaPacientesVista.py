from PyQt6.Qtwidgets import QTableWidget,QVBoxLayout,QLineEdit,QWidget,QPushButton,QHBoxLayout,QComboBox

class ListarPacienteVista(QWidget):

    def __init__(self,controladorListarPacienteVista,controladorDetallePaciente):
        super().__init__()
        self.setGeometry(100,100,250,250)
        self.setWindowTitle("Pacientes ")

        self.__comboBoxCriterio = QComboBox()
        self.__comboBoxCriterio.addItems(["DNI","Apellido","Nombre"])
        
        self.__barraBusqueda=QLineEdit()
        self.__barraBusqueda.setPlaceholderText("Buscar")
        self.__barraBusqueda.textchanget.connect(self.filtrar_pacientes())
        
        self.__tablaPacientes =QTableWidget()# mirar
        self.__tablaPacientes.setColumnCount(4)
        self.__tablaPacientes.setHorizontalHeaderLabels(["Nombre","Apellido","DNI","Proximio Turno"])
        
        self.__botonNuevoPaciente =QPushButton("Nuevo Paciente")
        self.__botonNuevoPaciente.clicked.connect(controladorListarPacienteVista.agregar_paciente())
        
        self.__botonVerPaciente =QPushButton("Ver Paciente")
        self.__botonVerPaciente.clicked.connect(controladorDetallePaciente.verPaciente())
        
        self.__layoutPrincipal=QVBoxLayout()
        self.__layoutBotones =QHBoxLayout()
        self.__layoutBusqueda =QHBoxLayout()
        
        self.__layoutBusqueda.addWidget(self.__comboBoxCriterio)
        self.__layoutBusqueda.addWidget(self.__barraBusqueda)
        
        self.__layoutPrincipal.addWidget(self.__layoutBusqueda)
        self.__layoutPrincipal.addWidget(self.__tablaPacientes)
        
        self.__layoutBotones.addWidget(self.__botonNuevoPaciente)
        self.__layoutBotones.addWidget(self.__botonVerPaciente)
        
        self.__layoutPrincipal.addLayout(self.__layoutBotones)
        
        self.setLayout(self.__layoutPrincipal)
        


