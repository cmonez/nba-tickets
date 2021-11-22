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
rows = table.findChildren("tr")

def get_team_name(node):
  title = node.find("div", id="meta")
  name = title.find(attrs={"itemprop" : "name"})
  spans = name.find_all("span")
  return spans[1].text

def get_opposing_team_name(node):
  opposing_team_name = node.find(attrs={"data-stat" : "opp_name"})
  return opposing_team_name.text

def get_home_team_score(node):
  opposing_team_score = node.find(attrs={"data-stat" : "pts"})
  return opposing_team_score.text

def get_opposing_team_score(node):
  opposing_team_score = node.find(attrs={"data-stat" : "opp_pts"})
  return opposing_team_score.text

def get_result(node):
  game_result = node.find(attrs={"data-stat" : "game_result"}).text
  if(game_result == 'W'):
      return 'WIN'
  else:
    return 'LOSS'

def declare_win_statement(soup, node):
  home_team_name = get_team_name(soup)
  home_team_score = get_home_team_score(node)
  opposing_team = get_opposing_team_name(node)
  opposing_score = get_opposing_team_score(node)
  result = get_result(node)
  text = f"{home_team_name}: {home_team_score} - {opposing_team}: {opposing_score} -  {result}"
  print(text)

declare_win_statement(soup, rows[0])

for row in rows:
  if row.has_attr("class"):
    continue
  else:
    declare_win_statement(soup, row)