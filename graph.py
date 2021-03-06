from PyQt4 import QtCore,QtGui
import pyqtgraph as pg
import numpy as np
from copy import deepcopy
import time

class Graph(pg.PlotWidget):
    """docstring for Graph"""
    def __init__(self,beamline):
        super(Graph, self).__init__()
        self.beamline = beamline

        self.x = []
        self.y = []

        self.start = time.time()

    def updateGraph(self):
        self.x.append(time.time()-self.start)
        self.y = np.append(self.y,self.beamline.current.value)
        
        self.x0 = self.beamline.optimalTime-self.start

        self.plotData()

    def plotData(self):
        self.plot(np.array(self.x),np.array(self.y),clear=True,pen = 'r')

        self.plot([self.x0],[self.beamline.max],pen='r', symbol='o')

    def clearPlot(self):
        self.x = []
        self.y = []
        self.clear()

class VoltGraph(Graph):
    def __init__(self,beamline,voltName):
        super(VoltGraph, self).__init__(beamline)

        self.voltName = voltName

    def updateGraph(self):
        self.x.append(self.beamline.voltages[self.voltName].readback)
        self.y = np.append(self.y,self.beamline.current.value)
        self.x0 = self.beamline.optimalSettings[self.voltName]

        self.plotData()

