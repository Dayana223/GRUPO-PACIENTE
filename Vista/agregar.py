import sys
from PyQt6.QtWidgets import QApplication ,QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox,QTextEdit, QVBoxLayout,QMainWindow
from PyQt6.uic import loadUi 

class new_user(QMainWindow,QWidget):
    
    def __init__(self):
        super(new_user,self).__init__()
        loadUi("Agregar.ui",self)
        self.agregar()
        
    def agregar(self):
        
        
        self.name.setPlaceholderText("Nombre...")
        self.name2.setPlaceholderText("Apellido...")
        self.dni.setPlaceholderText("DNI...")
        self.grupo_sanguineo.setPlaceholderText("Grupo Sanguineo...")
        
        # Interaciones de Botones
        self.add_button.clicked.connect(self.add_paciente)
        self.close_button.clicked.connect(self.close)
    
    # Funcion de Prueba de Botones
    def add_paciente(self):
        nombre = self.name.text()
        apellido = self.name2.text()
        dni = self.dni.text()
        grupo_sanguineo = self.grupo_sanguineo.text()
        print(nombre,apellido,dni,grupo_sanguineo)
        
        # Limpiar los campos de entrada
        if nombre and apellido and dni and grupo_sanguineo:
            self.name.clear()
            self.name2.clear()
            self.dni.clear()
            self.grupo_sanguineo.clear()
    
    def clase (self):
        self.deleteLater()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = new_user()
    ventana.show()
    sys.exit(app.exec())
    
    
