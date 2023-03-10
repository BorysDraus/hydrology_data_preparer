# -*- coding: utf-8 -*-
"""
/***************************************************************************
 HydrologyDataPreparer
                                 A QGIS plugin
 App for load date from difrent source to hydrology format
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-01-22
        copyright            : (C) 2023 by BULiGL
        email                : borys.draus@gmail.com
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
    """Load HydrologyDataPreparer class from file HydrologyDataPreparer.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .hydrology_data_preparer import HydrologyDataPreparer
    return HydrologyDataPreparer(iface)
