class CustomerRepository:

    def __init__(self):
        self.customers = []

    def create(self, customer):
        self.customers.append(customer)
        return customer

    def get_all(self):
        return self.customers

    def read(self, customer_id):
        for customer in self.customers:
            if customer["customer_id"] == customer_id:
                return customer
        return None
