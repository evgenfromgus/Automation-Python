# 1 вариант
def bank(x, y):
    for i in range(1, y+1):
        count = x + (x/10)
        x = count
    print(round(count, 1))


bank(1000, 10)

# 2 вариант
percent = 0.1


def bank(deposit, year):
    for i in range(year):
        deposit = deposit + (deposit * percent)
    return print(round(deposit, 1))


bank(1000, 10)


