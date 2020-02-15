from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt

# Librerie specifiche per lavorare con dati immagine
import rasterio as rio
# rasterio - libreria che ci permette di leggere le immagini di copernicus
# arrivano in formato jpeg2000 - che è un formato malvagio per comprimere immagini gigantesche

# in sentinel2 aarivano o jpeg2000 o netcdf ma su pangeo.io troviamo tutto
import rasterio.mask
from rasterio.plot import show
import matplotlib.pyplot as plt
import imageio
import cv2

# Libreria calcolo vettoriale (perché le immagini possono essere viste come tensori)
import numpy as np

# Librerie di aiuto per l'interfaccia OS
import zipfile
import os
import base64
from IPython.display import HTML