year = 2009
#year = int(input())  #можно и так сделать, чтобы проверять воодимое значение года
def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False
result = is_year_leap(year)
print(f'год {year}: {result}')
