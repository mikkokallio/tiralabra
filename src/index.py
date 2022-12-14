import argparse
from app import App
from config import AI_PLAYERS


def main():
    '''Starts the app'''
    parser = argparse.ArgumentParser(description='Runs gomoku for two AI players',
                                     epilog=f'Players must be from the following list:\
                                         \n{list(AI_PLAYERS.keys())}')
    parser.add_argument('-a', '--alternate', action='store_true',
                        help='plays the game twice with players switching colors')
    parser.add_argument('-r', '--repeat', type=int, metavar='n', default=1,
                        help='repeats the game n times')
    parser.add_argument('-c', '--csv', action='store_true',
                        help='hides normal output and instead only prints game result as csv')
    parser.add_argument('-s', '--store', action='store_true',
                        help='saves information about played games')
    parser.add_argument('-v', '--visualize', action='store_true',
                        help='visualize board state with colors')
    parser.add_argument('player1', choices=AI_PLAYERS)
    parser.add_argument('player2', choices=AI_PLAYERS)
    args = parser.parse_args()
    games = args.repeat * 2 if args.alternate else args.repeat
    flipped = False
    for _ in range(games):
        players = [args.player2, args.player1] if flipped else [args.player1, args.player2]
        app = App(players, 60, args.csv, args.store, args.visualize)
        result = app.run()
        if args.csv:
            print(result)
        flipped = not flipped

if __name__ == '__main__':
    main()
    