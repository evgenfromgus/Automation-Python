from pages.Calcmainpage import CalcMain


def test_calculator_assert(chrome_browsers):
    calcmain = CalcMain(chrome_browsers)
    calcmain.insert_time()
    calcmain.clicking_buttons()
    calcmain.wait_button_gettext()

    assert "15" in calcmain.wait_button_gettext()
