# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ndvi_dialog_base.ui'
#
# Created: Tue Dec 06 01:15:25 2016
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog
from qgis.core import QgsProject
from qgis.core import QgsMapLayerRegistry
from qgis.core import QgsMapLayer
from logger import Logger
from water_calculator import WaterCalculator



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

class Ui_ndviDialogBase(object):
    def __init__(self, ndviDialogBase):
        ndviDialogBase.setObjectName(_fromUtf8("ndviDialogBase"))
        ndviDialogBase.resize(400, 300)
        self.button_box = QtGui.QDialogButtonBox(ndviDialogBase)
        self.button_box.accepted.connect(self.accepted)
        self.button_box.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.verticalLayoutWidget = QtGui.QWidget(ndviDialogBase)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 371, 41))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.R_combo_box = QtGui.QComboBox(self.verticalLayoutWidget)
        self.R_combo_box.setObjectName(_fromUtf8("R_combo_box"))
        self.verticalLayout_2.addWidget(self.R_combo_box)
        self.verticalLayoutWidget_2 = QtGui.QWidget(ndviDialogBase)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 60, 371, 41))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.NIR_combo_box = QtGui.QComboBox(self.verticalLayoutWidget_2)
        self.NIR_combo_box.setObjectName(_fromUtf8("NIR_combo_box"))
        self.verticalLayout_3.addWidget(self.NIR_combo_box)
        self.verticalLayoutWidget_3 = QtGui.QWidget(ndviDialogBase)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 110, 371, 41))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_4.addWidget(self.label_3)
        self.ndvi_text_box = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.ndvi_text_box.setObjectName(_fromUtf8("ndvi_text_box"))
        self.verticalLayout_4.addWidget(self.ndvi_text_box)
        self.load_to_canvas = QtGui.QCheckBox(ndviDialogBase)
        self.load_to_canvas.setGeometry(QtCore.QRect(20, 240, 111, 17))
        self.load_to_canvas.setObjectName(_fromUtf8("load_to_canvas"))
        self.verticalLayoutWidget_4 = QtGui.QWidget(ndviDialogBase)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 160, 371, 46))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_5.addWidget(self.label_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.output_file_text_box = QtGui.QLineEdit(self.verticalLayoutWidget_4)
        self.output_file_text_box.setObjectName(_fromUtf8("output_file_text_box"))
        self.horizontalLayout.addWidget(self.output_file_text_box)
        self.browse_button = QtGui.QPushButton(self.verticalLayoutWidget_4)
        self.browse_button.clicked.connect(self.open_browse)
        self.browse_button.setObjectName(_fromUtf8("browse_button"))
        self.horizontalLayout.addWidget(self.browse_button)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.retranslateUi(ndviDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), ndviDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), ndviDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(ndviDialogBase)

    def retranslateUi(self, ndviDialogBase):
        ndviDialogBase.setWindowTitle(_translate("ndviDialogBase", "1NDVI", None))
        self.label.setText(_translate("ndviDialogBase", "R:", None))
        self.label_2.setText(_translate("ndviDialogBase", "NIR:", None))
        self.label_3.setText(_translate("ndviDialogBase", "NDVI slieksnis:", None))
        self.load_to_canvas.setText(_translate("ndviDialogBase", "Load to canvas", None))
        self.label_4.setText(_translate("ndviDialogBase", "Output", None))
        self.browse_button.setText(_translate("ndviDialogBase", "Browse...", None))

    def load_images(self, iface):
        Logger.log("Loading images")
        self.iface = iface
        layers = iface.legendInterface().layers()
        for layer in layers:
            if layer.type() == QgsMapLayer.RasterLayer:
                self.R_combo_box.addItem( layer.name(), layer )
                self.NIR_combo_box.addItem( layer.name(), layer )

    def open_browse(self):
        filename1 = QFileDialog.getSaveFileName(None, 'Save As', QgsProject.instance().readPath("./") , '*.tif')
        self.output_file_text_box.setText(filename1)

    def accepted(self):
        Logger.log("OK button pressed")
        red_layer = str(self.R_combo_box.currentText())
        nir_layer = str(self.NIR_combo_box.currentText())
        ndvi_threshold = str(self.ndvi_text_box.text())
        output_file_name = str(self.output_file_text_box.text())
        load_to_canvas = str(self.load_to_canvas.checkState())

        calculator = WaterCalculator(red_layer, nir_layer, ndvi_threshold, output_file_name, load_to_canvas)
        output = calculator.calculate_water_area()
        Logger.log("Checkbox status: " + str(self.load_to_canvas.checkState()))
        if self.load_to_canvas.checkState()==2:
            layer = self.iface.addRasterLayer(output, "Leyer calculated with ndvi plugin")
