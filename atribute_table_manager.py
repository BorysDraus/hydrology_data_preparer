import sys
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox, QWidget
from qgis.core import QgsProject, Qgis, QgsVectorLayer, QgsProcessingFeedback,  QgsFields, QgsCoordinateReferenceSystem
from qgis._core import QgsWkbTypes, QgsMapLayer, QgsVectorFileWriter, QgsVectorDataProvider, QgsField, QgsRectangle, QgsMapLayerProxyModel, QgsProcessing
from qgis.core import *





class AtibuteTableManager():


    def removeDataFrolLayerByValue(self, layer, column_name, value):

        #01 Declare fildto analize by filed (column name)
        field = layer.fields().indexFromName(str(column_name))

        #02 Delare empty list to store ids of data to remove
        list_of_data_to_remove = []

        # 03 Loop by all feature
        # for row in layer.getSelectedFeatures():
        for row in layer.getFeatures():

            # Declare id of feature (row)
            id = row.id()

            # Declare cuurent feature
            feature = layer.getFeature(id)

            # Declare feature to compare
            # for instance: "ROWY", "LINIE"
            feature_to_compare = (feature[field] or 0)

            if feature_to_compare == value:
                list_of_data_to_remove.append(id)

        # 04 Decalre layers capabilities
        capabilities = layer.dataProvider().capabilities()



        # 05 Check if there is possibility to remove data from that layer
        if capabilities & QgsVectorDataProvider.DeleteFeatures:
            # Deleting features by ids from list
            layer.dataProvider().deleteFeatures(list_of_data_to_remove)
            # Data refresh
            layer.triggerRepaint()


