import requests
from constants import X_client_URL

path = '/employee/'


class Employer:
    def __init__(self, url=X_client_URL):
        self.url = url
        changed_emp_id = None

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
        return info_new_employer, id_new_emp, code

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
