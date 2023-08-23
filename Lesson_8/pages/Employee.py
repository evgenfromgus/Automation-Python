import requests
from constants import X_client_URL
from data.data import body_employer
from data.data import body_change_employer
from pages.Company import GetCompany
from pages.Autorization import InsertLogpass

path = '/employee/'


class Employer:
    def __init__(self, url):
        self.url = url

    def test_get_list_employers(self):
        company = {'company': GetCompany.test_get_list_companies(self)}
        resp_employers = requests.get(X_client_URL + '/employee', params=company)
        list_employers = resp_employers.json()
        code = resp_employers.status_code
        return list_employers, code, company

    def test_add_new_employer(self):
        headers = {'x-client-token': InsertLogpass.test_get_token(self)[0]}
        resp_add_new_employer = requests.post(X_client_URL + '/employee', headers=headers, json=body_employer)
        new_employer_id = resp_add_new_employer.json()['id']
        # self.id_employer_ = new_employer_id
        return new_employer_id, headers

    def test_get_new_employer(self):
        id_employer = str()
        resp_get_new_employer = requests.get(X_client_URL + path + id_employer)
        info_new_employer = resp_get_new_employer.json()
        print(info_new_employer)
        id_new_emp = resp_get_new_employer.json()['id']
        code = resp_get_new_employer.status_code
        return info_new_employer, id_new_emp, code

    def test_change_new_employer(self):
        id_employer = str(self.test_add_new_employer()[0])
        headers = {'x-client-token': self.token}
        resp_change_employer = requests.patch(X_client_URL + path + id_employer, headers=headers,
                                              json=body_change_employer)
        inform_changed_employer = resp_change_employer.json()
        return inform_changed_employer

    def test_get_new_employer_changed(self):
        id_employer = str(self.test_add_new_employer()[0])
        resp_new_employer_info_changed = requests.get(X_client_URL + path + id_employer)
        info_new_employer = resp_new_employer_info_changed.json()
        return info_new_employer
