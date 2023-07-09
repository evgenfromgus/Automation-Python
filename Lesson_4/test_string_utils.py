from string_utils import StringUtils
import pytest
#utils = StringUtils() используется для создания экземпляра класса StringUtils,
#чтобы можно было вызывать его методы и проверять их результаты

#test_capitalize() проверяет, что метод capitilize() правильно делает первую букву заглавной
def test_capitalize():
    utils = StringUtils()
    assert utils.capitilize("") == ""
    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("hello world") == "Hello world"
@pytest.mark.xfail()
def test_capitilize_with_special_characters_input():
    utils = StringUtils()
    assert utils.capitilize("#$%^&*") == "#$%^&*"
def test_capitilize_with_unicode_characters_input():
    utils = StringUtils()
    assert utils.capitilize("Привет") == "Привет"
def test_capitilize_with_numbers_input():
    utils = StringUtils()
    assert utils.capitilize("12345") == "12345"

#test_trim() проверяет, что метод trim() удаляет пробелы в начале строки
def test_trim():
    utils = StringUtils()
    assert utils.trim("") == ""
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("  hello world  ") == "hello world  "
@pytest.mark.xfail()
def test_trim_with_unicode_characters_input():
    utils = StringUtils()
    assert utils.trim("Привет") == "Привет"
def test_trim_with_numbers_input():
    utils = StringUtils()
    assert utils.trim("12345") == "12345"

#test_to_list() проверяет, что метод to_list() правильно разделяет строку на список строк с заданным разделителем
def test_to_list():
    utils = StringUtils()
    assert utils.to_list("") == []
    assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert utils.to_list("1:2:3", ":") == ["1", "2", "3"]
@pytest.mark.xfail()
def test_to_list_with_empty_string_input():
    utils = StringUtils()
    assert utils.to_list("", "-") == []
def test_to_list_with_whitespace_input():
    utils = StringUtils()
    assert utils.to_list("     ", "-") == []
def test_to_list_with_special_characters_input():
    utils = StringUtils()
    assert utils.to_list("#$%^&*", "-") == ["#$%^&*"]
def test_to_list_with_unicode_characters_input():
    utils = StringUtils()
    assert utils.to_list("Привет", "-") == ["Привет"]
def test_to_list_with_numbers_input():
    utils = StringUtils()
    assert utils.to_list("12345", "-") == ["12345"]

#test_contains() проверяет, что метод contains() возвращает True, если строка содержит заданный символ, и False в противном случае
def test_contains():
    utils = StringUtils()
    assert utils.contains("SkyPro", "S") == True
    assert utils.contains("SkyPro", "U") == False
    assert utils.contains("Hello world", "o") == True
@pytest.mark.xfail()
def test_contains_with_empty_string_input():
    utils = StringUtils()
    assert utils.contains("", "e") == False
def test_contains_with_whitespace_input():
    utils = StringUtils()
    assert utils.contains("     ", "hello") == False
def test_contains_with_special_characters_input():
    utils = StringUtils()
    assert utils.contains("#$%^&*", "o") == False
def test_contains_with_unicode_characters_input():
    utils = StringUtils()
    assert utils.contains("Привет", "l") == False
def test_contains_with_numbers_input():
    utils = StringUtils()
    assert utils.contains("12345", "h") == False

#test_delete_symbol() проверяет, что метод delete_symbol() правильно удаляет все вхождения заданного символа из строки
def test_delete_symbol():
    utils = StringUtils()
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert utils.delete_symbol("Hello world", "o") == "Hell wrld"
@pytest.mark.xfail()
def test_delete_symbol_with_empty_string_input():
    utils = StringUtils()
    assert utils.delete_symbol("", "h") == ""
def test_delete_symbol_with_whitespace_input():
    utils = StringUtils()
    assert utils.delete_symbol("     ", "h") == "     "
