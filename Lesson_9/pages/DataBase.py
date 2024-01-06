from constants import db
from sqlalchemy import create_engine, text


class DataBase:
    query = {
        'list_SELECT': text('select * from employee where company_id = :id'),
        'item_SELECT': text('select * from employee where company_id = :c_id and id = :e_id'),
        'maxID_SELECT': text('select MAX(id) from employee where company_id = :c_id'),
        'item_DELETE': text('delete from employee where id = :id_delete'),
        'item_INSERT': text(
            'insert into employee(company_id, first_name, last_name, phone) values(:id, :name, :surname, :phone_num)')
    }

    """ Инициализируем класс и двигатель БД"""

    def __init__(self, engine) -> None:
        self.db = create_engine(engine)

    """ Получаем список сотрудников из БД"""

    def db_get_list_employee(self, company_id):
        try:
            with self.db.connect() as connection:
                result = connection.execute(self.query['list_SELECT'], parameters=dict(id=company_id)).fetchall()
                return result
        except Exception as _ex:
            print("[INFO] Error - can't work with SQL", _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] DB connection closed")

    """ Создаем сотрудника в БД"""

    def db_create_employee(self, company_id, first_name, last_name, phone):
        try:
            with self.db.connect() as connection:
                result = connection.execute(self.query['item_INSERT'],
                                            parameters=dict(id=company_id, name=first_name, surname=last_name,
                                                            phone_num=phone))
                connection.commit()
                return result
        except Exception as _ex:
            print("[INFO] Error - can't work with SQL", _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] DB connection closed")

    """ Получаем ID сотрудника в из БД"""

    def db_get_employee_id(self, company_id):
        try:
            with self.db.connect() as connection:
                result = connection.execute(self.query['maxID_SELECT'], parameters=dict(c_id=company_id)).fetchall()[0][
                    0]
                return result
        except Exception as _ex:
            print("[INFO] Error - can't work with SQL", _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] DB connection closed")

    """ Удаляем сотрудника из БД"""

    def db_delete_employee(self, id):
        try:
            with self.db.connect() as connection:
                result = connection.execute(self.query['item_DELETE'], parameters=dict(id_delete=id))
                connection.commit()
                return result
        except Exception as _ex:
            print("[INFO] Error - can't work with SQL", _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] DB connection closed")

            # from constants import db_connection_string
# import psycopg2
#
#
# # from faker import Faker
#
#
# class DataBase:
#     def __init__(self):
#         pass
#
#     def test_db_creating_company(self):
#         global connection
#         try:
#             connection = psycopg2.connect(db_connection_string)
#             connection.autocommit = True  # Нужно чтобы в БД автоматом записывались изменения
#             # Создание данных в БД
#             with connection.cursor() as cursor:
#                 name = "python_db"
#                 description = "for_my_future"
#                 # Записываем данные
#                 insert_query = cursor.execute(
#                     f"INSERT INTO company (name, description) VALUES ('{name}', '{description}')")
#         except Exception as _ex:
#             print("[INFO] Error - can't work with SQL", _ex)
#         finally:
#             if connection:
#                 connection.close()
#                 print("[INFO] DB connection closed")
#
#     def test_db_get_id_company(self):
#         global connection
#         try:
#             connection = psycopg2.connect(db_connection_string)
#             connection.autocommit = True  # Нужно чтобы в БД автоматом записывались изменения
#             # Получение информации из БД
#             with connection.cursor() as cursor:
#                 select_all_rows = cursor.execute(
#                     "SELECT id, name, description FROM company ORDER BY create_timestamp DESC")  # Необходима сортировка по созданному времени,ибо в БД так
#                 eject_rows = cursor.fetchall()  # Этот метод извлекает все строки
#                 rows = eject_rows[0]  # Забираем последнюю добавленную по времени строчку
#                 id_company = rows[0]  # Забираем последнюю добавленную по времени строчку
#                 return id_company
#         except Exception as _ex:
#             print("[INFO] Error - can't work with SQL", _ex)
#         finally:
#             if connection:
#                 connection.close()
#                 print("[INFO] DB connection closed")
#
#     def test_db_creating_employer(self):
#         id_comp = self.test_db_get_id_company()
#         global connection
#         try:
#             connection = psycopg2.connect(db_connection_string)
#             connection.autocommit = True  # Нужно чтобы в БД автоматом записывались изменения
#             # Создание данных в БД
#             with connection.cursor() as cursor:
#                 # Записываем данные
#                 insert_query = cursor.execute(
#                     "INSERT INTO employee (first_name, last_name, middle_name, company_id, email, avatar_url, phone, birthdate, is_active) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
#                     (
#                         'Ivan!', 'Petrov', 'string', id_comp, 'test@mail.ru', 'string', 'string',
#                         '2023-08-14T11:02:45.622Z',
#                         'true'))
#         except Exception as _ex:
#             print("[INFO] Error - can't work with SQL", _ex)
#         finally:
#             if connection:
#                 connection.close()
#                 print("[INFO] DB connection closed")

#
#

#
#
# def test_db_get_info():
#     global connection
#     try:
#         connection = psycopg2.connect(db_connection_string)
#         connection.autocommit = True  # Нужно чтобы в БД автоматом записывались изменения
#         # Получение информации из БД
#         with connection.cursor() as cursor:
#             select_all_rows = cursor.execute("SELECT id, name, description FROM company ORDER BY create_timestamp DESC")
#             eject_rows = cursor.fetchall()  # Этот метод извлекает все строки
#             rows = eject_rows[0]  # Забираем последнюю добавленную по времени строчку
#             id_value = rows[0]
#             # assert id_value == 2544
#             print(id_value)
#             # for row in rows:
#             #     print(row)
#             # print("#" * 20)
#     except Exception as _ex:
#         print("[INFO] Error - can't work with SQL", _ex)
#     finally:
#         if connection:
#             connection.close()
#             print("[INFO] DB connection closed")
#
#
# # Обновление данных
# with connection.cursor() as cursor:
#     update_query = "UPDATE company SET description = 'test2' WHERE name = 'QA'"
#     cursor.execute(update_query)
#
# # Удаление данных
# with connection.cursor() as cursor:
#     delete_query = "DELETE FROM company WHERE id = 2537"
#     cursor.execute(delete_query)
#
#     # Получение информации из БД
#     with connection.cursor() as cursor:
#         select_all_rows = cursor.execute("SELECT id, name, description FROM company ORDER BY create_timestamp DESC")
#         # cursor.execute(select_all_rows)
#         rows = cursor.fetchall()  # Этот метод извлекает все строки
#         a = rows[0]
#         assert a[3] == "Berry PLC"
#         print(a)
#         # for row in rows:
#         #     print(row)
#         # print("#" * 20)

#
#
