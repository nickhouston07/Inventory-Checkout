class Cart:
    def __init__(self):
        self.__items = {}
        self.__total = 0

    def purchase_item(self, name, units, price):
        self.__items[name] = [price, units]
        self.__total += (price * units)

    def get_total(self):
        return self.__total

    def show_items(self):
        return self.__items

    def remove_item(self, name, cost):
        self.__total -= cost
        del self.__items[name]

    def clear(self):
        self.__items = {}
        self.__total = 0
