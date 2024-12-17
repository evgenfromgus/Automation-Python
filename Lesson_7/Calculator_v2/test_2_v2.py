from Lesson_7.Calculator_v2.Pages.CalcPage import CalcPage

def test_calculator(chrome_browser):
    delay = 45
    result = 15
    keys_press = '7+8='

    calc = CalcPage(chrome_browser)
    calc.open()
    calc.set_delay(delay)
    calc.input_text(keys_press)
    calc.wait_result(delay, result)

    assert calc.result_text() == str(result)
