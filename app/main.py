from fastapi import FastAPI
from pydantic import BaseModel
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

# Libreria calcolo vettoriale (perché le immagini possono essere viste come tensori)
import numpy as np

# Librerie di aiuto per l'interfaccia OS
import zipfile
import os
import base64






app = FastAPI()

class QueryMapper(BaseModel):
    lambda_function : str
    query_string: str
    geojson: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/products/{querystring}")
def get_products(geojson: str, q: str = None):
    return {"geojson": geojson, "q": q}

# per lanciare il server
# uvicorn main:app --reload