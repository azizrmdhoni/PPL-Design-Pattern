class Product:
    def __init__(self, product_id, name, price):
        self.id = product_id
        self.name = name
        self.price = price


class ProductRepository:
    def __init__(self):
        self.products = []

    def find_all(self):
        return self.products

    def find_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def save(self, product):
        self.products.append(product)

    def delete(self, product_id):
        self.products = [
            product for product in self.products
            if product.id != product_id
        ]


class ProductService:
    def __init__(self, repository):
        self.repository = repository

    def add_product(self, product):
        self.repository.save(product)

    def show_products(self):
        return self.repository.find_all()

    def remove_product(self, product_id):
        self.repository.delete(product_id)


repository = ProductRepository()
service = ProductService(repository)

service.add_product(Product(1, "Book", 50000))
service.add_product(Product(2, "Keyboard", 150000))

for product in service.show_products():
    print(product.name, product.price)