# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from mplcanvaswrapper import MplCanvasWrapper
textplaceholder = """Welcome to the cubic spline fitting program. 
All codes are wrote by PENG Zhenghao leveraging QT, scipy, matplotlib libraries.
Type your data or import a .csv/.txt file. 
You can also click "Load data" bottoms to import testing data.
Then click "generate" botton to get the figure.
Click "auto" after "generate" to get a series-figure w.r.t. smooth factor.
------ 
Input data should be in forms of:
 	x,y,weight 
or 	x,y 
Examples:
 	1,1,1
 	2,2,2 
or
 	1,1
 	2,2             
"""

text = """Input data should be in forms of:
 	x,y,weight 
or 	x,y 
Examples:
 	1,1,1
 	2,2,2 
or
 	1,1
 	2,2"""



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.canvas = MplCanvasWrapper(self.centralWidget)
        self.canvas.setGeometry(QtCore.QRect(280, 20, 600, 400))
        self.canvas.setObjectName("canvas")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 251, 541))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.data = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.data.setObjectName("data")
        self.verticalLayout.addWidget(self.data)
        self.load = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.load.setObjectName("load")
        self.verticalLayout.addWidget(self.load)
        self.load_weight = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.load_weight.setObjectName("load_weight")
        self.verticalLayout.addWidget(self.load_weight)
        self.read = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.read.setObjectName("read")
        self.verticalLayout.addWidget(self.read)
        self.generate = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.generate.setObjectName("generate")
        self.verticalLayout.addWidget(self.generate)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.smooth_factor = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.smooth_factor.setDecimals(6)
        self.smooth_factor.setMaximum(1001.0)
        self.smooth_factor.setSingleStep(0.05)
        self.smooth_factor.setProperty("value", 0.0)
        self.smooth_factor.setObjectName("smooth_factor")
        self.horizontalLayout.addWidget(self.smooth_factor)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.print = QtWidgets.QTextBrowser(self.centralWidget)
        self.print.setGeometry(QtCore.QRect(280, 440, 600, 120))
        self.print.setObjectName("print")
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cubic Spline Fitting"))
        self.data.setPlaceholderText(_translate("MainWindow", "Import your data!"))
        self.load.setText(_translate("MainWindow", "Load data without weight"))
        self.load_weight.setText(_translate("MainWindow", "Load data with weight"))
        self.read.setText(_translate("MainWindow", "Read from .csv/.txt"))
        self.generate.setText(_translate("MainWindow", "Generate figure"))
        self.label.setText(_translate("MainWindow", "Smooth "))
        self.print.setText(_translate("MainWindow", textplaceholder))
        self.pushButton.setText(_translate("MainWindow", "Auto"))
