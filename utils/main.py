import class_valueonprint
import class_getforprint

if __name__ == "__main__":
    number_of_operations = int(input("Какое количество операций Вы хотите вывести?"))

    # Делаем экзмеляр class GetForPrint для получения списка
    list = class_getforprint.GetForPrint(number_of_operations)
    l = list.get_true_file()

    # Создаем цикл для вывода операций
    for x in range(number_of_operations):
        print(class_valueonprint.ValueOnPrint(l).view_on_print(x))

