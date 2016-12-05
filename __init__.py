# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ndvi
                                 A QGIS plugin
 NDVI
                             -------------------
        begin                : 2016-12-06
        copyright            : (C) 2016 by Roberts Krūms
        email                : robertskruums@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ndvi class from file ndvi.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .ndvi import ndvi
    return ndvi(iface)
