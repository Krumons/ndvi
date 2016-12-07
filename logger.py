from qgis.core import QgsMessageLog


class Logger(object):
        @staticmethod
        def log(message):
            QgsMessageLog.logMessage(str(message), 'NDVI plugin log')
