# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProgressDesign.ui'
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

class Ui_ProgressWindow(object):
    def setupUi(self, ProgressWindow):
        ProgressWindow.setObjectName(_fromUtf8("ProgressWindow"))
        ProgressWindow.resize(461, 315)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProgressWindow.sizePolicy().hasHeightForWidth())
        ProgressWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(ProgressWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.TB_ProgressLog = QtGui.QTextBrowser(self.centralwidget)
        self.TB_ProgressLog.setObjectName(_fromUtf8("TB_ProgressLog"))
        self.verticalLayout.addWidget(self.TB_ProgressLog)
        self.PB_ProgressBar = QtGui.QProgressBar(self.centralwidget)
        self.PB_ProgressBar.setProperty("value", 24)
        self.PB_ProgressBar.setObjectName(_fromUtf8("PB_ProgressBar"))
        self.verticalLayout.addWidget(self.PB_ProgressBar)
        ProgressWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProgressWindow)
        QtCore.QMetaObject.connectSlotsByName(ProgressWindow)

    def retranslateUi(self, ProgressWindow):
        ProgressWindow.setWindowTitle(_translate("ProgressWindow", "Progress Window", None))

