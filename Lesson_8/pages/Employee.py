import requests
from Lesson_8.constants import X_client_URL

path = '/employee/'


class Employer:
    def __init__(self, url=X_client_URL):
        self.url = url

    def get_list_employers(self, get_list_companies):
        company_id = get_list_companies
        company = {'company': company_id}
        resp_employers = requests.get(self.url + '/employee', params=company)
        list_employers = resp_employers.json()
        code = resp_employers.status_code
        print(list_employers, code)
        return list_employers, code, company

    def get_new_employer(self, add_new_employer):
        id_new_employer = str(add_new_employer[0])
        resp_get_new_employer = requests.get(self.url + path + id_new_employer)
        info_new_employer = resp_get_new_employer.json()
        id_new_emp = resp_get_new_employer.json()['id']
        code = resp_get_new_employer.status_code
        return info_new_employer, id_new_emp, code

    def change_new_employer(self, get_token, add_new_employer):
        token = get_token[0]
        id_employer = str(add_new_employer[0])
        headers = {'x-client-token': token}
        body_change_employer = {
            'lastName': 'Pupkin',
            'email': 'test2@mail.ru',
            'url': 'string',
            'phone': 'string',
            'isActive': 'true'
        }
        resp_change_employer = requests.patch(self.url + path + id_employer, headers=headers,
                                              json=body_change_employer)
        inform_changed_employer_id = resp_change_employer.json()['id']
        return inform_changed_employer_id, body_change_employer

    def get_new_employer_changed(self, add_new_employer):
        id_employer = str(add_new_employer[0])
        resp_new_employer_info_changed = requests.get(self.url + path + id_employer)
        info_new_employer_id = resp_new_employer_info_changed.json()['id']
        info_new_employer_lastName = resp_new_employer_info_changed.json()['lastName']
        info_new_employer_email = resp_new_employer_info_changed.json()['email']
        return info_new_employer_id, info_new_employer_lastName, info_new_employer_email
