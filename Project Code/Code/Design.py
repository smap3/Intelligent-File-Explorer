# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design.ui'
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
        MainWindow.resize(514, 200)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(514, 200))
        MainWindow.setTabShape(QtGui.QTabWidget.Triangular)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.BTN_SelFolder = QtGui.QPushButton(self.centralwidget)
        self.BTN_SelFolder.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BTN_SelFolder.setObjectName(_fromUtf8("BTN_SelFolder"))
        self.gridLayout.addWidget(self.BTN_SelFolder, 0, 0, 1, 1)
        self.RB_AdvClustering = QtGui.QRadioButton(self.centralwidget)
        self.RB_AdvClustering.setObjectName(_fromUtf8("RB_AdvClustering"))
        self.gridLayout.addWidget(self.RB_AdvClustering, 3, 0, 1, 2)
        self.LE_FolderPath = QtGui.QLineEdit(self.centralwidget)
        self.LE_FolderPath.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.LE_FolderPath.setAutoFillBackground(False)
        self.LE_FolderPath.setObjectName(_fromUtf8("LE_FolderPath"))
        self.gridLayout.addWidget(self.LE_FolderPath, 0, 1, 1, 1)
        self.RB_BasicClustering = QtGui.QRadioButton(self.centralwidget)
        self.RB_BasicClustering.setChecked(True)
        self.RB_BasicClustering.setObjectName(_fromUtf8("RB_BasicClustering"))
        self.gridLayout.addWidget(self.RB_BasicClustering, 1, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.BTN_Process = QtGui.QPushButton(self.centralwidget)
        self.BTN_Process.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BTN_Process.setObjectName(_fromUtf8("BTN_Process"))
        self.verticalLayout.addWidget(self.BTN_Process)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 514, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuAbout.sizePolicy().hasHeightForWidth())
        self.menuAbout.setSizePolicy(sizePolicy)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.actionDocumentation = QtGui.QAction(MainWindow)
        self.actionDocumentation.setObjectName(_fromUtf8("actionDocumentation"))
        self.actionOverview = QtGui.QAction(MainWindow)
        self.actionOverview.setObjectName(_fromUtf8("actionOverview"))
        self.actionAuthors = QtGui.QAction(MainWindow)
        self.actionAuthors.setObjectName(_fromUtf8("actionAuthors"))
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionOverview)
        self.menuAbout.addAction(self.actionAuthors)
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Multidimensional Association in Heterogeneous Media Files", None))
        self.BTN_SelFolder.setText(_translate("MainWindow", "Select Folder", None))
        self.RB_AdvClustering.setText(_translate("MainWindow", "Advanced Clustering (Requires Internet for Information Search)", None))
        self.LE_FolderPath.setPlaceholderText(_translate("MainWindow", "Folder Path", None))
        self.RB_BasicClustering.setText(_translate("MainWindow", "Basic Clustering (Local processing)", None))
        self.BTN_Process.setText(_translate("MainWindow", "Process", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation", None))
        self.actionOverview.setText(_translate("MainWindow", "Overview", None))
        self.actionAuthors.setText(_translate("MainWindow", "Authors", None))

