import argparse
import json
import accuallcorrection as accuallcorrection

def main():
    parser = argparse.ArgumentParser(prog='myprogram',description='Lintercleanter.', add_help=False) # add_help=False to remove the default help option
  
  
    parser.add_argument('-h', '--help', action='help', help='show this help message and exit')
    parser.add_argument('file', type=str, help='File to be corrected')
    parser.add_argument('-o', '--output', type=str, help='Output file')

    args = parser.parse_args() # parse the arguments
    