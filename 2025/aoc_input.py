import sys
import requests

YEAR            = 2025
COOKIE_FILE     = 'cookie.txt'
INPUT_DIR       = 'solns/'

def load_cookie():
    with open(COOKIE_FILE, 'r') as infile:
        cookie = infile.readline().rstrip()
    return cookie

def fetch_input(day):
    url     = f'https://adventofcode.com/{YEAR}/day/{day}/input'
    cookie  = load_cookie()

    print(f'fetching input for day {day}')
    response = requests.get(url, headers={'Cookie':cookie})

    with open(f'{INPUT_DIR}{day}.in', 'w') as outfile:
        text = response.text.rstrip()
        outfile.write(text)


if __name__ == '__main__':
    args    = sys.argv[1:]
    day     = int(args[0])

    fetch_input(day)
