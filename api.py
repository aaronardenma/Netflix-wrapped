import requests
import json

# i = valid IMDb ID (ie. tt1285016)
# t = movie title to search for
# type = movie, series, episode
# y = year of release


def api(parameters):
    key = 'f23755f8'
    response = requests.get(f'http://www.omdbapi.com/?{parameters}&apikey={key}')
    response.raise_for_status
    
    return json.loads(response.text)

print(api('t=oh+my+ghost&y=2015')['Type'])
