import sys
import requests
import os

def main():
    args = sys.argv[1:]
    print("Taking arg...")
    for i, arg in enumerate(args):
        print(i,arg)
    print("Kraj")

if __name__ == '__main__':
    main()