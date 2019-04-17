class Product:
    id = 0

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.id = Product.set_number()

    @classmethod
    def set_number(cls):
        Product.id += 1
        return Product.id

    def get_id(self):
        return self.id

    def get_sum(self):
        self.total_sum = self.price * self.quantity
        return self.total_sum

    def __str__(self):
        return "Product id: {} name: {}  price: {} quantity: {}".format(self.id, self.name, self.price, self.quantity)

    def __repr__(self):
        return str(self)


class ShoppingCart:
    discount_rate = 0.1

    def __init__(self, basket=None):
        if basket is None:
            self.basket = {}
        else:
            self.basket = basket

    def add_product(self, product):
        self.basket[product.id] = product
        return self.basket

    def del_product(self, id):
        del (self.basket[id])

    def print_basket(self):
        total_sum = 0
        discount = 0
        for product_id in self.basket:
            sum_of_product = self.basket[product_id].get_sum()
            if self.basket[product_id].quantity > 5:
                discount += sum_of_product * ShoppingCart.discount_rate
            total_sum += sum_of_product
            print(self.basket[product_id])
        return "payment: {}, discount: {}, discounted payment: {}".format(total_sum, round(discount, 2),
                                                                                   (total_sum - discount))

if __name__ == "__main__":
    p1 = Product("luncheon meat", 2.00, 5)
    p2 = Product("apple", 3, 5)
    p3 = Product("frikadelle ", 4, 6)

    basket1 = ShoppingCart()
    basket1.add_product(p2)
    basket1.add_product(p3)
    basket1.add_product(p1)

    print(basket1.print_basket())
    print('----------------------------------------------')
    basket2 = ShoppingCart()
    basket2.add_product(p2)
    basket2.add_product(p3)
    p2.price=4
    basket2.add_product(p1)
    basket2.del_product(3)
    print(basket2.print_basket())