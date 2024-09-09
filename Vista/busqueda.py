import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,QTableWidgetItem
from PyQt6.uic import loadUi 
from PyQt6.QtCore import Qt

class busqueda (QMainWindow,QWidget):
    
    def __init__(self):
        super(busqueda,self).__init__()
        loadUi("Busqueda.ui",self)
        #self.ventana()
        self.cargar_datos()
        
        
    def cargar_datos(self):
        
        info = [
            {"nombre": "Lucas", "apellido":"Vidal","DNI": 13221412},
            {"nombre": "Lucas", "apellido":"Vidal","DNI": 23123123},
            {"nombre": "Lucas", "apellido":"Vidal","DNI": 33434534},
            {"nombre": "Lucas", "apellido":"Vidal","DNI": 43123454},
            {"nombre": "Lucas", "apellido":"Vidal","DNI": 52133245},
            {"nombre": "Lucas", "apellido":"Vidal","DNI": 52132245}
        ]
        
        self.table_1.setRowCount(len(info))
        self.table_1.setColumnCount(3)
        self.table_1.setFixedSize(345,210)
        self.table_1.setColumnWidth(0,110)
        self.table_1.setColumnWidth(1,110)
        self.table_1.setColumnWidth(2,110)
        self.table_1.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        index = 0
        for a in info:
            self.table_1.setItem(index,0, QTableWidgetItem(str(a["nombre"])))
            self.table_1.setItem(index,1, QTableWidgetItem(str(a["apellido"])))
            self.table_1.setItem(index,2, QTableWidgetItem(str(a["DNI"])))
            index += 1
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = busqueda()
    window.show()
    sys.exit(app.exec())