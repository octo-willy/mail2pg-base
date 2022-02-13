#http requests 
import os
import requests

#retrieve xy from perceelnr
def perceelnr_to_xy(perceelnr):
    '''
    input (str): perceelnr in AMF00-K-6145 format
    return (str): WKT POINT(x,y)
    '''
    url = f"https://geodata.nationaalgeoregister.nl/locatieserver/v3/free?q={perceelnr}&fq=bron:DKK&rows=1"
    with requests.Session() as session:
        r = session.get(url)
        if r.status_code==200:
            data = r.json()
            row = data["response"]["docs"][0]
            if row.get("identificatie") == perceelnr:
                return row.get("centroide_rd")
 