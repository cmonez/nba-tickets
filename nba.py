import argparse
from pnba import get_next_game, get_results

parser = argparse.ArgumentParser(description='Get ticket info and NBA results.')

def print_nba_teams():
    teams_string = 'team_abbreviation | name\n'
    teams = {
    'ATL':	'Atlanta Hawks',
    'BKN':	'Brooklyn Nets',
    'BOS':	'Boston Celtics',
    'CHA':	'Charlotte Hornets',
    'CHI':	'Chicago Bulls',
    'CLE':	'Cleveland Cavaliers',
    'DAL':	'Dallas Mavericks',
    'DEN':	'Denver Nuggets',
    'DET':	'Detroit Pistons',
    'GSW':	'Golden State Warriors',
    'HOU':	'Houston Rockets',
    'IND':	'Indiana Pacers',
    'LAC':	'Los Angeles Clippers',
    'LAL':	'Los Angeles Lakers',
    'MEM':	'Memphis Grizzlies',
    'MIA':	'Miami Heat',
    'MIL':	'Milwaukee Bucks',
    'MIN':	'Minnesota Timberwolves',
    'NOP':	'New Orleans, Pelicans',
    'NYK':	'New York, Knicks',
    'OKC':	'Oklahoma City, Thunder',
    'ORL':	'Orlando Magic',
    'PHI':	'Philadelphia 76ers',
    'PHX':	'Phoenix Suns',
    'POR':	'Portland Trail Blazers',
    'SAC':	'Sacramento Kings',
    'SAS':	'San Antonio Spurs',
    'TOR':	'Toronto Raptors',
    'UTA':	'Utah Jazz',
    'WAS':	'Washington Wizards'
    }
    for key, value in teams.items():
        teams_string += f"{key}  | {value}\n"
    print(teams_string)


parser.add_argument('--team_name', type=str,
                    help='specify a team name (team abbreviation)')

parser.add_argument('--r', '--results', required=False, action="store_true", dest="results",
                    help='get the results for a team')

parser.add_argument('--ng', '--next_game', required=False, action="store_true", dest="ng",
                    help='next game')

parser.add_argument('--prices', type=str, required=False,
                    help='get ticket prices for current team')

parser.add_argument('--playing_today', type=str, required=False,
                    help='is the team playing today')

parser.add_argument('-ls', '--list_teams', required=False, action="store_true", dest="list_teams",
                    help='list team abbreviations')

args = parser.parse_args()
team = args.team_name.upper()

if args.list_teams == True:
    print_nba_teams()

if args.results == True:
    if team == "BKN":
     team = "BRK"
    if team == "CHA":
        team = "CHO"
    if team == "PHX":
        team = "PHO"
    get_results(team)

if args.ng == True:
    get_next_game(team)


