import requests, json, pprint, re
from bs4 import BeautifulSoup as bs4

base_site = 'https://hub.arcgis.com/datasets?source=City%20of%20Washington%2C%20DC'
base_site = 'http://maps2.dcgis.dc.gov/dcgis/rest/services'
data_directory = '/DCGIS_DATA/'
#query structure is base_website + / path / to / dataset# / query?option1=1&option2=2
default_query = '/query?where=1%3D1&f=pjson'

results = requests.get(base_site+data_directory)
soup = bs4(results.content,'html.parser')
soupA = soup.find_all(re.compile(".href="))

with open('output.txt','w') as f:
    for item in soupA:
        f.write(str(item))
        f.write('\n')
