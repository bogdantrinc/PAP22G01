import json

import requests


def time_getter(location):
    response = requests.get(f'http://worldtimeapi.org/api/timezone/{location}')
    print(f'Initial: {response}')
    time_str = response.text.abcd
    print(f'After process: {time_str}')
    return json.loads(time_str)


if __name__ == '__main__':
    print(time_getter('Europe'))
