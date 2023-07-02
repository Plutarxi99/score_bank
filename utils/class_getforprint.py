import datetime

import constant

import json


class GetForPrint:
    """Получение данных для их послудующего вывода"""

    def __init__(self, value_for_print):
        self.name = None
        self.amount = None
        self.to = None
        self.from_ = None
        self.description = None
        self.time = None
        self.value_for_print = value_for_print

    def get_true_file(self):
        """
        Читает файл с операциями operations.json и фильтрует его по constant.STATUS_STATE
        и записывает в файл score_bank.json последних value_for_print операций
        """
        with open(constant.FILE_JSON, 'r', encoding="UTF-8") as f:
            file = json.load(f)
            list_filter = []

            for x in range(-self.value_for_print, 0):
                if file[x]['state'] in constant.STATUS_STATE:
                    if len(list_filter) <= self.value_for_print:
                        list_filter.insert(len(list_filter), file[x])
            #file_1 = open('score_bank.json', 'w')
            #json.dump(list_filter, file_1)
        return list_filter[0:self.value_for_print]




