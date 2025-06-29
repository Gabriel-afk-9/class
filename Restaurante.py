# Exceções personalizadas
class ItemAlreadyExistsError(Exception):
    pass

class ItemNotFoundError(Exception):
    pass

# Classe Item
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Classe Order
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        for existing_item in self.items:
            if existing_item.name == item.name:
                raise ItemAlreadyExistsError(f"O item '{item.name}' já está no pedido.")
        self.items.append(item)
        print(f"Item '{item.name}' adicionado ao pedido.")
    
    def remove_item(self, item_name):
        for existing_item in self.items:
            if existing_item.name == item_name:
                self.items.remove(existing_item)
                print(f"Item '{item_name}' removido do pedido.")
                return
        raise ItemNotFoundError(f"Item '{item_name}' não foi encontrado no pedido.")
    
    def show_order(self):
        if not self.items:
            print("O pedido está vazio.")
            return 0
        print("Itens no pedido:")
        total = 0
        for item in self.items:
            print(f"- {item.name}: R${item.price:.2f}")
            total += item.price
        print(f"Total parcial: R${total:.2f}")
        return total

# Classe Bill
class Bill:
    def __init__(self, order, service_fee=0.10):
        self.order = order
        self.service_fee = service_fee
    
    def calculate_total(self):
        subtotal = self.order.show_order() or 0
        total = subtotal + (subtotal * self.service_fee)
        return total

    def show_bill(self):
        subtotal = self.order.show_order() or 0
        service_fee_value = subtotal * self.service_fee
        total = self.calculate_total()
        print("=== Detalhamento da Conta ===")
        print(f"Subtotal: R${subtotal:.2f}")
        print(f"Taxa de serviço (10%): R${service_fee_value:.2f}")
        print(f"Total final: R${total:.2f}")

# Exemplo de uso
if __name__ == "__main__":
    pizza = Item("Pizza", 40.00)
    refrigerante = Item("Refrigerante", 8.00)
    sobremesa = Item("Sobremesa", 15.00)

    pedido = Order()
    pedido.add_item(pizza) 
    pedido.add_item(refrigerante)

    pedido.show_order()

    pedido.remove_item("Refrigerante")
    pedido.show_order()

    try:
        pedido.add_item(pizza)
    except ItemAlreadyExistsError as e:
        print(e)

    pedido.add_item(sobremesa)

    conta = Bill(pedido)
    conta.show_bill()