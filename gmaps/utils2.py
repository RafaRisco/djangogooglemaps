client_id = "django"
client_secret = "zStZGCvPt4ElxdccHpjcHH736dEFrrDOHuuFv5yzMU9Az6I2QbzHX1DQwbQv6DwD"
username = "rafaelrisco@socialmass.co"
password = "SEVilla2018("
app_id = 23258918

from pypodio2 import api

def item(nombre, lat, long, user):
    nombre = nombre
    lat = lat
    long = long
    user = user
    item = {
    	"fields":[
    		{"external_id":"titulo", "values":[{"value":nombre}]},
            {"external_id":"cantidad", "values":[{"value":lat}], "decimals": 16},
            {"external_id":"long", "values":[{"value":long}], "decimals": 16},
            {"external_id":"user", "values":[{"value":user}]}
    	]
    }
    return item

def djangoClient(nombre, lat, long, user):
    nombre = nombre
    lat = lat
    long = long
    user = user
    c = api.OAuthClient(
        client_id,
        client_secret,
        username,
        password,
    )
    c.Item.create(app_id, item(nombre, lat, long, user))
    return c
