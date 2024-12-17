# 1 вариант
var_1 = 37
var_2 = 99
var_1, var_2 = var_2, var_1
print('var_1 =', var_1, 'var_2 =', var_2)

# 2 вариант
var_1 = 37
var_2 = 99

# Меняем значения местами с помощью временной переменной
temp = var_1
var_1 = var_2
var_2 = temp

# Выводим обновленные значения
print('var_1 =', var_1, 'var_2 =', var_2)
