import requests
from bs4 import BeautifulSoup

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
gsw_url = "https://www.basketball-reference.com/teams/GSW/2022_games.html"

req = requests.get(gsw_url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

table = soup.find("tbody")

print(table.prettify())