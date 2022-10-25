import pprint
import requests
from matplotlib import pyplot as plt
from datetime import datetime

# here we are formatting the PrettyPrinter. Try using different indents!
pp = pprint.PrettyPrinter(indent=4)

API_URL = 'https://goweather.herokuapp.com/weather/'
city = 'miami' # feel free to enter your own city here!
r = requests.get(API_URL + city)
response = r.json()

pp.pprint(response)


