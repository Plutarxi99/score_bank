import json

FILE_JSON = "/home/egor/PycharmProjects/coursev/c_bank/operations.json"
STATUS_STATE = "EXECUTED"


class GetForPrint:
    """
    Получение данных для их послудующего вывода
    """

    def __init__(self, value_for_print):
        self.value_for_print = value_for_print

    def get_true_file(self):
        """
        Читает файл с операциями operations.json и фильтрует его по constant.STATUS_STATE
        и возвращает список отфильтрованный по дате
        :return: list formatted_on_date
        """
        with open(FILE_JSON, 'r', encoding="UTF-8") as f:
            file = json.load(f)
            list_filter = []

            # Цикл для фльтрования по 'state' == EXECUTED
            for x in range(len(file)):
                if file[x].get('state') == STATUS_STATE:
                    list_filter.append(file[x])

            # Переворачиваем список и делаем срез, того количества, которое надо вывести value_for_print
            list_filter.reverse()
            slice_list = list_filter[-len(list_filter):(-len(list_filter) + self.value_for_print)]

            # форматируем список по дате от новых к старым
            formatted_on_date = sorted(slice_list, key=lambda d: d['date'], reverse=True)

        return formatted_on_date
