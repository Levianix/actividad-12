# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiact10.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1166, 735)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_6 = QGridLayout(self.tab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.contGlo = QGroupBox(self.tab)
        self.contGlo.setObjectName(u"contGlo")
        self.gridLayout = QGridLayout(self.contGlo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ory_lab_2 = QSpinBox(self.contGlo)
        self.ory_lab_2.setObjectName(u"ory_lab_2")
        self.ory_lab_2.setEnabled(True)
        self.ory_lab_2.setMaximum(500)

        self.gridLayout.addWidget(self.ory_lab_2, 2, 1, 1, 1)

        self.id_spin = QSpinBox(self.contGlo)
        self.id_spin.setObjectName(u"id_spin")

        self.gridLayout.addWidget(self.id_spin, 0, 1, 1, 1)

        self.orx_spin = QSpinBox(self.contGlo)
        self.orx_spin.setObjectName(u"orx_spin")
        self.orx_spin.setEnabled(True)
        self.orx_spin.setMaximum(500)

        self.gridLayout.addWidget(self.orx_spin, 1, 1, 1, 1)

        self.desy_lab = QLabel(self.contGlo)
        self.desy_lab.setObjectName(u"desy_lab")

        self.gridLayout.addWidget(self.desy_lab, 4, 0, 1, 1)

        self.desy_spin = QSpinBox(self.contGlo)
        self.desy_spin.setObjectName(u"desy_spin")
        self.desy_spin.setEnabled(True)
        self.desy_spin.setMaximum(500)

        self.gridLayout.addWidget(self.desy_spin, 4, 1, 1, 1)

        self.id_lab = QLabel(self.contGlo)
        self.id_lab.setObjectName(u"id_lab")

        self.gridLayout.addWidget(self.id_lab, 0, 0, 1, 1)

        self.ory_lab = QLabel(self.contGlo)
        self.ory_lab.setObjectName(u"ory_lab")

        self.gridLayout.addWidget(self.ory_lab, 2, 0, 1, 1)

        self.desx_spin = QSpinBox(self.contGlo)
        self.desx_spin.setObjectName(u"desx_spin")
        self.desx_spin.setEnabled(True)
        self.desx_spin.setMaximum(500)

        self.gridLayout.addWidget(self.desx_spin, 3, 1, 1, 1)

        self.vel_lab = QLabel(self.contGlo)
        self.vel_lab.setObjectName(u"vel_lab")

        self.gridLayout.addWidget(self.vel_lab, 5, 0, 1, 1)

        self.orx_lab = QLabel(self.contGlo)
        self.orx_lab.setObjectName(u"orx_lab")

        self.gridLayout.addWidget(self.orx_lab, 1, 0, 1, 1)

        self.desx_lab = QLabel(self.contGlo)
        self.desx_lab.setObjectName(u"desx_lab")

        self.gridLayout.addWidget(self.desx_lab, 3, 0, 1, 1)

        self.vel_spin = QSpinBox(self.contGlo)
        self.vel_spin.setObjectName(u"vel_spin")

        self.gridLayout.addWidget(self.vel_spin, 5, 1, 1, 1)


        self.gridLayout_6.addWidget(self.contGlo, 0, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.tab)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_6.addWidget(self.plainTextEdit, 0, 1, 2, 1)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.colred_lab = QLabel(self.groupBox)
        self.colred_lab.setObjectName(u"colred_lab")

        self.gridLayout_2.addWidget(self.colred_lab, 0, 0, 1, 1)

        self.colred_spin = QSpinBox(self.groupBox)
        self.colred_spin.setObjectName(u"colred_spin")
        self.colred_spin.setMaximum(255)

        self.gridLayout_2.addWidget(self.colred_spin, 0, 1, 1, 1)

        self.colgr_lab = QLabel(self.groupBox)
        self.colgr_lab.setObjectName(u"colgr_lab")

        self.gridLayout_2.addWidget(self.colgr_lab, 1, 0, 1, 1)

        self.colgr_spin = QSpinBox(self.groupBox)
        self.colgr_spin.setObjectName(u"colgr_spin")
        self.colgr_spin.setMaximum(255)

        self.gridLayout_2.addWidget(self.colgr_spin, 1, 1, 1, 1)

        self.colbl_lab = QLabel(self.groupBox)
        self.colbl_lab.setObjectName(u"colbl_lab")

        self.gridLayout_2.addWidget(self.colbl_lab, 2, 0, 1, 1)

        self.colbl_spin = QSpinBox(self.groupBox)
        self.colbl_spin.setObjectName(u"colbl_spin")
        self.colbl_spin.setMaximum(255)

        self.gridLayout_2.addWidget(self.colbl_spin, 2, 1, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox, 1, 0, 1, 1)

        self.botMosRes = QPushButton(self.tab)
        self.botMosRes.setObjectName(u"botMosRes")

        self.gridLayout_6.addWidget(self.botMosRes, 2, 0, 1, 1)

        self.areaMos = QPlainTextEdit(self.tab)
        self.areaMos.setObjectName(u"areaMos")

        self.gridLayout_6.addWidget(self.areaMos, 2, 1, 3, 1)

        self.botEnvPrio = QPushButton(self.tab)
        self.botEnvPrio.setObjectName(u"botEnvPrio")

        self.gridLayout_6.addWidget(self.botEnvPrio, 3, 0, 1, 1)

        self.botEnvNorm = QPushButton(self.tab)
        self.botEnvNorm.setObjectName(u"botEnvNorm")

        self.gridLayout_6.addWidget(self.botEnvNorm, 4, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.mostrarTabla_pushButton = QPushButton(self.tab_2)
        self.mostrarTabla_pushButton.setObjectName(u"mostrarTabla_pushButton")

        self.gridLayout_4.addWidget(self.mostrarTabla_pushButton, 1, 2, 1, 1)

        self.table = QTableWidget(self.tab_2)
        self.table.setObjectName(u"table")

        self.gridLayout_4.addWidget(self.table, 0, 0, 1, 3)

        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout_4.addWidget(self.buscar_lineEdit, 1, 0, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_4.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_9 = QGridLayout(self.tab_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.textBrowser = QTextBrowser(self.tab_3)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout_9.addWidget(self.textBrowser, 2, 0, 1, 1)

        self.dibujarPushButton = QPushButton(self.tab_3)
        self.dibujarPushButton.setObjectName(u"dibujarPushButton")

        self.gridLayout_9.addWidget(self.dibujarPushButton, 5, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.orXLabel_2 = QLabel(self.groupBox_2)
        self.orXLabel_2.setObjectName(u"orXLabel_2")

        self.gridLayout_5.addWidget(self.orXLabel_2, 1, 0, 1, 1)

        self.orXSpinBox = QSpinBox(self.groupBox_2)
        self.orXSpinBox.setObjectName(u"orXSpinBox")
        self.orXSpinBox.setMaximum(500)

        self.gridLayout_5.addWidget(self.orXSpinBox, 0, 1, 2, 1)

        self.orYSpinBox_3 = QSpinBox(self.groupBox_2)
        self.orYSpinBox_3.setObjectName(u"orYSpinBox_3")
        self.orYSpinBox_3.setMaximum(500)

        self.gridLayout_5.addWidget(self.orYSpinBox_3, 2, 1, 2, 1)

        self.orYLabel_3 = QLabel(self.groupBox_2)
        self.orYLabel_3.setObjectName(u"orYLabel_3")

        self.gridLayout_5.addWidget(self.orYLabel_3, 3, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.limpiarPushButton_2 = QPushButton(self.tab_3)
        self.limpiarPushButton_2.setObjectName(u"limpiarPushButton_2")

        self.gridLayout_9.addWidget(self.limpiarPushButton_2, 4, 0, 1, 1)

        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_9.addWidget(self.graphicsView, 0, 1, 6, 1)

        self.recoPushButton_3 = QPushButton(self.tab_3)
        self.recoPushButton_3.setObjectName(u"recoPushButton_3")

        self.gridLayout_9.addWidget(self.recoPushButton_3, 3, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1166, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir...", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar...", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.contGlo.setTitle(QCoreApplication.translate("MainWindow", u"Captura de Part\u00edculas", None))
        self.desy_lab.setText(QCoreApplication.translate("MainWindow", u"Destino y", None))
        self.id_lab.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.ory_lab.setText(QCoreApplication.translate("MainWindow", u"Origen en y", None))
        self.vel_lab.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.orx_lab.setText(QCoreApplication.translate("MainWindow", u"Origen en x", None))
        self.desx_lab.setText(QCoreApplication.translate("MainWindow", u"Destino x", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Color Part\u00edcula", None))
        self.colred_lab.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.colgr_lab.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.colbl_lab.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.botMosRes.setText(QCoreApplication.translate("MainWindow", u"Mostrar Resultados", None))
        self.botEnvPrio.setText(QCoreApplication.translate("MainWindow", u"Enviar con Prioridad", None))
        self.botEnvNorm.setText(QCoreApplication.translate("MainWindow", u"Enviar Normal", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.mostrarTabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar por id.....", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.dibujarPushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Origen", None))
        self.orXLabel_2.setText(QCoreApplication.translate("MainWindow", u"OrigenX", None))
        self.orYLabel_3.setText(QCoreApplication.translate("MainWindow", u"OrigenY", None))
        self.limpiarPushButton_2.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.recoPushButton_3.setText(QCoreApplication.translate("MainWindow", u"Recorrer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Gr\u00e1ficas", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

