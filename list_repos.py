import requests


if __name__ == '__main__':
    URL = 'https://api.github.com/users/drosenwinkel/repos'
    r = requests.get(URL)

    data=r.json()

    for project in data:
        print(project["name"])