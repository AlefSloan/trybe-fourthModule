# Data Clumps

class CardInfo:
    def __init__(
        self,
        name,
        number,
        month,
        year,
        security_code,
    ):
        self.name = name
        self.number = number
        self.month = month
        self.year = year
        self.security_code = security_code


class Order:
    def __init__(
        self,
        items,
        card_info,
    ):
        self.items = items
        self.card_info = card_info
