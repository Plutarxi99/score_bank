import datetime


class ValueOnPrint:
    """
    Класс для форматирования полученных значений
    """

    def __init__(self, list_formatted_on_date):

        self.index_in_list = None
        self.list_formatted_on_date = list_formatted_on_date

    def view_on_print(self, index_in_list):
        """
        Вывод в терминал в нужном ввиде
        :param index_in_list: получает индекс для списка
        :return:    14.10.2018 Перевод организации
                    Visa Platinum 7000 79** **** 6361 -> Счет **9638
                    82771.72 руб.
        """
        self.index_in_list = index_in_list
        list_for_value = self.list_formatted_on_date
        # Объявляем переменные и работаем со списком для получения нужного вывода
        data = self.formatted_time(list_for_value[index_in_list]["date"])

        description = list_for_value[index_in_list]["description"]

        card_number = (list_for_value[index_in_list].get('from', ''))
        from_ = self.formatted_card_number(card_number)

        score_number = list_for_value[index_in_list]["to"]
        to = self.formatted_score_number(score_number)

        amount = list_for_value[index_in_list]['operationAmount']["amount"]

        name = list_for_value[index_in_list]['operationAmount']['currency']["name"]

        return f'''
        {data} {description}
        {from_}->{to}
        {amount} {name}
        '''

    def formatted_time(self, data):
        """
        Форматирует нужный формат даты
        :param data: получает дату для форматирования
        :return: DD.ММ.YYYY
        """
        date = datetime.datetime.fromisoformat(data)
        date_f = date.strftime("%d.%m.%Y")
        return date_f

    def formatted_card_number(self, card_number):
        """
        функция для форматирования номера карты
        :param card_number: получает номер карты для его форматирования
        :return: XXXX XX** **** XXXX
        """
        number = []
        name_card = []

        for x in card_number:
            if x.isdigit():
                number.append(x)
            else:
                name_card.append(x)
        s = "".join(number)
        res = " ".join(s[i * 4: i * 4 + 4] for i in range(len(s) // 4))

        a = "*"
        b = a * int(len(res))
        cod = res[0:7] + b + res[-4:]
        return f'{"".join(name_card)} {cod}'

    def formatted_score_number(self, score_number):
        """
        функция для форматирования счета
        :param score_number: получает счет для его форматирования
        :return: **XXXX
        """
        number = []
        name_card = []

        for x in score_number:
            if x.isdigit():
                number.append(x)
            else:
                name_card.append(x)
        s = "".join(number)
        res = " ".join(s[i * 4: i * 4 + 4] for i in range(len(s) // 4))

        a = "*"
        b = a * 2
        cod = b + res[-4:]
        return f'{"".join(name_card)} {cod}'
