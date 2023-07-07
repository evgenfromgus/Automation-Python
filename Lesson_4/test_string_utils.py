from string_utils import StringUtils

def test_reverse_string():
    assert StringUtils.reverse_string("hello") == "olleh"
    assert StringUtils.reverse_string("world") == "dlrow"

def test_capitalize_string():
    assert StringUtils.capitalize_string("hello world") == "Hello World"
    assert StringUtils.capitalize_string("python is awesome") == "Python Is Awesome"

def test_remove_duplicates():
    assert StringUtils.remove_duplicates("hello") == "helo"
    assert StringUtils.remove_duplicates("hello world") == "helo wrd"

def test_count_characters():
    assert StringUtils.count_characters("hello") == 5
    assert StringUtils.count_characters("world") == 5