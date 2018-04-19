import matplotlib
from PyQt5.QtWidgets import QSizePolicy
from scipy.interpolate import *

matplotlib.use("Qt5Agg")
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MplCanvasWrapper(FigureCanvas):
    def __init__(self, parent=None, ):
        self.fig = Figure(facecolor='white', dpi=50,tight_layout=True)
        FigureCanvas.__init__(self, self.fig)
        # self.resize(800, 800)
        self.setParent(parent)
        self.ax = self.fig.add_subplot(111)
        # FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