def test_delete_symbol_with_special_characters_input():
    utils = StringUtils()
    assert utils.delete_symbol("#$%^&*", "h") == "#$%^&*"
def test_delete_symbol_with_unicode_characters_input():
    utils = StringUtils()
    assert utils.delete_symbol("Привет", "h") == "Привет"
def test_delete_symbol_with_numbers_input():
    utils = StringUtils()
    assert utils.delete_symbol("12345", "h") == "12345"

#test_starts_with() проверяет, что метод starts_with() возвращает True, если строка начинается с заданного символа, и False в противном случае
def test_starts_with():
    utils = StringUtils()
    assert utils.starts_with("SkyPro", "S") == True
    assert utils.starts_with("SkyPro", "P") == False
    assert utils.starts_with("Hello world", "H") == True
@pytest.mark.xfail()
def test_starts_with_with_empty_string_input():
    utils = StringUtils()
    assert utils.starts_with("", "H") == False
def test_starts_with_with_whitespace_input():
    utils = StringUtils()
    assert utils.starts_with("     ", "H") == False
def test_starts_with_with_special_characters_input():
    utils = StringUtils()
    assert utils.starts_with("#$%^&*", "H") == False
def test_starts_with_with_unicode_characters_input():
    utils = StringUtils()
    assert utils.starts_with("Привет", "H") == False
def test_starts_with_with_numbers_input():
    utils = StringUtils()
    assert utils.starts_with("12345", "H") == False

#test_end_with() проверяет, что метод end_with() возвращает True, если строка заканчивается заданным символом, и False в противном случае
def test_end_with():
    utils = StringUtils()
    assert utils.end_with("SkyPro", "o") == True
    assert utils.end_with("SkyPro", "y") == False
    assert utils.end_with("Hello world", "d") == True
@pytest.mark.xfail()
def test_end_with_with_empty_string_input():
    utils = StringUtils()
    assert utils.end_with("", "T") == False
def test_end_with_with_whitespace_input():
    utils = StringUtils()
    assert utils.end_with("     ", "T") == False
def test_end_with_with_special_characters_input():
    utils = StringUtils()
    assert utils.end_with("#$%^&*", "P") == False
def test_end_with_with_unicode_characters_input():
    utils = StringUtils()
    assert utils.end_with("Привет", "P") == False
def test_end_with_with_numbers_input():
    utils = StringUtils()
    assert utils.end_with("12345", "U") == False

#test_is_empty() проверяет, что метод is_empty() возвращает True, если строка пустая, и False в противном случае
def test_is_empty():
    utils = StringUtils()
    assert utils.is_empty("") == True
    assert utils.is_empty(" ") == True
    assert utils.is_empty("SkyPro") == False
@pytest.mark.xfail()
def test_is_empty_with_special_characters_input():
    utils = StringUtils()
    assert utils.is_empty("#$%^&*") == False
def test_is_empty_with_numbers_input():
    utils = StringUtils()
    assert utils.is_empty("12345") == False

#test_list_to_string() проверяет, что метод list_to_string() правильно преобразует список элементов в строку с заданным разделителем
def test_list_to_string():
    utils = StringUtils()
    assert utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
@pytest.mark.xfail()
def test_list_to_string_with_empty_list_input():
    utils = StringUtils()
    assert utils.list_to_string([], "-") == ""
def test_list_to_string_with_single_element_input():
    utils = StringUtils()
    assert utils.list_to_string(["hello"], "-") == "hello"
def test_list_to_string_with_whitespace_element_input():
    utils = StringUtils()
    assert utils.list_to_string(["     "], "-") == "     "
def test_list_to_string_with_special_characters_input():
    utils = StringUtils()
    assert utils.list_to_string(["#$%^&*"], "-") == "#$%^&*"
def test_list_to_string_with_unicode_characters_input():
    utils = StringUtils()
    assert utils.list_to_string(["Привет"], "-") == "Привет"
