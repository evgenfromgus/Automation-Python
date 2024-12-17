# year = 2024
# 1 вариант
year = int(input())  # можно и так сделать, чтобы проверять воодимое значение года
def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False
result = is_year_leap(year)
print(f'год {year}: {result}')

# # 2 вариант
def is_year_leap(year):
    return year % 4 == 0
    # return f'год {year} високосный?: {year % 4 == 0}'
print(is_year_leap(2024))
print(is_year_leap(2023))
print(is_year_leap(2022))