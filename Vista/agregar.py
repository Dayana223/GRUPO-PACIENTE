import sys
from PyQt6.QtWidgets import QApplication ,QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox


class new_user(QWidget):
    def __init__(self):
        super().__init__()
        self.inicio()
        
    def inicio(self):
        self.setGeometry(300,300,310,310)
        self.setWindowTitle("Datos  Paciente")
        self.generar_formulario()
        self.show()
        
    def generar_formulario(self):
        
        name_label = QLabel(self)
        name_label.setText("Datos del Paciente")
        name_label.move(92,24)
        
        name_label = QLabel(self)
        name_label.setText("Nombre:")
        name_label.move(20,54)
        
        self.name_input = QLineEdit(self)
        self.name_input.resize(200,24)
        self.name_input.move(90,50)
        
        name2_label = QLabel(self)
        name2_label.setText("Apellido:")
        name2_label.move(20,94)
        
        self.name2_input = QLineEdit(self)
        self.name2_input.resize(200,24)
        self.name2_input.move(90,90)
        
        dni_label = QLabel(self)
        dni_label.setText("DNI:")
        dni_label.move(20,134)
        
        self.dni_input = QLineEdit(self)
        self.dni_input.resize(200,24)
        self.dni_input.move(90,130)
        
        agregar_button = QPushButton(self)
        agregar_button.setText("Agregar")
        agregar_button.resize(200,28)
        agregar_button.move(60,220)
    
        cancelar_button = QPushButton(self)
        cancelar_button.setText("Cancelar")
        cancelar_button.resize(200,28)
        cancelar_button.move(60,260)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = new_user()
    sys.exit(app.exec())
    
    