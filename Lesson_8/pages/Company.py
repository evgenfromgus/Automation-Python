import requests
from constants import X_client_URL


class GetCompany:
    def __init__(self, url):
        self.url = url

    def test_get_list_companies(self):
        param_true = {'active': 'true'}
        resp_companies = requests.get(X_client_URL + '/company', params=param_true)
        last_companie_id = resp_companies.json()[-1]['id']
        return last_companie_id
