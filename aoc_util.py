import requests
import os

session = os.getenv('AOC_COOKIE')
def test():
    print("Okay")

def get_day(day_num):
    cache_path = f'input/{day_num}.input'
    if os.path.exists(cache_path):
        print(f"Using cached input for day {day_num}")
        with open(cache_path, 'r') as f:
            return f.read()
    print(f"Downloading input for day {day_num}")
    ses = requests.Session()
    ses.cookies.set("session", session)
    input = ses.get(f"https://adventofcode.com/2021/day/{day_num}/input").text
    with open(cache_path, 'w') as f:
        f.write(input)
    return input
