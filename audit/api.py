import requests

class GitHubAPI:
    def __init__(self, token=None):
        self.base_url = "https://api.github.com"
        self.session = requests.Session()

        if token:
            self.session.headers.update({
                "Authorization": f"token {token}"
            })

    def _get(self, url, params=None):
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_followers(self, username):
        followers = []
        page = 1

        while True:
            url = f"{self.base_url}/users/{username}/followers"
            params = {"per_page": 100, "page": page}
            data = self._get(url, params=params)

            if not data:
                break

            followers.extend(data)
            page += 1

        return followers

    def get_user(self, username):
        url = f"{self.base_url}/users/{username}"
        return self._get(url)
