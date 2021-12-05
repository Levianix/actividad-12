from mainWindow import MainWindow
from PySide2.QtWidgets import QApplication
import sys

#Aplicación de QT
app=QApplication()
#Se crea un botón con la palabra "Hola"
window=MainWindow()
#Se hace visible el botón
window.show()
#Qt loop
sys.exit(app.exec_())
