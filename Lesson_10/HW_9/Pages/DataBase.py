from sqlalchemy import create_engine, text
import allure

class DataBase:
    """Эта функция создает словарь query, где каждый ключ представляет тип запроса
    к базе данных (например, создание компании, удаление компании и т. д.), 
    а каждое значение - объект текстового запроса SQL, соответствующего этому типу 
    запроса. Таким образом, этот словарь содержит предварительно определенные SQL-запросы,
    которые будут использоваться для выполнения операций с базой данных."""
    query = {
        'create_company': text('insert into company (name, description) values (:name, :description)'),
        'max_company_id': text('select MAX(id) from company'),
        'delete_company': text('delete from company where id = :company_id'),
        'list_SELECT': text('select * from employee where company_id = :id'),
        'item_SELECT': text('select * from employee where company_id = :c_id and id = :e_id'),
        'maxID_SELECT': text('select MAX(id) from employee where company_id = :c_id'),
        'item_DELETE': text('delete from employee where id = :id_delete'),
        'item_UPDATE': text('update employee set first_name = :new_name where id = :employer_id'),
        'item_INSERT': text(
            'insert into employee(company_id, first_name, last_name, phone) values(:id, :name, :surname, :phone_num)')
    }

    """Инициализируем класс и двигатель БД"""

    def __init__(self, engine) -> None:
        self.db = create_engine(engine)
        
    @allure.step("Cоздаем компанию в БД")
    def create_company(self, company_name: str, description: str):
        try:
            with self.db.connect() as connection:
                result = connection.execute(self.query['create_company'],
                                            parameters=dict(name=company_name, description=description))
                connection.commit()
                return result
        except Exception as _ex:
            print("[INFO] Error - can't work with SQL", _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] DB connection closed")
                
    @allure.step("Удаляем компанию из БД")
    def delete(self, company_id: int):
        try:
            with self.db.connect() as connection:
                connection.execute(self.query['delete_company'], parameters=dict(company_id=company_id))
                connection.commit()
        except Exception as _ex:
            print("[INFO] Error - can't work with SQL", _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] DB connection closed")

    @allure.step("Получаем ID последней созданной компании")
    def last_company_id(self):
        try:
            with self.db.connect() as connection:
                result = connection.execute(self.query['max_company_id']).fetchall()[0][0]
                return result
        except Exception as _ex:
            print("[INFO] Error - can't work with SQL", _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] DB connection closed")

    @allure.step("Получаем список сотрудников из БД")
    def get_list_employer(self, company_id: int):
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

    @allure.step("Создаем сотрудника в БД")
    def create_employer(self, company_id: int, first_name: str, last_name: str, phone: str):
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

    @allure.step("Получаем ID сотрудника из БД")
    def get_employer_id(self, company_id: int):
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

    @allure.step("Изменяем информацию о сотруднике в БД")
    def update_employer_info(self, new_name: str, id: int):
        try:
            with self.db.connect() as connection:
                result = connection.execute(self.query['item_UPDATE'],
                                            parameters=dict(new_name=new_name, employer_id=id))
                connection.commit()
        except Exception as _ex:
            print("[INFO] Error - can't work with SQL", _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] DB connection closed")

    @allure.step("Удаляем сотрудника из БД")
    def delete_employer(self, id: int):
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

    """ Более компактный вариант записи, с выносом обработки в отдельную функцию execute_query.
    Эта функция выполняет запрос к базе данных, используя заданный ключ запроса и 
    параметры (если они указаны). Она устанавливает соединение с базой данных, 
    выполняет SQL-запрос, фиксирует изменения (если это требуется), и возвращает 
    результат выполнения запроса. В случае возникновения ошибки при работе с базой 
    данных, функция отлавливает исключение, выводит сообщение об ошибке и закрывает 
    соединение с базой данных. По завершении работы функция также закрывает соединение 
    с базой данных."""
    
    # def __init__(self, engine):
    #     self.db = create_engine(engine)

    # def execute_query(self, query_key, parameters=None):
    #     try:
    #         with self.db.connect() as connection:
    #             result = connection.execute(self.query[query_key], parameters)
    #             connection.commit()
    #             return result
    #     except Exception as _ex:
    #         print("[INFO] Error - can't work with SQL", _ex)
    #     finally:
    #         if connection:
    #             connection.close()
    #             print("[INFO] DB connection closed")

    # def create_company(self, company_name: str, description: str):
    #     return self.execute_query('create_company', {'name': company_name, 'description': description})

    # def delete(self, company_id: int):
    #     return self.execute_query('delete_company', {'company_id': company_id})

    # def last_company_id(self):
    #     result = self.execute_query('max_company_id')
    #     return result.fetchall()[0][0]

    # def get_list_employer(self, company_id: int):
    #     result = self.execute_query('list_SELECT', {'id': company_id})
    #     return result.fetchall()

    # def create_employer(self, company_id: int, first_name: str, last_name: str, phone: str):
    #     return self.execute_query('item_INSERT', {'id': company_id, 'name': first_name, 'surname': last_name, 'phone_num': phone})

    # def get_employer_id(self, company_id: int):
    #     result = self.execute_query('maxID_SELECT', {'c_id': company_id})
    #     return result.fetchall()[0][0]

    # def update_employer_info(self, new_name: str, id: int):
    #     return self.execute_query('item_UPDATE', {'new_name': new_name, 'employer_id': id})

    # def delete_employer(self, id: int):
    #     return self.execute_query('item_DELETE', {'id_delete': id})