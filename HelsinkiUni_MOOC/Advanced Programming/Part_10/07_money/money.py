# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        amount = self.__euros + (self.__cents * 0.01)
        return f"{amount:.2f} eur"
    

    def __eq__(self, another):
        return self.__euros == another.__euros and self.__cents == another.__cents
    

    def __lt__(self, another):
        amount = self.__euros + (self.__cents * 0.01)
        other_amount = another.__euros + (another.__cents * 0.01)

        return amount < other_amount
    

    def __gt__(self, another):
        amount = self.__euros + (self.__cents * 0.01)
        other_amount = another.__euros + (another.__cents * 0.01)

        return amount > other_amount
    

    def __ne__(self, another):
        amount = self.__euros + (self.__cents * 0.01)
        other_amount = another.__euros + (another.__cents * 0.01)

        return amount != other_amount
    
    
    def __add__(self, another):
        amount = self.__euros + (self.__cents * 0.01)
        other_amount = another.__euros + (another.__cents * 0.01)

        total  = amount + other_amount

        if total < 0:
            raise ValueError('a negative result is not allowed')

        else:
            cents = total % 1
            eur = total - cents
            cents_convert = cents * 100

            return Money(eur, cents_convert)


    def __sub__(self, another):
        amount = self.__euros + (self.__cents * 0.01)
        other_amount = another.__euros + (another.__cents * 0.01)

        subtracted  = amount - other_amount

        if subtracted < 0:
            raise ValueError('a negative result is not allowed')
        
        else:

            cents = subtracted % 1
            eur = subtracted - cents
            cents_convert = cents * 100

            return Money(eur, cents_convert)
        

if __name__ == '__main__':
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    print(e1)
    e1.__euros = 1000
    print(e1)