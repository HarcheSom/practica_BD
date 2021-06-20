import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore

# from modules.login import Login
from modules.main_ui import Ui_MainWindows
from modules.ui_functions import Ui_functions


import os
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindows()
        self.ui.setupUi(self)

        global this
        this = self.ui

        self.windows_maximized = False

        self.ui_functions = Ui_functions(self)
        # self.ui_functions.remove_border()
        

        
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.Dialog)
        self.setWindowFlags(flags|QtCore.Qt.FramelessWindowHint |QtCore.Qt.CustomizeWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)#fondo de la ventana transparente

        # Ui_functions.Ui_functions(self)

        self.init()

        # self.login = Login()
        # self.login.exec_()
        # if self.login.cancel:
        #     QMessageBox.about(self,"Error","No se puede cerrar sin acceder.")
        #     sys.exit(self)

        this.btn_ventas.clicked.connect(self.menu)
        this.btn_compras.clicked.connect(self.menu)
        this.btn_productos.clicked.connect(self.menu)
        this.btn_proveedores.clicked.connect(self.menu)
        this.btn_tickets.clicked.connect(self.menu)
        this.btn_recorte_caja.clicked.connect(self.menu)
        this.btn_copia_seguridad.clicked.connect(self.menu)

        this.btn_closed.clicked.connect(self.close)
        this.btn_maximized.clicked.connect(self.show_windows)
        this.btn_minimized.clicked.connect(self.showMinimized)

        #self.showFullScreen()
		#self.showMaximized()
		#self.showMinimized()
		#self.showNormal()




    def init(self):
        # this.main.setStyleSheet("#main {background:red;}")
        this.App.setStyleSheet("#App {box-shadow: 5px 10px #888888;}")
        pass
        
    def show_windows(self):
        if self.windows_maximized:
            self.showNormal()
        else:
            self.showMaximized()
        self.windows_maximized = not self.windows_maximized
    
    def menu(self):
        btn = self.sender()
        btn_name = btn.objectName()
        print(btn_name)

        select = this.stackedWidget.setCurrentWidget
        if btn_name == "btn_ventas":
            select(this.page_ventas)
        elif btn_name == "btn_compras":
            select(this.page_compras)
        elif btn_name == "btn_productos":
            select(this.page_productos)
        elif btn_name == "btn_tickets":
            select(this.page_tickets)
        elif btn_name == "btn_proveedores":
            select(this.page_proveedores)
        elif btn_name == "btn_recorte_caja":
            select(this.page_recorte_caja)
        elif btn_name == "btn_copia_seguridad":
            select(this.page_copia_seguridad)

    
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            try:
                self.old_pos_active = True
                self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
                event.accept()
            except Exception as e:
                pass

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton and self.old_pos_active:
            try:
                self.move(event.globalPos() - self.dragPosition)
                event.accept()
            except Exception as e:
                pass

    def mouseReleaseEvent(self, event):
        self.old_pos_active = False


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())

    # pyside6-uic main.ui > main_ui.py
    # pyside6-rcc resources.qrc -o resources_rc.py