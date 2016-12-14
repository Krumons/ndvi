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
            self.geo_info = ''

        def open_tiff(self, path):
            Logger.log("Opening file")
            Logger.log("File path " + str(path))
            dataset = gdal.Open(path, GA_ReadOnly )
            self.geo_info = dataset.GetGeoTransform()
            band1 = dataset.GetRasterBand(1)
            dataArray = dataset.ReadAsArray()
            Logger.log("INput: " + str(dataArray.shape))
            return dataArray

        def calculate_ndvi(self, r, nir):
            Logger.log("Calculating ndvi")
            return (nir - r) / (nir + r)

        def find_water_area(self, r, nir, thr):
            Logger.log("Finding water area")
            self.ndvi = self.calculate_ndvi(r,nir)
            self.ndvi[self.ndvi < int(thr)] = 0
            self.ndvi[self.ndvi > int(thr)] = 1
            Logger.log(self.ndvi)

            return self.ndvi

        def write_to_file(self, output, data):
            Logger.log(self.ndvi.shape)
            out_ds = gdal.GetDriverByName('GTiff').Create(output, self.ndvi.shape[1], self.ndvi.shape[0], 1, gdal.GDT_Byte)
            out_ds.SetGeoTransform(self.geo_info)
            out_ds.GetRasterBand(1).WriteArray(data)
            out_ds.FlushCache()

        def calculate_water_area(self):
            r_values = self.open_tiff(self.r_band_path)
            nir_values = self.open_tiff(self.nir_band_path)
            ndvi_area = self.find_water_area(r_values, nir_values, self.ndvi_threshold)
            self.write_to_file(self.output_file_path, self.ndvi)
            return self.output_file_path

        def add_to_project(self, result):
            layer = iface.addRasterLayer(result)
