# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Association.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(450, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.TW_Assoc = QtGui.QTableWidget(self.centralwidget)
        self.TW_Assoc.setObjectName(_fromUtf8("TW_Assoc"))
        self.TW_Assoc.setColumnCount(2)
        self.TW_Assoc.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.TW_Assoc.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.TW_Assoc.setHorizontalHeaderItem(1, item)
        self.TW_Assoc.horizontalHeader().setDefaultSectionSize(202)
        self.verticalLayout.addWidget(self.TW_Assoc)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        item = self.TW_Assoc.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Files", None))
        item = self.TW_Assoc.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Topic", None))

