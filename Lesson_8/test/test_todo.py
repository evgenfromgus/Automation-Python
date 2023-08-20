import pytest
from pages.TodoMain import WorkIssue


def test_todo():
    zadacha = WorkIssue(WorkIssue)
    """Получение списка задач"""
    zadacha.get_list()
    """Создание новой задачи"""
    zadacha.create_issue()
    """Переименование  задачи"""
    zadacha.rename_issue()
    """Получение информации по созданной задаче"""
    zadacha.get_issue_info()
    """Отметка задачи - выполнена"""
    zadacha.done_issue()
    """Снятие отметки задачи - выполнена"""
    zadacha.un_done_issue()
    """Удаление задачи"""
    zadacha.delete_issue()
