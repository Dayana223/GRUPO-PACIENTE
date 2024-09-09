import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit

class AgregarPacienteVista(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Agregar Paciente") 

        # Etiquetas y campos de texto
        self.__dni = QLabel("DNI:")
        self.__lineEditDni = QLineEdit()
        
        self.__nombre = QLabel("Nombre:")
        self.__lineEditNombre = QLineEdit()
        
        self.__apellido = QLabel("Apellido:")
        self.__lineEditApellido = QLineEdit()
        
        # Botón para agregar paciente
        self.__botonGuardar= QPushButton("Guardar")
        self.__botonCancelar = QPushButton("Cancelar")
        # Conectar el botón al método que agregar paciente (a definir en el controlador)
        # self.__botonAgregar.clicked.connect(controladorAgregarPaciente.agregar_paciente)

        # Layout para el botón
        self.__layoutBoton = QHBoxLayout()
        self.__layoutBoton.addWidget(self.__botonGuardar)
        self.__layoutBoton.addWidget(self.__botonCancelar)
        
        # Layout para el formulario
        self.__layoutForm = QVBoxLayout()
        self.__layoutForm.addWidget(self.__dni)
        self.__layoutForm.addWidget(self.__lineEditDni)
        self.__layoutForm.addWidget(self.__nombre)
        self.__layoutForm.addWidget(self.__lineEditNombre)
        self.__layoutForm.addWidget(self.__apellido)
        self.__layoutForm.addWidget(self.__lineEditApellido)
        
        # Layout principal
        self.__ventanaPrincipalLayout = QVBoxLayout()
        self.__ventanaPrincipalLayout.addLayout(self.__layoutForm)
        self.__ventanaPrincipalLayout.addLayout(self.__layoutBoton)
        
        # Setear el layout principal en la ventana
        self.setLayout(self.__ventanaPrincipalLayout)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = AgregarPacienteVista()
    ventana.show()  # Mostrar la ventana
    sys.exit(app.exec())
