immutable_var = (1, 2, "text", True)
print("Immutable tuple:", immutable_var)
# immutable_var[0]= 100 # Строка кода не работает корректно, потому что, immutable_var имеет тиип данных "tuple" и явлеется не изменяемым
mutable_list = [1, 2, "str", True]
mutable_list[3] = "string"
print("Mutable list;", mutable_list)
