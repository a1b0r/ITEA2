class Market:

    _total_sales = 0

    def get_total_sales():
        return Market._total_sales

    _name = None
    _sales = 0

    def __init__(self, name, sales=0):
        self._name = name
        self._sales = sales
        Market._total_sales += self._sales

    def add_sale(self,sale):
        self._sales += sale
        Market._total_sales += self._sales

    def __str__(self):
        plural = ''
        if self._sales > 1:
            plural = 's'
        return '{} sold {} item{}.'.format(self._name, self._sales, plural)

    def print_sales(self):
        print(self.__str__())


atb1 = Market('ATB1', 1)
atb1.add_sale(1)
atb1.print_sales()

atb2 = Market('ATB2', 2)
atb2.add_sale(2)
atb2.print_sales()

atb3 = Market('ATB3', 3)
atb3.add_sale(3)
print(atb3)

atb4 = Market('ATB4', 4)
atb4.add_sale(4)
print(atb4)

print('Total sales: {}'.format(Market.get_total_sales()))
