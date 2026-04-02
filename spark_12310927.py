import os
import sys

def main():
    if os.getcwd() != os.path.dirname(os.path.abspath(__file__)):
        print("Please run this script from its own directory.")
        sys.exit(1)