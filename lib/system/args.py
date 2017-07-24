import argparse

__all__ = ['Args']

parser = argparse.ArgumentParser(description='SweetSixteenScheduler',
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-v', '--verbose', action='count', default=0,
                    help="Specify the level (number of -v counts)\n"
                         "0 = WARNING or above for application& libs\n"
                         "1 = INFO for application, WARNING for libs\n"
                         "2 = DEBUG for application, WARNING for libs\n"
                         "3 = DEBUG for application, INFO for libs\n"
                         "4 = DEBUG for application& libs")

parser.add_argument('-c', '--color',
                    action='store',
                    choices=['auto', 'always', 'never'],
                    default='auto',
                    help="Control the use of colors in the Log-Output")

parser.add_argument('-t', '--timestamp', action='store_true',
                    help="Enable timestamps in the Log-Output")

parser.add_argument('-i', '--ini-file', action='store',
                    help="Load a custom config.ini-File")


Args = parser.parse_args()
