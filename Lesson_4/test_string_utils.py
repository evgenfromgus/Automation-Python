from string_utils import StringUtils
#utils = StringUtils() используется для создания экземпляра класса StringUtils,
#чтобы можно было вызывать его методы и проверять их результаты

#test_capitalize() проверяет, что метод capitilize() правильно делает первую букву заглавной
def test_capitalize():
    utils = StringUtils()
    assert utils.capitilize("") == ""
    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("hello world") == "Hello world"
#test_trim() проверяет, что метод trim() удаляет пробелы в начале строки
def test_trim():
    utils = StringUtils()
    assert utils.trim("") == ""
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("  hello world  ") == "hello world  "
#test_to_list() проверяет, что метод to_list() правильно разделяет строку на список строк с заданным разделителем
def test_to_list():
    utils = StringUtils()
    assert utils.to_list("") == []
    assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert utils.to_list("1:2:3", ":") == ["1", "2", "3"]
#test_contains() проверяет, что метод contains() возвращает True, если строка содержит заданный символ, и False в противном случае
def test_contains():
    utils = StringUtils()
    assert utils.contains("SkyPro", "S") == True
    assert utils.contains("SkyPro", "U") == False
    assert utils.contains("Hello world", "o") == True
#test_delete_symbol() проверяет, что метод delete_symbol() правильно удаляет все вхождения заданного символа из строки
def test_delete_symbol():
    utils = StringUtils()
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert utils.delete_symbol("Hello world", "o") == "Hell wrld"
#test_starts_with() проверяет, что метод starts_with() возвращает True, если строка начинается с заданного символа, и False в противном случае
def test_starts_with():
    utils = StringUtils()
    assert utils.starts_with("SkyPro", "S") == True
    assert utils.starts_with("SkyPro", "P") == False
    assert utils.starts_with("Hello world", "H") == True
#test_end_with() проверяет, что метод end_with() возвращает True, если строка заканчивается заданным символом, и False в противном случае
def test_end_with():
    utils = StringUtils()
    assert utils.end_with("SkyPro", "o") == True
    assert utils.end_with("SkyPro", "y") == False
    assert utils.end_with("Hello world", "d") == True
#test_is_empty() проверяет, что метод is_empty() возвращает True, если строка пустая, и False в противном случае
def test_is_empty():
    utils = StringUtils()
    assert utils.is_empty("") == True
    assert utils.is_empty(" ") == True
    assert utils.is_empty("SkyPro") == False
#test_list_to_string() проверяет, что метод list_to_string() правильно преобразует список элементов в строку с заданным разделителем
def test_list_to_string():
    utils = StringUtils()
    assert utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"