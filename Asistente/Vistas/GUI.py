# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'agenteInmobiliarioTxHWiv.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(912, 524)
        Dialog.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout_6 = QVBoxLayout(Dialog)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.frame)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 0))
        self.frame_superior.setMaximumSize(QSize(16777215, 40))
        self.frame_superior.setStyleSheet(u"QFrame{\n"
"background-color: rgb(108, 211, 255);\n"
"background-color: rgb(0,0,0);\n"
"	\n"
"	\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: #000000ff;\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(53, 53, 79);\n"
"border-radius: 20px;\n"
"\n"
"}\n"
"")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_superior)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(200, 0))
        icon = QIcon()
        icon.addFile(u"./img/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(675, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_minimizar = QPushButton(self.frame_superior)
        self.btn_minimizar.setObjectName(u"btn_minimizar")
        self.btn_minimizar.setMinimumSize(QSize(40, 40))
        self.btn_minimizar.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"./img/menos (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimizar.setIcon(icon1)
        self.btn_minimizar.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_minimizar)

        self.btn_restaurar = QPushButton(self.frame_superior)
        self.btn_restaurar.setObjectName(u"btn_restaurar")
        self.btn_restaurar.setMinimumSize(QSize(40, 40))
        self.btn_restaurar.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"./img/flecha-hacia-abajo-a-la-izquierda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_restaurar.setIcon(icon2)
        self.btn_restaurar.setIconSize(QSize(100, 100))

        self.horizontalLayout.addWidget(self.btn_restaurar)

        self.btn_maximizar = QPushButton(self.frame_superior)
        self.btn_maximizar.setObjectName(u"btn_maximizar")
        self.btn_maximizar.setMinimumSize(QSize(40, 40))
        self.btn_maximizar.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"./img/flecha (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximizar.setIcon(icon3)
        self.btn_maximizar.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_maximizar)

        self.btn_cerrar = QPushButton(self.frame_superior)
        self.btn_cerrar.setObjectName(u"btn_cerrar")
        self.btn_cerrar.setMinimumSize(QSize(40, 40))
        self.btn_cerrar.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"./img/x (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cerrar.setIcon(icon4)
        self.btn_cerrar.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_cerrar)


        self.verticalLayout_2.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(self.frame)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setMinimumSize(QSize(0, 0))
        self.frame_inferior.setMaximumSize(QSize(16777215, 16777215))
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_menu = QFrame(self.frame_inferior)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setStyleSheet(u"QFrame{\n"
"background-color: rgb(53, 53, 79);\n"
"}\n"
"QPushButton{\n"
"font: 87 12pt \"Arial Black\";\n"
"background-color: rgb(53, 53, 79);\n"
"color: rgb(20, 200, 220);\n"
"border-radius: 5px;\n"
"border: 1px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:black;\n"
"}\n"
"")
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.btn_mostrarCatalogo = QPushButton(self.frame_menu)
        self.btn_mostrarCatalogo.setObjectName(u"btn_mostrarCatalogo")
        self.btn_mostrarCatalogo.setLayoutDirection(Qt.LeftToRight)
        self.btn_mostrarCatalogo.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u"./img/documento.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_mostrarCatalogo.setIcon(icon5)
        self.btn_mostrarCatalogo.setIconSize(QSize(32, 32))

        self.verticalLayout_5.addWidget(self.btn_mostrarCatalogo)

        self.btn_buscar = QPushButton(self.frame_menu)
        self.btn_buscar.setObjectName(u"btn_buscar")
        self.btn_buscar.setToolTipDuration(2)
        self.btn_buscar.setLayoutDirection(Qt.LeftToRight)
        self.btn_buscar.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"background-color: black;\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"./img/buscar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_buscar.setIcon(icon6)
        self.btn_buscar.setIconSize(QSize(32, 32))
        self.btn_buscar.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.btn_buscar)

        self.btn_agregar = QPushButton(self.frame_menu)
        self.btn_agregar.setObjectName(u"btn_agregar")
        self.btn_agregar.setLayoutDirection(Qt.LeftToRight)
        icon7 = QIcon()
        icon7.addFile(u"./img/boton-agregar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_agregar.setIcon(icon7)
        self.btn_agregar.setIconSize(QSize(32, 32))

        self.verticalLayout_5.addWidget(self.btn_agregar)

        self.btn_vender = QPushButton(self.frame_menu)
        self.btn_vender.setObjectName(u"btn_vender")
        self.btn_vender.setLayoutDirection(Qt.LeftToRight)
        icon8 = QIcon()
        icon8.addFile(u"./img/precio.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_vender.setIcon(icon8)
        self.btn_vender.setIconSize(QSize(32, 32))

        self.verticalLayout_5.addWidget(self.btn_vender)

        self.btn_visualizar = QPushButton(self.frame_menu)
        self.btn_visualizar.setObjectName(u"btn_visualizar")
        self.btn_visualizar.setLayoutDirection(Qt.LeftToRight)
        icon9 = QIcon()
        icon9.addFile(u"./img/vision (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_visualizar.setIcon(icon9)
        self.btn_visualizar.setIconSize(QSize(32, 32))

        self.verticalLayout_5.addWidget(self.btn_visualizar)

        self.btn_editar = QPushButton(self.frame_menu)
        self.btn_editar.setObjectName(u"btn_editar")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_editar.sizePolicy().hasHeightForWidth())
        self.btn_editar.setSizePolicy(sizePolicy)
        self.btn_editar.setLayoutDirection(Qt.LeftToRight)
        icon10 = QIcon()
        icon10.addFile(u"./img/editar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_editar.setIcon(icon10)
        self.btn_editar.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.btn_editar)

        self.btn_eliminar = QPushButton(self.frame_menu)
        self.btn_eliminar.setObjectName(u"btn_eliminar")
        icon11 = QIcon()
        icon11.addFile(u"./img/eliminar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_eliminar.setIcon(icon11)
        self.btn_eliminar.setIconSize(QSize(32, 32))

        self.verticalLayout_5.addWidget(self.btn_eliminar)


        self.horizontalLayout_3.addWidget(self.frame_menu)

        self.frame_paginas = QFrame(self.frame_inferior)
        self.frame_paginas.setObjectName(u"frame_paginas")
        self.frame_paginas.setStyleSheet(u"QFrame{\n"
"background-color: rgb(61, 61, 61);\n"
"}\n"
"QLabel{\n"
"font: 87 12pt \"Arial Black\";\n"
"background-color: #000000ff;\n"
"color: rgb(20, 200, 220);\n"
"border: 0px solid #14C8DC;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 0px;\n"
"color: rgb(255, 255, 255);\n"
"border-bottom: 2px solid rgb(61, 61, 61);\n"
"font: 75 12pt \"Times New Roman\";\n"
"\n"
"}\n"
"QPushButton{\n"
"font: 87 12pt \"Arial Black\";\n"
"background-color: rgb(53, 53, 79);\n"
"color: rgb(20, 200, 220);\n"
"border-radius: 5px;\n"
"border: 1px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:black;\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0,0,0);\n"
"gridline-color: rgb(0, 206, 151);\n"
"font-size: 12pt;\n"
"color: #000000;\n"
"}\n"
"QHeaderView::section{\n"
"background-color: rgb(0, 206, 151);\n"
"border: 1px solid rgb(0,0,0);\n"
"font-size:12pt;\n"
"}\n"
"QTableWidget QTableCornerButton::section{\n"
"background-color: rgb(0,0,0);\n"
"border: 1px solid rgb(0, 206, 151);\n"
"}"
                        "\n"
"")
        self.frame_paginas.setFrameShape(QFrame.StyledPanel)
        self.frame_paginas.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_paginas)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_titulo = QFrame(self.frame_paginas)
        self.frame_titulo.setObjectName(u"frame_titulo")
        self.frame_titulo.setFrameShape(QFrame.StyledPanel)
        self.frame_titulo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_titulo)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_titulo = QLabel(self.frame_titulo)
        self.label_titulo.setObjectName(u"label_titulo")
        self.label_titulo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_titulo)


        self.verticalLayout.addWidget(self.frame_titulo)

        self.frame_form = QFrame(self.frame_paginas)
        self.frame_form.setObjectName(u"frame_form")
        self.frame_form.setFrameShape(QFrame.StyledPanel)
        self.frame_form.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.splitter = QSplitter(self.frame_form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAcceptDrops(False)
        self.label_2.setToolTipDuration(1)

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.splitter.addWidget(self.widget)
        self.widget1 = QWidget(self.splitter)
        self.widget1.setObjectName(u"widget1")
        self.verticalLayout_4 = QVBoxLayout(self.widget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_id = QLineEdit(self.widget1)
        self.lineEdit_id.setObjectName(u"lineEdit_id")

        self.verticalLayout_4.addWidget(self.lineEdit_id)

        self.lineEdit_tipo = QLineEdit(self.widget1)
        self.lineEdit_tipo.setObjectName(u"lineEdit_tipo")

        self.verticalLayout_4.addWidget(self.lineEdit_tipo)

        self.lineEdit_ubi = QLineEdit(self.widget1)
        self.lineEdit_ubi.setObjectName(u"lineEdit_ubi")

        self.verticalLayout_4.addWidget(self.lineEdit_ubi)

        self.lineEdit_dim = QLineEdit(self.widget1)
        self.lineEdit_dim.setObjectName(u"lineEdit_dim")

        self.verticalLayout_4.addWidget(self.lineEdit_dim)

        self.splitter.addWidget(self.widget1)

        self.horizontalLayout_2.addWidget(self.splitter)

        self.splitter_2 = QSplitter(self.frame_form)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.widget2 = QWidget(self.splitter_2)
        self.widget2.setObjectName(u"widget2")
        self.verticalLayout_7 = QVBoxLayout(self.widget2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_7.addWidget(self.label_6)

        self.label_7 = QLabel(self.widget2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_7.addWidget(self.label_7)

        self.label_8 = QLabel(self.widget2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_7.addWidget(self.label_8)

        self.label_9 = QLabel(self.widget2)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_7.addWidget(self.label_9)

        self.splitter_2.addWidget(self.widget2)
        self.widget3 = QWidget(self.splitter_2)
        self.widget3.setObjectName(u"widget3")
        self.verticalLayout_8 = QVBoxLayout(self.widget3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_valor = QLineEdit(self.widget3)
        self.lineEdit_valor.setObjectName(u"lineEdit_valor")

        self.verticalLayout_8.addWidget(self.lineEdit_valor)

        self.lineEdit_cuartos = QLineEdit(self.widget3)
        self.lineEdit_cuartos.setObjectName(u"lineEdit_cuartos")

        self.verticalLayout_8.addWidget(self.lineEdit_cuartos)

        self.lineEdit_lavados = QLineEdit(self.widget3)
        self.lineEdit_lavados.setObjectName(u"lineEdit_lavados")

        self.verticalLayout_8.addWidget(self.lineEdit_lavados)

        self.lineEdit_url = QLineEdit(self.widget3)
        self.lineEdit_url.setObjectName(u"lineEdit_url")

        self.verticalLayout_8.addWidget(self.lineEdit_url)

        self.splitter_2.addWidget(self.widget3)

        self.horizontalLayout_2.addWidget(self.splitter_2)


        self.verticalLayout.addWidget(self.frame_form)

        self.frame_msj = QFrame(self.frame_paginas)
        self.frame_msj.setObjectName(u"frame_msj")
        self.frame_msj.setFrameShape(QFrame.StyledPanel)
        self.frame_msj.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_msj)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_msj = QLabel(self.frame_msj)
        self.lbl_msj.setObjectName(u"lbl_msj")
        self.lbl_msj.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_5.addWidget(self.lbl_msj)

        self.btn_limpiar = QPushButton(self.frame_msj)
        self.btn_limpiar.setObjectName(u"btn_limpiar")

        self.horizontalLayout_5.addWidget(self.btn_limpiar)

        self.horizontalLayout_5.setStretch(0, 8)
        self.horizontalLayout_5.setStretch(1, 2)

        self.verticalLayout.addWidget(self.frame_msj)

        self.frame_table = QFrame(self.frame_paginas)
        self.frame_table.setObjectName(u"frame_table")
        self.frame_table.setFrameShape(QFrame.StyledPanel)
        self.frame_table.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_table)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget = QTableWidget(self.frame_table)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_table)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 7)

        self.horizontalLayout_3.addWidget(self.frame_paginas)

        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 8)

        self.verticalLayout_2.addWidget(self.frame_inferior)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)

        self.verticalLayout_6.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText("")
        self.btn_minimizar.setText("")
        self.btn_restaurar.setText("")
        self.btn_maximizar.setText("")
        self.btn_cerrar.setText("")
        self.btn_mostrarCatalogo.setText(QCoreApplication.translate("Dialog", u"CATALOGO ", None))
