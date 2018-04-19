from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QApplication,QGridLayout,QMainWindow
from MplMainWindow import Ui_MainWindow
from PyQt5.QtCore import pyqtSlot, QThread,QTimer,QElapsedTimer
import re
import numpy as np
import time
MINIMUM_TIME_INTERVEL = 0.0000001
from matplotlib.animation import FuncAnimation
import threading
import csv
import os
from backend import *
from main import testing_data, testing_data_weighted


class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.main = Ui_MainWindow()
        self.main.setupUi(self)
        self.setWindowTitle(u"Cubic Spline Fitting and Interpolation (PENG Zhenghao)")
        self.canvas = self.main.canvas
        self.ax = self.main.canvas.ax
        self.ifGen = False

    def print(self, str):
        self.main.print.append(str)
        self.main.print.moveCursor(11)

    @QtCore.pyqtSlot()
    def on_load_clicked(self):
        self.main.data.setPlainText(testing_data)

    @QtCore.pyqtSlot()
    def on_load_weight_clicked(self):
        self.main.data.setPlainText(testing_data_weighted)

    @QtCore.pyqtSlot()
    def on_read_clicked(self):
        file_name = QFileDialog.getOpenFileName(self, "Open File",filter="Csv files(*.csv);;Txt files(*.txt)")
        # file_name = QFileDialog.getOpenFileName(self, "Open File", "",
        #                                         "Csv files(*.csv);;Txt files(*.txt)")
        data = []
        if file_name[1]=='Csv files(*.csv)' or file_name[1]=='Txt files(*.txt)':
            with open(file_name[0], 'r') as f:
                self.main.data.setPlainText(f.read())
        else:
            return None


    @QtCore.pyqtSlot()
    def on_generate_clicked(self):
        self.ifGen = True
        self.generate()

    @QtCore.pyqtSlot(float)
    def on_smooth_factor_valueChanged(self):
        if self.ifGen:
            self.generate()

    @QtCore.pyqtSlot()
    def on_pushButton_clicked(self):
        if self.ifGen:
            self.print("Generating series-curves w.r.t. smooth factor...")
            arr,_ = self.read()
            x, y = fit(arr, 0)
            self.ax.plot(x, y, c='k', label="smooth factor 0")
            li = np.logspace(0, 2, 16)
            for smooth in li:
                x, y = fit(arr, smooth)
                self.ax.plot(x, y, label="smooth factor {}".format(smooth))
            self.ax.legend()
            self.canvas.draw()


    def read(self):
        d = self.main.data.document()
        smooth = eval(self.main.smooth_factor.text())
        if d.toPlainText() == "":
            self.print("Empty input!")
            return
        arr = [eval(i) for i in (d.toPlainText()).split('\n')]
        try:
            arr = np.array(arr, dtype=np.float32)
        except ValueError:
            self.print("""Input data should be in forms of:
         	x,y,weight 
        or 	x,y 
        Examples:
         	1,1,1
         	2,2,2 
        or
         	1,1
         	2,2
         	Wrong input!""")
            return
        return arr, smooth


    def generate(self):
        self.ax.clear()
        arr, smooth = self.read()
        self.print("Generating figure with {} samples and the weight is {} and smooth is {}".format(arr.shape[0], 'on' if arr.shape[
                                                                                                             1] == 3 else 'Off', smooth))
        self.ax.scatter(arr[:, 0], arr[:, 1], c='k', marker='.', s=20)
        # x, y = fit(arr)
        x, y = fit(arr, smooth)
        self.ax.plot(x,y,c='r',label="smooth factor {}".format(smooth))
        x, y = fit(arr, 0)
        self.ax.plot(x,y,c='b', label="smooth factor 0")
        self.ax.legend()
        self.canvas.draw()