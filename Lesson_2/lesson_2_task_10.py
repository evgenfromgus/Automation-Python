def bank(x, y):
    for i in range(1, y+1):
        count = x + (x/10)
        x = count
    print(count) #сли сдвинуть эту функцию вправо (под х), то будет выводиться сумма за каждый год

bank(150, 3)

