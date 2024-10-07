immutable_var = (1, 'Один', False)
print (immutable_var)

#выдает ошибку, т.к. кортеж относится к неизменяемым типам данных
immutable_var[0] = 2024

mutable_list = [1, 'Один', False]
mutable_list[-1] = True
mutable_list[0] = 2024
print(mutable_list)