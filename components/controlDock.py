import sys
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
from pyqtgraph.dockarea import Dock
from customTypes import ThreadType
from components.scaleButtons import ScaleButtons
from components.onoffswitch import MySwitch, OnOffSwitch
from components.analoggaugewidget import AnalogGaugeWidget

class ControlDock(Dock):

    def __init__(self):
        super().__init__("Control")
        self.widget = pg.LayoutWidget()

        #self.startBtn = QtGui.QPushButton("Start All")
        #self.stopBtn = QtGui.QPushButton("Stop All")
        self.quitBtn = QtGui.QPushButton("quit")
        self.quitBtn.setStyleSheet(
            "QPushButton {color:#f9ffd9; background:#ed2a0c;}"
            "QPushButton:disabled {color:#8f8f8f; background:#bfbfbf;}"
        )
        self.quitBtn.setFont(QtGui.QFont('serif',16))

        #self.prasmaLabel = QtGui.QLabel(self.__setLabelFont("Plasma Current", "#000001"))
        #self.prasmaStatus = QtGui.QLabel(self.__setStatusFont(False))
        #self.valuePraBw = QtGui.QTextBrowser()
        #self.valuePraBw.setMaximumHeight(45)
        #self.valuePraBw.setMaximumWidth(130)
        #self.praScaleBtns = ScaleButtons()

        self.tempLabel = QtGui.QLabel(self.__setLabelFont("Temperature", "#000001"))
        #self.tempStatus = QtGui.QLabel(self.__setStatusFont(False))
        self.valueTBw = QtGui.QTextBrowser()
        self.valueTBw.setMaximumHeight(100)
        #self.valueTBw.setMaximumWidth(130)
        self.tScaleBtns = ScaleButtons()
#        self.tScaleBtns.setStyleSheet(
#            "QComboBox {color:#f9ffd9; background:#ed2a0c;}"            
#        )        
        #self.tScaleBtns.setFont(QtGui.QFont('serif',20))
        
        #self.pressure1Label = QtGui.QLabel(self.__setLabelFont("Pressure1", "#000001"))
        #self.pressure1Status = QtGui.QLabel(self.__setStatusFont(False))
        #self.valueP1Bw = QtGui.QTextBrowser()
        #self.valueP1Bw.setMaximumHeight(45)
        #self.valueP1Bw.setMaximumWidth(130)
        #self.p1ScaleBtns = ScaleButtons()

        #self.pressure2Label = QtGui.QLabel(self.__setLabelFont("Pressure2", "#000001"))
        #self.pressure2Status = QtGui.QLabel(self.__setStatusFont(False))
        #self.valueP2Bw = QtGui.QTextBrowser()
        #self.valueP2Bw.setMaximumHeight(45)
        #self.valueP2Bw.setMaximumWidth(130)
        #self.p2ScaleBtns = ScaleButtons()

        self.FullNormSW = MySwitch()
        self.OnOffSW = OnOffSwitch()
        self.OnOffSW.setFont(QtGui.QFont('serif',16))
        
        # Analog Gauge to show Temperature
        self.gaugeT = AnalogGaugeWidget()
        self.gaugeT.set_MinValue(0)
        self.gaugeT.set_MaxValue(400)
        self.gaugeT.set_total_scale_angle_size(180)
        self.gaugeT.set_start_scale_angle(180)
        self.gaugeT.set_enable_value_text(False)

        self.__setLayout()

    def __setLayout(self):
        self.addWidget(self.widget)

        #self.widget.addWidget(self.startBtn, 0, 0)
        #self.widget.addWidget(self.stopBtn, 0, 1)
        self.widget.addWidget(self.OnOffSW, 0, 0)
        self.widget.addWidget(self.quitBtn, 0, 1)

#        self.widget.addWidget(self.prasmaLabel, 1, 0)
#        self.widget.addWidget(self.prasmaStatus, 1, 1)
#        self.widget.addWidget(self.valuePraBw, 2, 0, 1, 1)
#        self.widget.addWidget(self.praScaleBtns, 2, 1, 1, 1)


#        self.widget.addWidget(self.tempLabel, 3, 0)
#        self.widget.addWidget(self.tempStatus, 3, 1)
        self.widget.addWidget(self.valueTBw, 1, 0,1,2)
        self.widget.addWidget(self.tScaleBtns, 2, 1)
        self.widget.addWidget(self.FullNormSW,2,0)
        # Temperature analouge gauge
        self.widget.addWidget(self.gaugeT,3,0)
        
#        self.widget.addWidget(self.pressure1Label, 5, 0)
#        self.widget.addWidget(self.pressure1Status, 5, 1)
#        self.widget.addWidget(self.valueP1Bw, 6, 0, 1, 1)
#        self.widget.addWidget(self.p1ScaleBtns, 6, 1, 1, 1)

#        self.widget.addWidget(self.pressure2Label, 7, 0)
#        self.widget.addWidget(self.pressure2Status, 7, 1)
#        self.widget.addWidget(self.valueP2Bw, 8, 0, 1, 1)
#        self.widget.addWidget(self.p2ScaleBtns, 8, 1, 1, 1)
        
        self.verticalSpacer = QtGui.QSpacerItem(
            0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding
        )
        self.widget.layout.setVerticalSpacing(5)
        self.widget.layout.addItem(self.verticalSpacer)

    def __setLabelFont(self, text: str, color: str):
        txt = "<font color={}><h3>{}</h3></font>".format(color, text)
        return txt

    def __setStatusFont(self, active: bool):
        color = "#FF005D" if active else "#002AFF"
        txt = "Active" if active else "InActive"
        return "<font color={}><h3>{}</h3></font>".format(color, txt)

    def setStatus(self, ttype: ThreadType, active: bool):
        txt = self.__setStatusFont(active)
        if ttype == ThreadType.PRASMA:
            self.prasmaStatus.setText(txt)
        elif ttype == ThreadType.TEMPERATURE:
            self.tempStatus.setText(txt)
        elif ttype == ThreadType.PRESSURE1:
            self.pressure1Status.setText(txt)
        elif ttype == ThreadType.PRESSURE2:
            self.pressure2Status.setText(txt)
        else:
            return

    def setBwtext(self, ttype: ThreadType, value: float):
        """ Update value in the value browser """
        # Obsolete, exchanged to one browser for all, set-up in main.py
        
        txt = f"""<font size=5 color="#d1451b">{value:.2f}</font>"""
        if ttype == ThreadType.PRASMA:
            self.valuePraBw.setText(txt)
        elif ttype == ThreadType.TEMPERATURE:
            self.valueTBw.setText(txt)
        elif ttype == ThreadType.PRESSURE1:
            self.valueP1Bw.setText(txt)
        elif ttype == ThreadType.PRESSURE2:
            self.valueP2Bw.setText(txt)
        else:
            return

if __name__ == "__main__":
    pass
