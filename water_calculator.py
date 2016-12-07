from osgeo import gdal
from qgis.core import QgsProject
from logger import Logger
from gdalconst import *
import numpy as np
from numpy import *


class WaterCalculator(object):
        def __init__(self, rband, nirband, ndvi_thr, output, load):
            Logger.log("Initializing water calculator")
            self.project_path = QgsProject.instance().readPath("./")
            self.r_band_path =  str(self.project_path) + '/' + str(rband) + '.tif'
            self.nir_band_path = str(self.project_path)+ '/' + str(nirband) + '.tif'
            self.output_file_path = output
            self.ndvi_threshold = ndvi_thr
            self.load_to_canvas = load


        def open_tiff(self, path):
            Logger.log("Opening file")
            Logger.log("File path " + str(path))
            dataset = gdal.Open(path, GA_ReadOnly )
            self.band1 = dataset.GetRasterBand(1)
            dataArray = dataset.ReadAsArray()
            dataArray = array(dataArray, dtype = float)
            return dataArray

        def calculate_ndvi(self, r, nir):
            Logger.log("Calculating ndvi")
            return (nir - r) / (nir + r)

        def find_water_area(self, r, nir, thr):
            Logger.log("Finding water area")
            ndvi = self.calculate_ndvi(r,nir)
            ndvi[ndvi < thr] = 0
            ndvi[ndvi > thr] = 1
            Logger.log("Size of array: " + str(len(ndvi)))

            return ndvi

        def write_to_file(self, output, data):
            driver = gdal.GetDriverByName("GTiff")
            datasetOut = driver.Create(output, data.shape[0], data.shape[1], 1, self.band1.DataType)
            CopyDatasetInfo(data,datasetOut)
            bandOut=datasetOut.GetRasterBand(1)
            BandWriteArray(bandOut, dataOut)
            bandOut = None

        def calculate_water_area(self):
            r_values = self.open_tiff(self.r_band_path)
            nir_values = self.open_tiff(self.nir_band_path)
            ndvi_area = self.find_water_area(r_values, nir_values, self.ndvi_threshold)
            self.write_to_file(self.output_file_path, ndvi_area)
