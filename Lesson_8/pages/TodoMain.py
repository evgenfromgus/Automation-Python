import requests
from constants import Todo_list_URL


class WorkIssue:
    def __init__(self, url=Todo_list_URL):
        self.url = url
        self.result = None

    def get_list(self):
        resp_list = requests.get(self.url)
        all_list = resp_list.json()
        code = resp_list.status_code
        return all_list, code

    def create_issue(self):
        params = {"title": "Задача из питона", "completed": 'false'}
        resp = requests.post(self.url, json=params)
        id_issue = resp.json()['id']
        self.result = id_issue
        return self.result

    def rename_issue(self):
        id_str = str(self.result)
        params = {"title": "Задача из питона новая"}
        resp = requests.patch(self.url + id_str, json=params)
        new_id = resp.json()['id']
        title = resp.json()['title']
        return new_id, title

    def get_issue_info(self):
        id_str = str(self.result)
        resp_info = requests.get(self.url + id_str)
        title = resp_info.json()['title']
        issue_id = resp_info.json()['id']
        return title, issue_id

    def done_issue(self):
        id_str = str(self.result)
        params = {"completed": 'true'}
        resp = requests.patch(self.url + id_str, json=params)
        done_status = resp.json()['completed']
        return done_status

    def un_done_issue(self):
        id_str = str(self.result)
        params = {"completed": 'false'}
        resp = requests.patch(self.url + id_str, json=params)
        un_done_status = resp.json()['completed']
        return un_done_status

    def delete_issue(self):
        id_str = str(self.result)
        resp = requests.delete(self.url + id_str)
        code = resp.status_code
        return code
