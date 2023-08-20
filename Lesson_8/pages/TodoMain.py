import requests
from constants import Todo_list_URL


class WorkIssue:
    def __init__(self, result):
        self.result = None

    def get_list(self):
        resp_list = requests.get(Todo_list_URL)
        all_list = resp_list.json()
        return all_list

    def create_issue(self):
        params = {"title": "Задача из питона", "completed": 'false'}
        resp = requests.post(Todo_list_URL, json=params)
        id_issue = resp.json()['id']
        self.result = id_issue
        return self.result

    def rename_issue(self):
        id_str = str(self.result)
        params = {"title": "Задача из питона новая"}
        resp = requests.patch(Todo_list_URL + id_str, json=params)
        new_title = resp.json()['id']
        return new_title

    def get_issue_info(self):
        id_str = str(self.result)
        resp_info = requests.get(Todo_list_URL + id_str)
        info = resp_info.json()
        return info

    def done_issue(self):
        id_str = str(self.result)
        params = {"completed": 'true'}
        resp = requests.patch(Todo_list_URL + id_str, json=params)
        done_status = resp.json()['completed']
        return done_status

    def un_done_issue(self):
        id_str = str(self.result)
        params = {"completed": 'false'}
        resp = requests.patch(Todo_list_URL + id_str, json=params)
        un_done_status = resp.json()['completed']
        return un_done_status

    def delete_issue(self):
        id_str = str(self.result)
        resp = requests.delete(Todo_list_URL + id_str)
        return resp
