import argparse

parser = argparse.ArgumentParser(description='Get ticket info and NBA results.')

def print_nba_teams():
    print("Hello")

parser.add_argument('--team_name', type=str, required=True)

parser.add_argument('--results', type=str, required=False,
                    help='get the results for a team')
parser.add_argument('--prices', type=str, required=False,
                    help='get ticket prices for current team')
parser.add_argument('--are_playing', type=str, required=False,
                    help='is the team playing today')
parser.add_argument('--next_game', type=str, required=False,
                    help='next game')

args = parser.parse_args()
print('Hello,', args.team_name)


