import requests
from constants import X_client_URL
from DataBase import DataBase

path = '/employee/'


class Employer:
    def __init__(self, url=X_client_URL):
        self.url = url
        changed_emp_id = None

    def get_token(username='stella', password='sun-fairy'):
        log_pass = {'username': username, 'password': password}
        resp_token = requests.post(X_client_URL + '/auth/login', json=log_pass)
        token = resp_token.json()['userToken']
        code = resp_token.status_code
        return token, code

    def get_list_companies():
        param_true = {'active': 'true'}
        resp_companies = requests.get(X_client_URL + '/company', params=param_true)
        # last_companies_id = resp_companies.json()[-1]['id']
        last_companies_name = resp_companies.json()[-1]['name']
        return last_companies_name

    def add_new_employer(get_token, get_list_companies):
        company_id = get_list_companies
        token = str(get_token[0])
        headers = {'x-client-token': token}
        body_employer = {
            'id': 0,
            'firstName': 'Ivan',
            'lastName': 'Petrov',
            'middleName': 'string',
            'companyId': company_id,
            'email': 'test@mail.ru',
            'url': 'string',
            'phone': 'string',
            'birthdate': '2023-08-14T11:02:45.622Z',
            'isActive': 'true'
        }
        resp_add_new_employer = requests.post(X_client_URL + '/employee', headers=headers, json=body_employer)
        id_new_employer = resp_add_new_employer.json()['id']
        return id_new_employer, headers

    def get_list_employers(self, company_id):
        company = {'company': company_id}
        resp_employers = requests.get(self.url + '/employee', params=company)
        list_employers = resp_employers.json()
        code = resp_employers.status_code
        return list_employers, code, company

    def get_new_employer(self, id_new_employer):
        resp_get_new_employer = requests.get(self.url + path + str(id_new_employer))
        info_new_employer = resp_get_new_employer.json()
        id_new_emp = resp_get_new_employer.json()['id']
        code = resp_get_new_employer.status_code
        new_employer_firstname = info_new_employer.json()['first_name']
        return info_new_employer, id_new_emp, code, new_employer_firstname

    def change_new_employer(self, id_new_employer, token):
        headers = {'x-client-token': token}
        body_change_employer = {
            'lastName': 'Pupkin',
            'email': 'test2@mail.ru',
            'url': 'string',
            'phone': 'string',
            'isActive': 'true'
        }
        resp_change_employer = requests.patch(self.url + path + str(id_new_employer), headers=headers,
                                              json=body_change_employer)
        inform_changed_employer_id = resp_change_employer.json()['id']
        global changed_emp_id
        changed_emp_id = inform_changed_employer_id
        return inform_changed_employer_id, body_change_employer

    def get_new_employer_changed(self):
        resp_new_employer_info_changed = requests.get(self.url + path + str(changed_emp_id))
        info_new_employer_id = resp_new_employer_info_changed.json()['id']
        info_new_employer_lastName = resp_new_employer_info_changed.json()['lastName']
        info_new_employer_email = resp_new_employer_info_changed.json()['email']
        return info_new_employer_id, info_new_employer_lastName, info_new_employer_email
