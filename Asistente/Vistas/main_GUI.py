from PySide6 import QtCore
from PySide6.QtCore import QPropertyAnimation, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QApplication, QDialog, QTableWidgetItem
from Asistente.Vistas.GUI import Ui_Dialog
from Asistente.Modelo.asistente import Asistente
from Asistente.Modelo.cliente import Cliente
from Asistente.Modelo.webScraping import PropertyScraper


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.build_gui()
        self.scraper: PropertyScraper = PropertyScraper()
        e, _ = self.scraper.scrape_properties()
        self.ui.lbl_msj.setText(e)
        self.asistente: Asistente = Asistente(self.scraper)
        self.cliente: Cliente = Cliente(nombre= "Usuario", asistente= self.asistente)


    def build_gui(self):
        self.ui.btn_restaurar.hide()
        self.ui.btn_cerrar.clicked.connect(lambda: self.close())
        self.ui.btn_minimizar.clicked.connect(self.control_btn_minimizar)
        self.ui.btn_restaurar.clicked.connect(self.control_btn_restaurar)
        self.ui.btn_maximizar.clicked.connect(self.control_btn_maximizar)
        self.ui.pushButton.clicked.connect(self.mover_menu)
        self.ui.btn_limpiar.clicked.connect(self.control_btn_limpiar)
        self.ui.btn_mostrarCatalogo.clicked.connect(self.llenar_tabla)
        self.ui.btn_agregar.clicked.connect(self.agregar)
        self.ui.tableWidget.cellClicked.connect(self.openUrl)
        self.ui.btn_buscar.clicked.connect(self.buscar)
        self.ui.btn_visualizar.clicked.connect(self.visualizar)
        self.ui.btn_vender.clicked.connect(self.poner_venta)
        self.ui.btn_editar.clicked.connect(self.editar)
    def control_btn_minimizar(self):
        self.showMinimized()
    def control_btn_restaurar(self):
        self.showNormal()
        self.ui.btn_restaurar.hide()
        self.ui.btn_maximizar.show()
    def control_btn_maximizar(self):
        self.showMaximized()
        self.ui.btn_restaurar.show()
        self.ui.btn_maximizar.hide()
    def mover_menu(self):
        width = self.ui.frame_menu.width()
        normal = 0
        if width == 0:
            extender = 200
        else:
            extender = normal

        self.animacion = QPropertyAnimation(self.ui.frame_menu, b'minimumWidth')
        self.animacion.setDuration(300)
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(extender)

        self.animacion.start()

    def control_btn_limpiar(self):
        self.ui.lineEdit_id.clear()
        self.ui.lineEdit_tipo.clear()
        self.ui.lineEdit_ubi.clear()
        self.ui.lineEdit_valor.clear()
        self.ui.lineEdit_cuartos.clear()
        self.ui.lineEdit_lavados.clear()
        self.ui.lineEdit_dim.clear()
        self.ui.lineEdit_url.clear()




    def llenar_tabla(self):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)

        _, lista = self.asistente.mostrar_catalogo()
        i = len(lista)
        self.ui.tableWidget.setRowCount(i)

        for row, propiedad in enumerate(lista):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(propiedad.id)))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(propiedad.tipo)))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(propiedad.ubicacion)))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(propiedad.dimension)))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(propiedad.valor)))
            self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(str(propiedad.habitaciones)))
            self.ui.tableWidget.setItem(row, 6, QTableWidgetItem(str(propiedad.lavados)))
            self.ui.tableWidget.setItem(row, 7, QTableWidgetItem(str(propiedad.url)))


    def openUrl(self, row, column):
        if column != 7:
            return
        url_text = self.ui.tableWidget.item(row, 7).text()
        url = QUrl(url_text)
        if url.isValid():
            QDesktopServices.openUrl(url)

    def agregar(self):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)
        id = len(self.cliente.propiedades_cliente)
        dict ={

        'tipo':  self.ui.lineEdit_tipo.text().upper(),
        'ubicacion':  self.ui.lineEdit_ubi.text().upper(),
        'valor':  self.ui.lineEdit_valor.text().upper(),
        'habitaciones':  self.ui.lineEdit_cuartos.text().upper(),
        'lavados':  self.ui.lineEdit_lavados.text().upper(),
        'dimension':  self.ui.lineEdit_dim.text().upper(),
        'url': self.ui.lineEdit_url.text().upper()
        }


        string, booleano=self.cliente.agregar_propiedad(dict['tipo'],dict['ubicacion'],dict['dimension'], dict['valor'], dict['lavados'], dict['habitaciones'], dict['url'] )
        if booleano == True:
            row_index = self.ui.tableWidget.rowCount()  # Obtener el índice de la próxima fila disponible
            self.ui.tableWidget.insertRow(row_index)

            self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(str(id)))
            self.ui.tableWidget.setItem(0, 1, QTableWidgetItem(str(dict['tipo'])))
            self.ui.tableWidget.setItem(0, 2, QTableWidgetItem(str(dict['ubicacion'])))
            self.ui.tableWidget.setItem(0, 3, QTableWidgetItem(str(dict['dimension'])))
            self.ui.tableWidget.setItem(0, 4, QTableWidgetItem(str(dict['valor'])))
            self.ui.tableWidget.setItem(0, 5, QTableWidgetItem(str(dict['habitaciones'])))
            self.ui.tableWidget.setItem(0, 6, QTableWidgetItem(str(dict['lavados'])))
            self.ui.tableWidget.setItem(0, 7, QTableWidgetItem(str(dict['url'])))
            self.ui.lbl_msj.setText(string)
        else:
            self.ui.lbl_msj.setText(string)
        self.control_btn_limpiar()



    def buscar(self):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)
        dict = {
            'id': self.ui.lineEdit_id.text().upper() if self.ui.lineEdit_id.text() else None,
            'tipo': self.ui.lineEdit_tipo.text().upper() if self.ui.lineEdit_tipo.text() else None,
            'ubicacion': self.ui.lineEdit_ubi.text().upper() if self.ui.lineEdit_ubi.text() else None,
            'valor': self.ui.lineEdit_valor.text().upper() if self.ui.lineEdit_valor.text() else None,
            'habitaciones': self.ui.lineEdit_cuartos.text().upper() if self.ui.lineEdit_cuartos.text() else None,
            'lavados': self.ui.lineEdit_lavados.text().upper() if self.ui.lineEdit_lavados.text() else None,
            'dimension': self.ui.lineEdit_dim.text().upper() if self.ui.lineEdit_dim.text() else None,
            'url': self.ui.lineEdit_url.text().upper() if self.ui.lineEdit_url.text() else None
        }

        propiedades_encontradas = self.asistente.buscar(
            dict['tipo'],
            dict['ubicacion'],
            dict['valor'],
            dict['habitaciones'],
            dict['lavados'],
            dict['dimension']
        )
        i = len(propiedades_encontradas)
        self.ui.tableWidget.setRowCount(i)
        for row, propiedad in enumerate(propiedades_encontradas):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(propiedad.id)))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(propiedad.tipo)))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(propiedad.ubicacion)))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(propiedad.dimension)))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(propiedad.valor)))
            self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(str(propiedad.habitaciones)))
            self.ui.tableWidget.setItem(row, 6, QTableWidgetItem(str(propiedad.lavados)))
            self.ui.tableWidget.setItem(row, 7, QTableWidgetItem(str(propiedad.url)))

        self.ui.lbl_msj.setText("Propiedades encontradas: {}".format(i))
        self.control_btn_limpiar()

    def poner_venta(self):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)
        id = self.ui.lineEdit_id.text().upper()
        msj = self.cliente.poner_venta(id)

        _, list = self.asistente.mostrar_catalogo()
        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(str(list[-1].id)))
        self.ui.tableWidget.setItem(0, 1, QTableWidgetItem(str(list[-1].tipo)))
        self.ui.tableWidget.setItem(0, 2, QTableWidgetItem(str(list[-1].ubicacion)))
        self.ui.tableWidget.setItem(0, 3, QTableWidgetItem(str(list[-1].dimension)))
        self.ui.tableWidget.setItem(0, 4, QTableWidgetItem(str(list[-1].valor)))
        self.ui.tableWidget.setItem(0, 5, QTableWidgetItem(str(list[-1].habitaciones)))
        self.ui.tableWidget.setItem(0, 6, QTableWidgetItem(str(list[-1].lavados)))
        self.ui.tableWidget.setItem(0, 7, QTableWidgetItem(str(list[-1].url)))

        self.ui.lbl_msj.setText(msj)
        self.control_btn_limpiar()
    def visualizar(self):
        _, lista = self.cliente.mostrar_propiedades_cliente()
        i = len(lista)
        self.ui.tableWidget.setRowCount(i)

        for row, propiedad in enumerate(lista):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(propiedad.id)))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(propiedad.tipo)))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(propiedad.ubicacion)))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(propiedad.dimension)))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(propiedad.valor)))
            self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(str(propiedad.habitaciones)))
            self.ui.tableWidget.setItem(row, 6, QTableWidgetItem(str(propiedad.lavados)))
            self.ui.tableWidget.setItem(row, 7, QTableWidgetItem(str(propiedad.url)))

    def editar(self):
        tipo = self.ui.lineEdit_tipo.text().upper()
        ubicacion =  self.ui.lineEdit_ubi.text().upper()
        valor = self.ui.lineEdit_valor.text().upper()
        habitaciones = self.ui.lineEdit_cuartos.text().upper()
        lavados = self.ui.lineEdit_lavados.text().upper()
        dimension = self.ui.lineEdit_dim.text().upper()
        url = self.ui.lineEdit_url.text().upper()


        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)
        id_str = self.ui.lineEdit_id.text().upper()
        msj = self.cliente.editar_propiedad(id_str, tipo, ubicacion, valor, lavados, habitaciones, dimension, url)
        self.ui.lbl_msj.setText(msj)
        self.control_btn_limpiar()