from pages.Shopmain import ShopmainPage
from pages.Shopcontainer import ShopContainer


def test_shop(chrome_browsers):
    expected_total = "58.29"
    shopmain = ShopmainPage(chrome_browsers)
    shopmain.registration_fields()
    shopmain.buy_issue()
    shopmain.click_issue()
    shopmain.into_container()
    container = ShopContainer(chrome_browsers)
    container.checkout()
    container.info()
    container.price()

    assert expected_total in container.price()  # Проверяем, что итоговая сумма равна $58.29
    print("Итоговая сумма равна $58.29")  # Выводим сообщение в случае успешного выполнения
