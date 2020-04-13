import os
os.environ['RESTAPI_USE_ARCPY'] = 'FALSE'

# now import restapi
import json
import restapi

# download Allegheny County Covid19 data
url ="https://services1.arcgis.com/vdNDkVykv9vEWFX4/ArcGIS/rest/services/Spatial_Join_408/FeatureServer/0"
county_layer = restapi.FeatureLayer(url)

# export to shapefile
shp = "/Users/sihanmao/Documents/Projects/sihan_covid/covid19_pgh/map/county_covid19.shp"
county_layer.export_layer(shp, outSR=4326)

# convert to geojson for mapbox 
os.system("ogr2ogr -f 'GeoJSON' county_covid19.geojson county_covid19.shp")

# delete crs for mapbox upload

with open('/Users/sihanmao/Documents/Projects/sihan_covid/covid19_pgh/map/county_covid19.geojson') as f:
    data = json.load(f)

data["crs"] = ""

with open('/Users/sihanmao/Documents/Projects/sihan_covid/covid19_pgh/map/county_covid19.geojson', 'w') as f:
    json.dump(data, f)