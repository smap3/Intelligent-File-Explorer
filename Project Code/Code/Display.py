# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Display.ui'
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
        MainWindow.resize(605, 373)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.TW_Table = QtGui.QTableWidget(self.centralwidget)
        self.TW_Table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.TW_Table.setObjectName(_fromUtf8("TW_Table"))
        self.TW_Table.setColumnCount(3)
        self.TW_Table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.TW_Table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.TW_Table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.TW_Table.setHorizontalHeaderItem(2, item)
        self.TW_Table.horizontalHeader().setDefaultSectionSize(184)
        self.verticalLayout.addWidget(self.TW_Table)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.PB_td = QtGui.QPushButton(self.centralwidget)
        self.PB_td.setObjectName(_fromUtf8("PB_td"))
        self.horizontalLayout.addWidget(self.PB_td)
        self.PB_cp = QtGui.QPushButton(self.centralwidget)
        self.PB_cp.setObjectName(_fromUtf8("PB_cp"))
        self.horizontalLayout.addWidget(self.PB_cp)
        self.PB_as = QtGui.QPushButton(self.centralwidget)
        self.PB_as.setObjectName(_fromUtf8("PB_as"))
        self.horizontalLayout.addWidget(self.PB_as)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 605, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        item = self.TW_Table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Cluster", None))
        item = self.TW_Table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Keywords", None))
        item = self.TW_Table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Files", None))
        self.PB_td.setText(_translate("MainWindow", "Display Topic Distribution", None))
        self.PB_cp.setText(_translate("MainWindow", "Display Clustering Plot", None))
        self.PB_as.setText(_translate("MainWindow", "Display Associations", None))

