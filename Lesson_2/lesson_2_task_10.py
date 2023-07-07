def bank(x, y):
    for i in range(1, y+1):
        count = x + (x/10)
        x = count
    print(round(count, 4)) #сли сдвинуть эту функцию вправо (под х), то будет выводиться сумма за каждый год

bank(13265, 12)

