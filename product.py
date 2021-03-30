class Invoice:
    """
    Object that contains data about a invoice, such as date, name of customer, and total price.
    """

    def __init__(self,date, name, total):
        self.date = date
        self.name = name
        self.total =total


class Product:
    """
    Creates a product which has a name and price
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price