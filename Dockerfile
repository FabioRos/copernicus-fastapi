FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# RUN apt install ffmpeg
RUN pip install geopandas
# geopandas = geo pandas
# pandas = libreria per dati tabellari (CSV)
# Geopandas -> evoluzione per dati geospaziali
# Geeopandas usato per processare il dato e mostrarlo in forma tabellare
RUN pip install folium
# Folium -  libreria per visualizzare delle mappe e creare hitmap interattive
RUN pip install sentinelsat
# Sentinelsat - libreria principale per interrogare scihub. Si interfaccia direttamente a scihub (che è il layer per recuperare i dati ufficiale di copernicus)
RUN pip install rasterio
RUN pip install opencv-python
RUN pip install imageio

COPY ./app /app
