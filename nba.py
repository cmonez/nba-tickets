import argparse

parser = argparse.ArgumentParser(description='Get ticket info and NBA results.')

parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--results', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
parser.add_argument('--prices', action='store_const',
                    const=sum, default=max,
                    help='get price for current team')
parser.add_argument('--are_playing', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))