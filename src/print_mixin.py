class PrintMixin:
    def __init__(self):
        print(self.__repr__())

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', '{self.price}', '{self.quantity}')"
        #Product('Продукт1', 'Описание продукта', 1200, 10)