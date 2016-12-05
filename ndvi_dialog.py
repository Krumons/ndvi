# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ndviDialog
                                 A QGIS plugin
 NDVI
                             -------------------
        begin                : 2016-12-06
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Roberts Krūms
        email                : robertskruums@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic
from qgis.core import QgsMapLayer
from qgis.core import QgsMapLayerRegistry

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'ndvi_dialog_base.ui'))


class ndviDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ndviDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

    def load_images(self):
        layers = QgsMapLayerRegistry.instance().mapLayers().values()
        for layer in layers:
            if layer.type() == QgsMapLayer.RasterLayer:
                self.R_combo_box.addItem( layer.name(), layer )
                self.NIR_combo_box.addItem( layer.name(), layer )

    def get_selected_images(self):
        r_layer = R_combo_box.itemData(R_combo_box.currentIndex())
        nir_layer =  NIR_combo_box.itemData(NIR_combo_box.currentIndex())
