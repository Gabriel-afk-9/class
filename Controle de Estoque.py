from datetime import datetime

# Exceções personalizadas
class InvalidStockValueError(Exception):
    pass

class InsufficientStockError(Exception):
    pass

class InvalidDateFormatError(Exception):
    pass

class Product:
    def __init__(self, name, quantity, expiry_date):
        self.name = name
        self.quantity = quantity
        self.expiry_date = expiry_date

    def add_stock(self, amount):
        if amount < 0:
            raise InvalidStockValueError("O valor do estoque não pode ser negativo.")
        self.quantity += amount
        print(f"{amount} unidades adicionadas ao estoque do produto '{self.name}'. Estoque atual: {self.quantity}")

    def remove_stock(self, amount):
        if amount > self.quantity:
            raise InsufficientStockError(f"Estoque insuficiente. Estoque atual: {self.quantity}")
        self.quantity -= amount
        print(f"{amount} unidades removidas do estoque do produto '{self.name}'. Estoque atual: {self.quantity}")

    def check_expiry(self, current_date):
        try:
            expiry = datetime.strptime(self.expiry_date, "%d/%m/%Y")
            current = datetime.strptime(current_date, "%d/%m/%Y")
        except ValueError:
            raise InvalidDateFormatError("A data deve estar no formato dd/mm/yyyy.")

        if current > expiry:
            print(f"O produto '{self.name}' está vencido. Data de validade: {self.expiry_date}")
            return True
        print(f"O produto '{self.name}' não está vencido. Data de validade: {self.expiry_date}")
        return False


if __name__ == "__main__":
    leite = Product("Leite", 10, "15/01/2025")

    leite.add_stock(5)

    try:
        leite.remove_stock(20)
    except InsufficientStockError as e:
        print(e)

    try:
        leite.check_expiry("01/01/2025")
        leite.check_expiry("20/01/2025")
    except InvalidDateFormatError as e:
        print(e)

    try:
        leite.check_expiry("01-01-2025")
    except InvalidDateFormatError as e:
        print(e)
