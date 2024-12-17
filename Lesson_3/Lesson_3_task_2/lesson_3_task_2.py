from smartpfone import Smartpfone

catalog = []
# Создаем пять разных экземпляров класса Smartphone с разными марками,моделями и абонентскими номерами.
phone1 = Smartpfone("Samsung", "Galaxy S21", "+79123456789")
phone2 = Smartpfone("Apple", "iPhone 12", "+79098765432")
phone3 = Smartpfone("Xiaomi", "Mi 11", "+79876543210")
phone4 = Smartpfone("Google", "Pixel 5", "+79765432109")
phone5 = Smartpfone("OnePlus", "9 Pro", "+79654321098")
# Затем каждый экземпляр добавляется в список catalog.
catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
    
    
# сокращенный вариант записи

catalog = []

phones_data = [
    ("Samsung", "Galaxy S21", "+79123456789"),
    ("Apple", "iPhone 12", "+79098765432"),
    ("Xiaomi", "Mi 11", "+79876543210"),
    ("Google", "Pixel 5", "+79765432109"),
    ("OnePlus", "9 Pro", "+79654321098")
]

catalog = [Smartpfone(brand, model, phone_number) for (brand, model, phone_number) in phones_data]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
