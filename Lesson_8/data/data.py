from pages.Company import GetCompany

ide = GetCompany(GetCompany)
company_id = ide.test_get_list_companies()

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

body_change_employer = {
    'lastName': 'Pupkin',
    'email': 'test2@mail.ru',
    'url': 'string',
    'phone': 'string',
    'isActive': 'true'
}
