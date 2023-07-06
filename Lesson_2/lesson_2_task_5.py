month_number = int(input())
def month_to_season(month_number):
    for i in range(1, month_number+1):
        if (month_number in (12, 1, 2)): return "Зима"
        elif (month_number in (3, 4, 5)): return "Весна"
        elif (month_number in (6, 7, 8)): return "Лето"
        elif (month_number in (9, 10, 11)): return "Осень"
        else: return "Ты что, не знаешь сколько месяцев в году и их порядковый номер? Заново запусти код и попробуй не облажаться опять!"
print(month_to_season(month_number))
