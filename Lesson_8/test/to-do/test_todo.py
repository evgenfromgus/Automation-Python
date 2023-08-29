import pytest
from pages.TodoMain import WorkIssue


def test_todo():
    zadacha = WorkIssue()
    """Получение списка задач"""
    list = zadacha.get_list()
    """Проверяем, что код ответа 200"""
    assert list[1] == 200

    """Создание новой задачи"""
    new = zadacha.create_issue()
    """Проверяем, что при создании задачи вернется не пустой ID"""
    assert new is not None

    """Переименование задачи"""
    rename = zadacha.rename_issue()
    """Проверяем, что новое название задачи соответствует заданному"""
    assert rename[1] == "Задача из питона новая"

    """Получение информации по созданной задаче"""
    info = zadacha.get_issue_info()
    """Проверяем, что новое название задачи соответствует заданному"""
    assert info[0] == "Задача из питона новая"
    """Проверяем, что ID задачи соответствует ID задачи созданной впервые"""
    assert info[1] == new

    """Отметка задачи - выполнена"""
    satus_true = zadacha.done_issue()
    """Проверяем, что статус задачи - true"""
    assert satus_true == True

    """Снятие отметки задачи - выполнена"""
    satus_false = zadacha.un_done_issue()
    """Проверяем, что статус задачи - false"""
    assert satus_false == False

    """Удаление задачи"""
    deleting = zadacha.delete_issue()
    """Проверяем, что код ответа 204"""
    assert deleting == 204
