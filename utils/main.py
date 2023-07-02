from utils.class_getforprint import GetForPrint
import value_on_print
import numbers


if __name__ == "__main__":
    # Просим пользователя ввести количество операции, которые надо вывести
    count_for_print = int(input("Сколько вывести последних операций"))
    # Делаем экземляр класса GetForPrint и работает со списком, который мы получаем
    file_1 = GetForPrint(count_for_print)
    list_for_value = file_1.get_true_file()
    print(value_on_print.value_on_print(list_for_value))


