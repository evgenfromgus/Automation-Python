import requests
from constants import X_client_URL


class InsertLogpass:
    def __init__(self, url):
        self.url = url

    def test_get_token(self, username='stella', password='sun-fairy'):
        log_pass = {'username': username, 'password': password}
        resp_token = requests.post(X_client_URL + '/auth/login', json=log_pass)
        token = resp_token.json()['userToken']
        code = resp_token.status_code
        # print(code)
        return token, code
