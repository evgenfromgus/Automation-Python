import pytest
import requests
from constants import X_client_URL
from Lesson_8.data.data import body_employer


@pytest.fixture(scope="class")
def get_token(username='stella', password='sun-fairy'):
    log_pass = {'username': username, 'password': password}
    resp_token = requests.post(X_client_URL + '/auth/login', json=log_pass)
    token = resp_token.json()['userToken']
    code = resp_token.status_code
    yield token, code


@pytest.fixture(scope="class")
def get_list_companies():
    param_true = {'active': 'true'}
    resp_companies = requests.get(X_client_URL + '/company', params=param_true)
    last_companies_id = resp_companies.json()[-1]['id']
    yield last_companies_id


@pytest.fixture(scope="class")
def add_new_employer(get_token):
    token = get_token
    headers = {'x-client-token': token}
    resp_add_new_employer = requests.post(X_client_URL + '/employee', headers=headers, json=body_employer)
    id_new_employer = resp_add_new_employer.json()['id']
    yield id_new_employer, headers
