from PySide2.QtGui import QPen, QColor
from ui_mainwindow import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from particula import Particula
from PySide2.QtCore import Slot
from particulas import Particulas
from random import randint
from pprint import pprint

#se hereda las propiedades de QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        #para llamar al constructor de clase padre
        super(MainWindow,self).__init__()
        self.particulas=Particulas()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        #interfaz agregar 1
        #Se captan las señales de los botones para que realicen acciones
        self.ui.botEnvNorm.clicked.connect(self.clickEnviarNorm)
        self.ui.botEnvPrio.clicked.connect(self.clickEnviarPrio)
        self.ui.botMosRes.clicked.connect(self.mostrar)

        #Se capta la señal para el sub-menú de arriba
        self.ui.actionAbrir.triggered.connect(self.abrir)
        self.ui.actionGuardar.triggered.connect(self.guardar)

        #interfaz Tabla 2
        self.ui.buscar_pushButton.clicked.connect(self.buscar)
        self.ui.mostrarTabla_pushButton.clicked.connect(self.mostrarTabla)

        #interfaz Gráficas
        self.ui.recoPushButton_3.clicked.connect(self.recorrer)
        self.ui.dibujarPushButton.clicked.connect(self.dibujar)
        self.ui.limpiarPushButton_2.clicked.connect(self.limpiar)

        #agregamos una escena
        self.scene=QGraphicsScene()
        #pasamos el objeto scene a nuestra graphicsview en la interfaz
        self.ui.graphicsView.setScene(self.scene)

    #Métodos 
    #interfaz agregar 1
    def abrir(self):
        #regrese solo el primer elemento
        ubicacion=QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.particulas.abrir(ubicacion):
            QMessageBox.information(self,"Exito","Se abrio correctamente en "+ubicacion)
        else:
            QMessageBox.warning(self,"Error","No se pudo abrir el archivo")

    def guardar(self):
        #Título de la ventana - donde se guardará el archivo - tipo de formato en que se guardará
        ubicacion=QFileDialog.getSaveFileName(self,'Guardar Particula','.','JSON (*.json)')
        print(ubicacion[0])
        try:
            self.particulas.guardar(ubicacion[0])
            QMessageBox.information(self,"Exito","Se guardo correctamente en "+ubicacion[0])
        except:
            QMessageBox.critical(self,"Error","No se pudo guardar el archivo")

    def clickEnviarNorm(self):
        #"value" nos regresa el valor entero o flotante del método
        #"text" - .text() nos regresa texto para guardarlo en la variable
        id=self.ui.id_spin.value()
        origenX=self.ui.orx_spin.value()
        origenY=self.ui.ory_lab_2.value()
        destinoX=self.ui.desx_spin.value()
        destinoY=self.ui.desy_spin.value()
        velocidad=self.ui.vel_spin.value()
        red=self.ui.colred_spin.value()
        green=self.ui.colgr_spin.value()
        blue=self.ui.colbl_spin.value()

        self.particulas.agregar_final(Particula(id,origenX,origenY,destinoX,destinoY,velocidad,red,green,blue)) 

    def clickEnviarPrio(self):
        #"value" nos regresa el valor entero o flotante del método
        #"text" - .text() nos regresa texto para guardarlo en la variable
        id=self.ui.id_spin.value()
        origenX=self.ui.orx_spin.value()
        origenY=self.ui.ory_lab_2.value()
        destinoX=self.ui.desx_spin.value()
        destinoY=self.ui.desy_spin.value()
        velocidad=self.ui.vel_spin.value()
        red=self.ui.colred_spin.value()
        green=self.ui.colgr_spin.value()
        blue=self.ui.colbl_spin.value()

        self.particulas.agregar_inicio(Particula(id,origenX,origenY,destinoX,destinoY,velocidad,red,green,blue)) 

    def mostrar(self):
        #mostrar datos bonitos
        self.ui.plainTextEdit.clear()
        self.particulas.ordenar()
        self.particulas.dicc()
        d=self.particulas.d
        self.ui.plainTextEdit.insertPlainText(str(self.particulas))
        
        #mostrarGraph
        self.ui.areaMos.clear()
        self.ui.areaMos.insertPlainText(str(d))
        pprint(d)

    def recorrer(self):
        print("recorrer")
        self.particulas.diccAux()
        dA=self.particulas.dA
        pprint(dA)
        

        #obtener los datos del grafo
        visitados=[]
        recorrido=[]
        pila=[]

        orX=self.ui.orXSpinBox.value()
        orY=self.ui.orYSpinBox_3.value()

        pila.append((orX,orY))

        while pila:
            actual=pila.pop()

            if actual not in visitados:
                
                visitados.append(actual)

            for k in dA[actual]:
                if k not in visitados:
                    pila.append(k)
        print("|---------------------------------------------------------------------------|")
        print("|                                 Recorrido                                 |")
        print("|",visitados)



    def buscar(self,orX,orY,desX,desY):
        camino=[]
        camino.append(inicio)

    #interfaz Tabla 2
    def buscar(self):
        print("Buscado")
        idBusqueda=int(self.ui.buscar_lineEdit.text())
        for particula in self.particulas:
            if(idBusqueda==particula.id):
                self.ui.table.clear()   
                self.ui.table.setRowCount(1)

                id =        QTableWidgetItem(str(particula.id))
                origenX =   QTableWidgetItem(str(particula.origenX))
                origenY =   QTableWidgetItem(str(particula.origenY))
                destinoX =  QTableWidgetItem(str(particula.destinoX))
                destinoY =  QTableWidgetItem(str(particula.destinoY))
                velocidad = QTableWidgetItem(str(particula.velocidad))
                red =       QTableWidgetItem(str(particula.red))
                green =     QTableWidgetItem(str(particula.green))
                blue =      QTableWidgetItem(str(particula.blue))
                distancia = QTableWidgetItem(str(particula.distancia))

                self.ui.table.setItem(0,0,id)
                self.ui.table.setItem(0,1,origenX)
                self.ui.table.setItem(0,2,origenY)
                self.ui.table.setItem(0,3,destinoX)
                self.ui.table.setItem(0,4,destinoY)
                self.ui.table.setItem(0,5,velocidad)
                self.ui.table.setItem(0,6,red)
                self.ui.table.setItem(0,7,green)
                self.ui.table.setItem(0,8,blue)
                self.ui.table.setItem(0,9,distancia)

                return
        QMessageBox.warning(self,"Error","No existen coincidencias para tu busqueda") 

    def mostrarTabla(self):
        print("Mostrar tabla")
        self.ui.table.setColumnCount(10)
        headers=["ID","Origen en x","Origen en y","Destino en x","Destino en y","Velocidad","Red","Green","Blue","Distancia"]
        self.ui.table.setHorizontalHeaderLabels(headers)
        #filas por mostrar
        self.ui.table.setRowCount(len(self.particulas))

        row=0
        for particula in self.particulas:
            id =        QTableWidgetItem(str(particula.id))
            origenX =   QTableWidgetItem(str(particula.origenX))
            origenY =   QTableWidgetItem(str(particula.origenY))
            destinoX =  QTableWidgetItem(str(particula.destinoX))
            destinoY =  QTableWidgetItem(str(particula.destinoY))
            velocidad = QTableWidgetItem(str(particula.velocidad))
            red =       QTableWidgetItem(str(particula.red))
            green =     QTableWidgetItem(str(particula.green))
            blue =      QTableWidgetItem(str(particula.blue))
            distancia = QTableWidgetItem(str(particula.distancia))

            self.ui.table.setItem(row,0,id)
            self.ui.table.setItem(row,1,origenX)
            self.ui.table.setItem(row,2,origenY)
            self.ui.table.setItem(row,3,destinoX)
            self.ui.table.setItem(row,4,destinoY)
            self.ui.table.setItem(row,5,velocidad)
            self.ui.table.setItem(row,6,red)
            self.ui.table.setItem(row,7,green)
            self.ui.table.setItem(row,8,blue)
            self.ui.table.setItem(row,9,distancia)
            row+=1

    #interfaz Gráficas
    def dibujar(self):
        print("Dibujar")

        x=100
        y=50

        for particula in self.particulas:
            origenX =   particula.origenX
            origenY =   particula.origenY
            destinoX =  particula.destinoX
            destinoY =  particula.destinoY
            red =       particula.red
            green =     particula.green
            blue =      particula.blue

            #diseños
            pen=QPen()
            pen.setWidth(2)

            r=red
            g=green
            b=blue
            color=QColor(r,g,b)
            pen.setColor(color)

            #lineas y puntos
            self.scene.addLine(origenX,origenY,destinoX,destinoY,pen)
            self.scene.addEllipse(origenX,origenY,2,2,pen)
            self.scene.addEllipse(destinoX,destinoY,2,2,pen)

            v=self.scene.addText("("+str(origenX)+","+str(origenY)+")")
            v2=self.scene.addText("("+str(destinoX)+","+str(destinoY)+")")
            v.setPos(origenX,origenY)
            v2.setPos(destinoX,destinoY)


    def limpiar(self):
        print("Limpiar")
        self.scene.clear()
        self.ui.textBrowser.clear()

    def wheelEvent(self,event):
        if(event.delta()>0):
            self.ui.graphicsView.scale(1.2,1.2)
        else:
            self.ui.graphicsView.scale(0.8,0.8)