#if QT_CONFIG(tooltip)
        self.btn_buscar.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_buscar.setText(QCoreApplication.translate("Dialog", u"BUSCAR", None))
        self.btn_agregar.setText(QCoreApplication.translate("Dialog", u"AGREGAR", None))
        self.btn_vender.setText(QCoreApplication.translate("Dialog", u"VENDER", None))
        self.btn_visualizar.setText(QCoreApplication.translate("Dialog", u"VER", None))
        self.btn_editar.setText(QCoreApplication.translate("Dialog", u"EDITAR", None))
        self.btn_eliminar.setText(QCoreApplication.translate("Dialog", u"ELIMINAR", None))
        self.label_titulo.setText(QCoreApplication.translate("Dialog", u"PROPIEDADES", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>este valor es obligatorio para su llenado</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_2.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>que es esto</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_2.setText(QCoreApplication.translate("Dialog", u"ID", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"TIPO", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"UBICACI\u00d3N", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"DIMENSI\u00d3N", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"VALOR", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"CUARTOS", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"BA\u00d1OS", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"URL", None))
        self.lbl_msj.setText("")
        self.btn_limpiar.setText(QCoreApplication.translate("Dialog", u"LIMPIAR", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"TIPO", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"UBICACI\u00d3N", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"VALOR", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"DIMENSI\u00d3N", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"CUARTOS", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"BA\u00d1OS", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"URL", None));
    # retranslateUi

