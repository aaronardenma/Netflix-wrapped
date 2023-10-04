import requests
import json

### site: https://www.omdbapi.com/
# i = valid IMDb ID (ie. tt1285016)
# t = movie title to search for
# type = movie, series, episode
# y = year of release


def api(parameters):
    key = 'f23755f8'
    response = requests.get(f'http://www.omdbapi.com/?{parameters}&apikey={key}')
    response.raise_for_status
    
    return json.loads(response.text)

# print(api('t=oh+my+ghost&y=2015')['Title'])
# print(api('t=oh+my+ghost&y=2015')['Title'])
# print(api('t=oh+my+ghost&y=2015')['Title'])
test = 'The Office (U.S.): Season 5: Business Ethics (Episode 3)'
print(test.replace(" ", "+"))

def search_api(title):
    title = title.replace(" ", "+")
    netflix_title = (api(f't={title}')['Title'])
    return netflix_title

print(search_api("The Office (U.S.)"))