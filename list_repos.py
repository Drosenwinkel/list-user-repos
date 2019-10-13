import requests
import fire

def get_repos(user):
    URL = 'https://api.github.com/users/{}/repos'.format(user)
    r = requests.get(URL)

    data=r.json()

    for project in data:
        print(project["name"])

if __name__ == '__main__':
    fire.Fire(get_repos)