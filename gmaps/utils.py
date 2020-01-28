import requests

GMAPS_ENDPOINT = "https://maps.googleapis.com/maps/api/distancematrix/json?"
PODIO_API_KEY = "zStZGCvPt4ElxdccHpjcHH736dEFrrDOHuuFv5yzMU9Az6I2QbzHX1DQwbQv6DwD"


def distance(origen, destino):
    origen = "{},{}".format(origen.lat, origen.long)
    destino = "{},{}".format(destino.lat, destino.long)
    key = "AIzaSyARqS0p-B803819uh-0flhdum-cmIzWKNQ"
    metric = "metric"
    params = {'origins': origen, 'destinations': destino, 'key': key, 'units': metric}
    r = requests.get(GMAPS_ENDPOINT, params=params)
    respuesta = r.json()
    return respuesta.get('rows')[0]['elements'][0]['distance']['value']
