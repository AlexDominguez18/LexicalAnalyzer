from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from ui_mainwindow import Ui_MainWindow
from lexical_analyzer import LexicalAnalyzer

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Slots
        self.ui.analyzePB.clicked.connect(self.analyze_btn_clicked)
        self.ui.clearPB.clicked.connect(self.clear_all_areas)
    
    @pyqtSlot()
    def analyze_btn_clicked(self):
        codeText = self.ui.codeTextEdit.toPlainText()
        if (len(codeText)):
            print(self.ui.codeTextEdit.toPlainText())
        else:
            message = QMessageBox()
            message.setIcon(QMessageBox.Warning)
            message.setWindowTitle("Error")
            message.setText("El área de texto está vacía.")
            message.exec()

    @pyqtSlot()
    def clear_all_areas(self):
        self.ui.codeTextEdit.clear()
        self.ui.assemblyTextEdit.clear()
        self.ui.resultsTB.clearContents()